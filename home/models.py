from django.db import models

class Edit(models.Model):
    name = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    collegeid = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    email = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    status = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    proof = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    verificationid = models.CharField(max_length=50,null=True,blank=True,default='Not Provided')

