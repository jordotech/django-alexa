# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import AlexaSkill


@admin.register(AlexaSkill)
class AlexaSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created', 'app_label', 'skill_id')
    list_filter = ('created', 'active',)
    search_fields = ('name', 'active',)
