# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import AlexaSkill


@admin.register(AlexaSkill)
class AlexaSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'app_label', 'skill_id')
    list_filter = ('created',)
    search_fields = ('name',)
