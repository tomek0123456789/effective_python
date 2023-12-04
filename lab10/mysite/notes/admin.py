from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Topic


class TopicAdmin(DjangoMpttAdmin):
    list_display = ('title', 'parent', 'public',)
    list_editable = ('public',)  # Dodaj pole do edycji z listy


admin.site.register(Topic, TopicAdmin)
