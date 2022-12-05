from django.db import models
import uuid

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=50,null=True)
    student_mailid=models.EmailField(max_length=254,null=True)
    student_PRN=models.CharField(max_length=50,null=True)
    student_branch=models.CharField(max_length=30,null=True)
    student_year=models.CharField(max_length=30,null=True)
    student_semester=models.CharField(max_length=30,null=True)
    student_phno=models.CharField(max_length=30,null=True)

class teacher(models.Model):
    t_id = models.IntegerField(primary_key=True)
    t_name=models.CharField(max_length=50,null=True,blank=True)
    t_mail=models.EmailField(max_length=254,null=True,blank=True)
    t_phno=models.CharField(max_length=30,null=True,blank=True)
    t_Gender=models.CharField(max_length=50,null=True,blank=True)
    t_Occupation=models.CharField(max_length=50,null=True,)
    t_branch=models.CharField(max_length=50,null=True,blank=True)
    t_post=models.CharField(max_length=50,null=True,blank=True)
    t_DOB=models.DateField(max_length=50,null=True,blank=True)
    tid_name=models.CharField(max_length=50,null=True,blank=True)
    tid_no=models.CharField(max_length=50,null=True,blank=True)
    # t_pic=models.ImageField(upload_to='images')
    # t_issue_date=models.DateField(max_length=50,null=True)

class course(models.Model):
    c_teacher=models.ForeignKey(teacher, on_delete=models.CASCADE,max_length=50)
    c_code=models.CharField(primary_key=True,max_length=50,default=None)
    c_name=models.CharField(max_length=50,null=True)
    c_semester=models.CharField(max_length=30,null=True)
    c_credit=models.CharField(max_length=30,null=True)
    # c_Teacher=models.CharField(max_length=30,null=True)

class course_teacher(models.Model):
    c_id=models.ForeignKey(course, on_delete=models.CASCADE,max_length=50)
    c_teacher=models.ForeignKey(teacher, on_delete=models.CASCADE,max_length=50)
