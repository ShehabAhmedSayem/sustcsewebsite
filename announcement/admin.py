from django.contrib import admin

from .models import Notice, ProgramCategory


class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title of the notice', {'fields': ['title']}),
        ('Program and Year', {'fields': ['program_year']}),
        ('Upload the Pdf file of the notice', {'fields': ['upload']}),
    ]

    list_display = ('title', 'program_year', 'date_published')
    list_filter = ['date_published', 'program_year']
    search_fields = ['title']


admin.site.register(ProgramCategory)
admin.site.register(Notice, NoticeAdmin)

