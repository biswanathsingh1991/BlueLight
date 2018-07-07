
from django.views.generic import TemplateView, DetailView, ListView, UpdateView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from . models import UserProfile, Friends
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured


class Home(TemplateView):

    template_name = 'core/home.html'


class UserCreation(CreateView):  # user creation generic view
    model = User
    template_name = 'core/singup.html'
    fields = "__all__"


class UserProfileEdit(UpdateView):
    model = UserProfile
    template_name = "core/userprofile_edit.html"
    success_url = 'core:home'
    fields = "__all__"

# #
# class UserDetailView(DetailView):
#     model = UserProfile
#     template_name = 'core/userdetailview.html'


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'core/profiledetailview.html'

    def get_object(self, queryset=None):
        login_user = self.request.user
        obj = login_user.userprofile
        return obj


def ajaxableusername(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        data = {'used': User.objects.filter(username__iexact=username).exists(),
                'mssg': username+" allready exist", }
    return JsonResponse(data)


def ajaxableemail(request):

    if request.method == 'GET':
        email = request.GET.get('email')
        data = {'used': User.objects.filter(email__iexact=email).exists(),
                'mssg': email+" allready exist", }
    return JsonResponse(data)


class AllUserProfile(ListView):
    model = UserProfile
    template_name = 'core/alluserprofile.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


def addfriend(request):
    profile = int(request.GET.get('profile'))
    userprofile = UserProfile.objects.get(user=request.user)
    friend_object, created = Friends.objects.get_or_create(creator=userprofile)
    add_friend = UserProfile.objects.get(pk=profile)
    friend_object.friend.add(add_friend)
    data = {
        'mssg': "{} added to your friend list".format(add_friend)
    }
    return JsonResponse(data)
