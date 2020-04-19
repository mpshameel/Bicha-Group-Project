from django.db import models

# Create your models here.

class job_post(models.Model):
    img         = models.ImageField(upload_to='jobpost')
    title       = models.CharField(max_length=200)
    company_name= models.CharField(max_length=200)
    des         = models.TextField()
    job_nature  = models.CharField(max_length=200)
    location    = models.CharField(max_length=200)
    salary      = models.CharField(max_length=100)
    tag_1       = models.CharField(max_length=100)
    tag_2       = models.CharField(max_length=100)
    tag_3       = models.CharField(max_length=100)
    datetime    = models.DateTimeField(null=True)
    code        = models.CharField(max_length=100)




class applyed_candidates(models.Model):
    code                        =   models.CharField(max_length=100)
    candidates_givenname        = models.CharField(max_length=200)
    candidates_surename         = models.CharField(max_length=200)
    candidates_email            = models.EmailField()
    candidates_phonenumber      = models.BigIntegerField()
    candidates_resume           = models.FileField(upload_to='CandidatesResume')

    

class imp_messages(models.Model):
    message         = models.TextField()
    datetime        = models.DateTimeField()    


