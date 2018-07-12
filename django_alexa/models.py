from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AlexaSkill(models.Model):
    name = models.CharField("Name", max_length=100, )
    app_label = models.CharField("Django App Label", max_length=100,
                                 help_text="Enter the django app label this skill, needed to route incoming "
                                           "requests to the correct django app")
    created = models.DateTimeField(auto_now_add=True)
    skill_id = models.CharField("API Key", max_length=100, unique=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        verbose_name = 'Alexa Skill'
        verbose_name_plural = 'Alexa Skills'

    def __str__(self):
        if self.pk:
            return self.name
        else:
            return "New Alexa Skill"
