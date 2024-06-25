from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm, UserLoginForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login, authenticate

class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Vartotojo puslapis: {self.object.user.username}'
        return context

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profile_edit.html'
    success_message = 'Profilis sėkmingai atnaujintas'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Vartotojo profilio redagavimas: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:profile_detail', kwargs={'pk': self.request.user.profile.pk})

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('store:home')
    template_name = 'users/user_register.html'
    success_message = 'Jūs sėkmingai užsiregistravote. Galite prisijungti prie svetainės!'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registracija svetainėje'
        return context

class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/user_login.html'
    next_page = 'store:home'
    success_message = 'Sveiki atvykę į svetainę!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Prisijungimas prie svetainės'
        return context

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('store:home')

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/user_password_change.html'
    success_message = 'Jūsų slaptažodis sėkmingai pakeistas!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Slaptažodžio keitimas'
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile_detail', kwargs={'pk': self.request.user.profile.pk})
