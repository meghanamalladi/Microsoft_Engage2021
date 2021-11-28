from django.db import models

status_choices = (
    ("Not Yet Vaccinated","Not Yet Vaccinated"),
    ("Partially Vaccinated","Partially Vaccinated"),
    ("Fully Vaccinated","Fully Vaccinated"),
)
proof_choices = (
    ("Aadhar Card", "Aadhar Card"),
    ("PAN Card","PAN Card"),
    ("Mobile Number", "Mobile Number"),
)

class Upload(models.Model):
    name = models.CharField(max_length=122,default='Not Provided')
    collegeid = models.CharField(max_length=122,null=True,blank=True)
    email = models.CharField(max_length=122)
    status = models.CharField(max_length=122,choices = status_choices, default = 'Not Yet Vaccinated')
    proof = models.CharField(max_length=122,choices = proof_choices, default = 'Aadhar Card')
    verificationid = models.CharField(max_length=50,null=True,blank=True)
    verificationpdf = models.FileField(upload_to='pdfs', default='settings.MEDIA_ROOT/pdfs/default.pdf')   

    def __str__(self):
        return self.name

class Contact(models.Model):
    desc = models.CharField(max_length=122,null=True,blank=True,default='Not Provided')

