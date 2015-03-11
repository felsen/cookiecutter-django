# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from {{cookiecutter.repo_name}}.base.models import UUIDModel


class User(UUIDModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=60, blank=False, null=False,
                                unique=True, db_index=True)
    name = models.CharField(_('name'), max_length=255, blank=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True,
                              max_length=254)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
