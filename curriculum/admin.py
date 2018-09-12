from django.contrib import admin

from .models import *


class ProgramAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Program name', {'fields': ['program_name']}),
        ('Details of the program', {'fields': ['details']}),
        ('Admission Form of the program', {'fields': ['admission_form']}),
    ]


class CourseAdmin(admin.ModelAdmin):
    fields = (
        ('program_name', 'year_semester'),
        ('course_type', 'course_title'),
        ('course_code', 'course_credit'),
        'course_details',
    )
    list_display = ('course_code', 'course_title', 'year_semester')
    list_filter = ('program_name', 'year_semester')
    search_fields = ['course_title', 'course_code']


admin.site.register(Program, ProgramAdmin)
admin.site.register(Semester)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class)



