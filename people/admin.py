from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'is_faculty', 'is_staff')

    fieldsets = (
        (('Login info'), {'fields': ('email', 'password')}),
        (('Additional info'), {'fields': ('is_faculty',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_faculty')}
        ),
    )


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'designation', 'order_number', 'organization')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Faculty)
admin.site.register(SocialProfile)
admin.site.register(Staff)
admin.site.register(Award)
admin.site.register(Batch)
admin.site.register(Education)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Student)
admin.site.register(ResearchStudent)
admin.site.register(ResearchArea)
