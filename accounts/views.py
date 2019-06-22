from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def profile(request):
  return render(request, 'profile.html')    