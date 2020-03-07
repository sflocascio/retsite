from django.db import models
import uuid
from uuid import UUID
from django.utils import timezone
from django.contrib.auth.models import User


# ./manage.py migrate --fake core
# python manage.py migrate --fake core zero
# python manage.py migrate --fake-initial
# python manage.py migrate --fake core 0001
# python manage.py migrate --fake

# python manage.py sqlclear core
# BEGIN;
# DROP TABLE "Process";
# DROP TABLE "Document";
# DROP TABLE "Ret";

# COMMIT

POSITION_OPTIONS = (  
    ('alpha_pos_1', 'alpha_pos_1'),
    ('alpha_pos_2', 'alpha_pos_2'),
)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Process(models.Model):
    #Essentials
     ref_number = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
     created_date = models.DateTimeField('date created', default=timezone.now)
     fcc_id = models.CharField(max_length=500, null=True)
     #Non Essentials: 
     site_common_name = models.CharField(max_length=500, null=True)
     market = models.CharField(max_length=500, null=True)
     enode_b_id = models.CharField(max_length=500, null=True) 
     ptn = models.CharField(max_length=500, null=True)
     release = models.CharField(max_length=500, null=True)
     cross_sector_redundency = models.BooleanField(default=True)

    #  user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="user")

     def __str__(self):
        return self.site_common_name 
    #  def __init__(self):
    #      super(Process, self).__init__()
    #      self.ref_number = str(uuid.uuid4())

    #  def __unicode__(self):
    #     return self.user

class Document(models.Model):
    document = models.FileField(upload_to='', null=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=500, null=True, choices=POSITION_OPTIONS)
    connected_rrh_serial = models.CharField(max_length=500, null=True) #This comes from user entry
    process = models.ForeignKey(
        Process, to_field='ref_number',null=True, related_name="process", on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.document   


class Ret(models.Model):
    parent_ref_number = models.ForeignKey(
        Process, to_field='ref_number',null=True, related_name="parent_ref_number", on_delete=models.CASCADE)
    ret_position = models.CharField(max_length=500, null=True) #Alpha Gamma Beta, Pos 1,2,3 ETC
    antenna_serial_number = models.CharField(max_length=500, null=True)
    device_serial = models.CharField(max_length=500, null=True)
    antenna_serial_number = models.CharField(max_length=500, null=True)
    antenna_model = models.CharField(max_length=500, null=True)
    aisg_version = models.CharField(max_length=500)
    ret_name = models.CharField(max_length=500, null=True)
    station_id = models.CharField(max_length=500, null=True)
    tilt_range = models.CharField(max_length=500, null=True)
    electrical_tilt = models.CharField(max_length=500, null=True)
    
    usid = models.CharField(max_length=500, null=True)
    base_station_id = models.CharField(max_length=500, null=True)
    sector_id = models.CharField(max_length=500, null=True)
    
    relative_antenna_position = models.CharField(max_length=500, null=True)
    bearing = models.CharField(max_length=500)
    operating_band = models.CharField(max_length=500, null=True) #Numbers or Pairs (ex: 700/800) based off Band table ...
    band = models.CharField(max_length=500, null=True) #Simply 1 character such (ex: 2, 3, E, K) etc.. 
    technology = models.CharField(max_length=500, null=True) #Simply 1 Letter (ex: L, U, F, N )
    eutran_cell_id = models.CharField(max_length=500, null=True)
    ret_sub_unit = models.CharField(max_length=500, null=True) #This is (station_id + eutran_cell_id)
    address = models.CharField(max_length=500)
    
    hw_version = models.CharField(max_length=500)
    installation_date = models.CharField(max_length=500, null=True)
    installer_id = models.CharField(max_length=500, null=True)
    ret_cell_id = models.CharField(max_length=500, null=True)

    #parent_file = models.ForeignKey(Document, on_delete=models.SET_NULL, related_name="parent_file", null=True)

    def __str__(self):
        return self.sector_id   


class Technology(models.Model):
    parent_ref_number = models.ForeignKey(
        Process, to_field='ref_number',null=True, related_name="parent_ref_number_tech", on_delete=models.CASCADE)
    technology_operating_band = models.CharField(max_length=500, null=True)
    technology_cell_id = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.technology_operating_band   