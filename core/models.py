from django.db import models
import uuid
from uuid import UUID

# ./manage.py migrate --fake core
# python manage.py migrate --fake core zero

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

class Process(models.Model):
     #user = models.ForeignKey(User)
     ref_number = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
     session_name = models.CharField(max_length=500, null=True, unique=True)

     def __str__(self):
        return self.session_name  
    #  def __init__(self):
    #      super(Process, self).__init__()
    #      self.ref_number = str(uuid.uuid4())

    #  def __unicode__(self):
    #     return self.user

class Document(models.Model):
    document = models.FileField(upload_to='', null=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=500, null=True, choices=POSITION_OPTIONS)
    process = models.ForeignKey(
        Process, to_field='ref_number',null=True, related_name="process", on_delete=models.CASCADE)
    # parent_name = models.OneToOneField(
    #    Process, on_delete=models.CASCADE, to_field='session_name', null=True, parent_link=True,  unique=True, related_name="parent_name")
    # def __str__(self):
    #     return self.document   


class Ret(models.Model):
    parent_ref_number = models.ForeignKey(
        Process, to_field='ref_number',null=True, related_name="parent_ref_number", on_delete=models.CASCADE)
    ret_position = models.ManyToManyField(
        Document, null=True, related_name="ret_position")
    ret_name = models.CharField(max_length=500, null=True)
    rret_name = models.CharField(max_length=500, null=True)
    station_id = models.CharField(max_length=500, null=True)
    aisg_version = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    bearing = models.CharField(max_length=500)
    hw_version = models.CharField(max_length=500)
    sector_id = models.CharField(max_length=500, null=True)
    #parent_file = models.ForeignKey(Document, on_delete=models.SET_NULL, related_name="parent_file", null=True)

    def __str__(self):
        return self.ret_name    


# class Unrelated(models.Model):
#     ret_name = models.CharField(max_length=500, null=True)
#     rret_name = models.CharField(max_length=500, null=True)
#     aisg_version = models.CharField(max_length=500)
#     address = models.CharField(max_length=500)
#     bearing = models.CharField(max_length=500)
#     hw_version = models.CharField(max_length=500)
#     #parent_file = models.ForeignKey(Document, on_delete=models.SET_NULL, related_name="parent_file", null=True)

#     def __str__(self):
#         return self.name    