# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   *` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Senator(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    first = models.CharField(blank=True, null=True, max_length= 200)
    last = models.CharField(blank=True, null=True, max_length = 200)
    party = models.CharField(blank=True, null=True, max_length = 200)
    class_field = models.CharField(db_column='class', blank=True, null=True, max_length = 200)  # Field renamed because it was a Python reserved word.
    state = models.CharField(blank=True, null=True, max_length = 200)
    start = models.IntegerField(blank = True, null = True)
    end = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'senators'

class Bill(models.Model):
    bill_id = models.IntegerField(primary_key=True, blank=True, null=False)
    title = models.TextField(blank=True, null=True)
    status = models.CharField(blank=True, null=True, max_length = 200)
    introduced_date = models.CharField(blank=True, null=True, max_length = 200)
    sponsor = models.ForeignKey(Senator, null = True)
    congress = models.CharField(blank = True, null = True, max_length = 10)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bills'

class Cosponsorship(models.Model):
    action_id = models.IntegerField(primary_key=True, blank=True, null=False)
    bill = models.IntegerField(blank=True, null=True)
    cosponsor = models.ForeignKey(Senator, null = True)
    joined_date = models.CharField(blank=True, null=True, max_length = 50)

    def __str__(self):
        return str(self.bill)

    class Meta:
        db_table = 'cosponsorships'

class Leadership(models.Model):
    senator_id = models.IntegerField(blank = True, null = True)
    congress = models.IntegerField(blank = True, null = True)
    bill_success_score = models.IntegerField(blank = True, null = True)
    cosponsors_out = models.IntegerField(blank = True, null = True)
    cosponsors_in = models.IntegerField(blank = True, null = True)

    class Meta:
        db_table = 'leadership'