from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created = models.DateTimeField(verbose_name=None, name=None, auto_now=True, editable=False)
    # modified = models.DateTimeField(verbose_name=None, name=None,
    # auto_now=False, auto_now_add=False, default=timezone.now)
    profile_pic = models.ImageField(verbose_name=None, name=None,
                                    width_field=None, height_field=None, upload_to="profile_pic/%Y/%m/%d/")
    mobile_no = models.IntegerField(verbose_name=None, name=None, primary_key=False, max_length=None, unique=False, blank=False, null=False,
                                    db_index=False, rel=None, default=0, editable=True,
                                    serialize=True, unique_for_date=None, unique_for_month=None, unique_for_year=None, choices=None,
                                    help_text='', db_column=None, db_tablespace=None, auto_created=False, validators=(), error_messages=None)


    def __str__(self):
        return "{}".format(self.user)

class Adress(models.Model):
        address1 = models.CharField(blank=True, null= True, max_length= 999999)
        address2 = models.CharField(blank=True, null= True, max_length= 999999)
        country = models.CharField(blank=True, null= True,max_length=120)
        state = models.CharField(blank=True, null= True,max_length=120)
        city = models.CharField(blank=True, null= True,max_length=120)
        zipcode = models.IntegerField(blank=True, null= True,default=0)

        def __str__(self):
            return "{0}/n{1}/n{2}/n{3}/n{4}/n{5}".format(address1, address2,
                                                        country, state, city,
                                                        zipcode)



@ receiver(user_signed_up)
def uerprofilecreat(request, user, **kwargs):
    if kwargs.get('created'):
        UserProfile.objects.get_or_create(user=user)


class Friends(models.Model):
    friend = models.ManyToManyField(UserProfile )
    creator = models.OneToOneField(UserProfile, related_name="owner",
                                   on_delete=models.CASCADE, null=True)
