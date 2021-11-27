from django.db import models

class Edit(models.Model):
    name = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    collegeid = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    email = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')
    status = models.CharField(max_length=122,null=True,blank=True)
    proof = models.CharField(max_length=122,null=True,blank=True)
    verificationid = models.CharField(max_length=50,null=True,blank=True,default='Not Provided')

    def __str__(self):
        return self.collegeid

class Contact(models.Model):
    desc = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')

