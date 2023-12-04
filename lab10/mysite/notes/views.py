from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegistrationForm
from .models import Note, Topic


class AddTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title']
    template_name = 'add_topic.html'


class AddNoteView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'contents', 'topic']
    template_name = 'add_note.html'  # Możesz utworzyć odpowiedni szablon HTML dla dodawania notatki

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Przypisanie aktualnie zalogowanego użytkownika jako właściciela
        return super().form_valid(form)


class UpdateNoteView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'contents']
    template_name = 'update_note.html'

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().created_by == self.request.user


class UpdateTopicView(UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title']
    template_name = 'update_topic.html'

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().created_by == self.request.user


class DeleteNoteView(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('add')  # Podaj nazwę URL, do którego ma wrócić po usunięciu notatki

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().created_by == self.request.user


class DeleteTopicView(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('add-topic')  # Podaj nazwę URL, do którego ma wrócić po usunięciu notatki

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().created_by == self.request.user


@login_required
def note_details_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'show_note.html', {'note': note})


@login_required
def topic_details_view(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'show_topic.html', {'topic': topic})


class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'topic_list.html'


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add-note'))
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world. You're at the notes index.")
