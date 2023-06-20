from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField("First name", max_length=255, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

from django.db import models

class Core(models.Model):
    id_core = models.AutoField(primary_key=True)
    registered_by = models.CharField(max_length=50)
    well_name = models.CharField(max_length=50)
    well_name_short = models.CharField(max_length=10)
    core_num = models.IntegerField()
    core_section = models.IntegerField()
    core_sec_name = models.CharField(max_length=50)
    collection_date = models.DateField()
    planned_core_num = models.IntegerField()
    top_depth = models.DecimalField(max_digits=10, decimal_places=2)
    bottom_depth = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField()
    core_sec_length = models.DecimalField(max_digits=10, decimal_places=2)
    core_recovery = models.DecimalField(max_digits=10, decimal_places=2)
    core_diameter = models.DecimalField(max_digits=10, decimal_places=2)
    coring_method = models.CharField(max_length=50)
    coreliner = models.CharField(max_length=50)
    lithology = models.CharField(max_length=50)
    core_status = models.CharField(max_length=50)
    preservation = models.CharField(max_length=50)
    core_weight = models.DecimalField(max_digits=10, decimal_places=2)
    radiation = models.CharField(max_length=50)
    registration_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.firstName