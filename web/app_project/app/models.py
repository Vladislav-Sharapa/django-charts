# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Messagelog(models.Model):
    yearreg = models.IntegerField()
    state = models.CharField(max_length=5)
    date_rcv = models.DateField()
    type_doc = models.CharField(max_length=7)
    custom = models.CharField(max_length=2, blank=True, null=True)
    pto = models.CharField(max_length=3, blank=True, null=True)
    declarant_unp = models.CharField(max_length=20, blank=True, null=True)
    fullname = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True) 
    status_doc = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messagelog'
