# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Adherents(models.Model):

    #__Adherents_FIELDS__
    nom = models.TextField(max_length=255, null=True, blank=True)
    prenom = models.TextField(max_length=255, null=True, blank=True)
    studient number = models.TextField(max_length=255, null=True, blank=True)

    #__Adherents_FIELDS__END

    class Meta:
        verbose_name        = _("Adherents")
        verbose_name_plural = _("Adherents")


class Product(models.Model):

    #__Product_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Transactions(models.Model):

    #__Transactions_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(null=True, blank=True)

    #__Transactions_FIELDS__END

    class Meta:
        verbose_name        = _("Transactions")
        verbose_name_plural = _("Transactions")



#__MODELS__END
