from django.contrib import admin
from .models import student
from .models import teacher
from .models import course
from .models import course_teacher


class StudentAdmin(admin.ModelAdmin):
     list_display=('student_name','student_mailid','student_PRN','student_branch','student_year','student_semester','student_phno')

admin.site.register(student,StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
     list_display=('t_name','t_mail','t_phno','t_Gender','t_DOB','t_Occupation','tid_name','tid_no','t_branch','t_post')
# class TeacherAdmin(admin.ModelAdmin):
     # list_display=('tid_name','tid_no','t_id')

admin.site.register(teacher,TeacherAdmin)

class CourseAdmin(admin.ModelAdmin):
     list_display=('c_name','c_code','c_semester','c_credit')

admin.site.register(course,CourseAdmin)


# class CteacherAdmin(admin.ModelAdmin):
#      # list_display=(' c_id',' c_teacher')

# admin.site.register(course_teacher,CteacherAdmin)






# Register your models here.
