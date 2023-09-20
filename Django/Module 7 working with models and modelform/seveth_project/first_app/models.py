
from typing import Any
from django.db import models


# Create your models here.
    
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f'Name : {self.name}'
    
# model inheritance:
# 1. Abstract base class (never make a object!!)
# 2. multitable inheritance
# 3. Proxy model



# make abstract base class
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    class Meta:
        abstract = True        

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()    
    payment = models.IntegerField()
    section  = models.CharField(max_length=50)


class TeacherInfoModel(CommonInfoClass):    
    salary = models.IntegerField()
    
    
# multitable inheritance
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)
    
class ManageModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()  


# proxy Model inheritance--

class Friend(models.Model): # amar friend classe presnt ase
    school = models.CharField(max_length=50)
    section = models.CharField(max_length=20)
    attendance = models.BooleanField()
    hw =models.CharField(max_length=15)
    
class Me(Friend):#ami ajke classe jay ni
    class Meta:
        proxy = True
        ordering = ['id'] # initialy - hisebe thake but eivabe ['id'] ta positive hesebe count hoy


# Relationship model--
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.name
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
# 1. one to many relationship or many to one
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)


# 2. many to many relationship--
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name= "teachers")
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return " , ".join([str(i) for i in self.student.all()])