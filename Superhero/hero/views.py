from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Superhero, User


class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = "heroes"


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = "hero"


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = ['name', 'identity', 'description',
              'image', 'strengths', 'weaknesses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/edit.html"
    model = User
    fields = ['username', 'email']
    success_url = reverse_lazy('edit')
