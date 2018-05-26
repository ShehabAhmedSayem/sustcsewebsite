from django.contrib import admin

from .models import Curriculum


class CurriculumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Program name for curriculum', {'fields': ['program_name']}),
        ('Details of that curriculum page', {'fields': ['curriculum_details']}),
    ]


admin.site.register(Curriculum, CurriculumAdmin)


