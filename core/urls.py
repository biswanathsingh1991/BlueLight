
from django.urls import path, re_path
from .views import (Home, ajaxableusername, ajaxableemail,
                    AllUserProfile, addfriend, ProfileDetailView, UserProfileEdit,
                    )
from django.contrib.auth import views as auth_views
from . form import LoginForm


app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('usercreation', UserCreation.as_view(), name='usercreation'),
    re_path(r'^userprofileedit/(?P<pk>[0-9]+)/$',
            UserProfileEdit.as_view(), name='userprofileedit'),
    path('profiledetailview/', ProfileDetailView.as_view(),
         name='profiledetailview'),
    path('home', Home.as_view(), name='home'),
    # path('login', auth_views.LoginView.as_view(template_name='core/login0.html',
    # authentication_form = LoginForm), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # path('passwordchange', auth_views.PasswordChangeView.as_view(
    #     template_name='core/passwordchange.html'), name='passswordchange'),
    # path('password_reset', auth_views.PasswordResetView.as_view(
    #     template_name='core/password_reset_form.html',
    #     email_template_name='core/password_reset_email.html',
    #     subject_template_name='core/password_reset_subject.txt'
    # ), name='password_reset'),
    # path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
    #     template_name='core/password_reset_done.html'),
    #     name=' password_reset_done'),
    # path('password_reset_confirm', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='core/password_reset_confirm.html'),
    #     name='password_reset_confirm'),
    # path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='core/password_reset_complete.html'),
    #     name='password_reset_complete'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('ajaxableusername/', ajaxableusername, name='ajaxableusername'),
    path('ajaxableemail/', ajaxableemail, name='ajaxableemail'),
    path('alluserprofile/', AllUserProfile.as_view(), name='alluserprofile'),
    path('addfriend/', addfriend, name='addfriend')
]
