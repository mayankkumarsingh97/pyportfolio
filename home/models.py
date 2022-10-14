from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Resume(models.Model):
    resume_heading=models.CharField(max_length=100,blank=True,null=True)
    resume= models.FileField(upload_to='resume_mayank', blank=True)

    def __str__(self):
        return self.resume_heading



class Contactus(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='Name')
    lastname = models.CharField(max_length=200, blank=True, verbose_name='lastname')
    email = models.CharField(max_length=200, blank=False, verbose_name='Email')
    phone = models.CharField(max_length=12, blank=True, verbose_name='Phone')
    message = models.TextField(max_length=300, blank=True, verbose_name='Message')

    def __str__(self):
        return self.name

class contactUsForm(ModelForm):
    class Meta:
        model = Contactus
        fields = [ 'name', 'lastname','email','phone', 'message']
           

class mywork(models.Model):
    link_info=models.CharField(max_length=100,blank=True,null=True)
    link= models.URLField(max_length = 200,blank=True,null=True)


    def __str__(self):
        return self.link_info           




class TechSkills(models.Model):
    links=models.URLField(max_length = 200,blank=True,null=True)
    skill_desc=RichTextField(blank=True,null=True)


    def __str__(self):
        return self.skill_desc


class socialicons(models.Model):
    icon_name=models.CharField(max_length=100,blank=True,null=True)
    icon_image=models.FileField(upload_to ='uploads/',blank=False,null=True)
    icon_link= models.URLField(max_length = 200,blank=False,null=True)


    def __str__(self):
        return self.icon_name           