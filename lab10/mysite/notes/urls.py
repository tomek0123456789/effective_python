from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import AddNoteView, UpdateNoteView, DeleteNoteView, index, registration_view, note_details_view, \
    AddTopicView, UpdateTopicView, DeleteTopicView, topic_details_view, TopicListView

urlpatterns = [
    path("", index, name="index"),
    path('login/', LoginView.as_view(template_name="login.html", success_url='dodaj/'), name='login'),
    path('register/', registration_view, name='register'),
    path('add/', AddNoteView.as_view(), name='add-note'),
    path('add_topic/', AddTopicView.as_view(), name='add-topic'),
    path('edit/<int:pk>/', UpdateNoteView.as_view(), name='update-note'),
    path('edit_topic/<int:pk>/', UpdateTopicView.as_view(), name='update-topic'),
    path('delete/<int:pk>/', DeleteNoteView.as_view(), name='delete-note'),
    path('delete_topic/<int:pk>/', DeleteTopicView.as_view(), name='delete-topic'),
    path('show/<int:pk>', note_details_view, name='show-note'),
    path('show_topic/<int:pk>', topic_details_view, name='show-topic'),
    path('topic_list/', TopicListView.as_view(), name='topic-list'),
    # Tutaj <int:pk> to identyfikator notatki, który będzie przekazywany do widoków UpdateView i DeleteView
]
