# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Bills(models.Model):
    bill_id = models.IntegerField(primary_key=True, blank=True, null=False)
    title = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    introduced_date = models.TextField(blank=True, null=True)
    sponsor_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bills'


class Cosponsorships(models.Model):
    action_id = models.IntegerField(primary_key=True, blank=True, null=False)
    bill = models.IntegerField(blank=True, null=True)
    cosponsor = models.IntegerField(blank=True, null=True)
    joined_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cosponsorships'


class Senators(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    first = models.TextField(blank=True, null=True)
    last = models.TextField(blank=True, null=True)
    party = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    rank = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'senators'
