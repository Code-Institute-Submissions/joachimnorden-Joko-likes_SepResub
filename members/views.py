from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import (SignUpForm, EditProfileForm,
                    PasswordChangingForm, ProfilePageForm)
from blog.models import Profile


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create-user-profile-page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit-profile-page.html"
    fields = ["bio", "profile_pic"]
    success_url = reverse_lazy("home")


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "registration/user-profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context = super(
            ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("password-success")


def password_success(request):
    return render(request, "registration/password-success.html", {})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit-settings.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
