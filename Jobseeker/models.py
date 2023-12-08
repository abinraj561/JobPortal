from django.db import models
from Employer.models import Jobs,MyUser

class JobseekerProfile(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name="jobseeker")
    username = models.CharField(max_length=30)
    DOB = models.DateField(null=True)
    qualification = models.CharField(max_length=120)
    skills = models.CharField(max_length=100)
    experience=models.PositiveIntegerField()
    cv=models.FileField(upload_to="files",null=True)
    
class Applications(models.Model):
    user=models.ForeignKey(JobseekerProfile,on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    submitted_date=models.DateField(auto_now_add=True)
    options=(("accepted","accepted"),
             ("rejected","rejected"))
    status=models.CharField(max_length=15,choices=options)
    Interview_Date=models.DateField(null=True)
