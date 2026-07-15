from django.db import models
from django.conf import settings

class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='study_groups')
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='studygroups')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name