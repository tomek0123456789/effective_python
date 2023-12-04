from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Topic(TitleSlugDescriptionModel, TimeStampedModel, MPTTModel):
    public = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def get_absolute_url(self):
        return reverse('add-topic')

    def __str__(self):
        return self.title

    public = models.BooleanField(default=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']


class Note(TimeStampedModel):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('add-note')
