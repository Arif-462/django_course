from django.contrib import admin    
# from . import models, StudentInfoModel,TecherInfoModel

from first_app.models import StudentModel ,StudentInfoModel,TeacherInfoModel,EmployeeModel,ManageModel,Friend,Me, Person, Passport,Post, Student, Teacher

# Register your models here---
admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)
## multitable inheritance----
# admin.site.register(EmployeeModel)
# admin.site.register(ManageModel)

# model admin cutomize and multitable for custom display--
# @admin.register(EmployeeModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name','designation', 'city']
# @admin.register(ManageModel)
# class ManagerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name','designation', 'city', 'take_interview', 'hiring']


# @admin.register(Friend)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'school','attendance', 'section', 'hw']
    
# @admin.register(Me)
# class MeModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'school','attendance', 'section', 'hw']

@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','city', 'email']
    
@admin.register(Passport)
class passpertModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','pass_number', 'page', 'validity']
    
    
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','post_cap', 'post_details', 'created_at']
    

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll', 'class_name']
    
@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject','student_list', 'mobile']
    

    
