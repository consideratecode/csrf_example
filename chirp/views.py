from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.crypto import get_random_string
from django.urls import reverse

from .forms import StatusForm

def create_user(request):
    """Creates a user with random username and password and logs in the user."""
    if request.method == 'POST':
        username = get_random_string(16)
        password = get_random_string(16)
        user = User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('chirp:create_status'))
    else:
        return render(request, 'create_user.html')


@login_required
def create_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            while request.user.status_set.count() > 10:
                request.user.status_set.order_by('created_at').first().delete()
            success_url = reverse('chirp:profile',
                                  kwargs={'username': request.user.username})
            return HttpResponseRedirect(success_url)
    else:
        form = StatusForm(user=request.user)
    return render(request, 'create_status.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'status_list.html', {'user': user})


def logout_view(request):
    if request.method == 'POST' or not request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect(reverse('chirp:create_user'))
    else:
        return render(request, 'logout.html')
