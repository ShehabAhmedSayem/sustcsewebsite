from django.contrib import admin
from .models import *

admin.site.register(ResearchGroup)
admin.site.register(ResearchGroupNotice)
admin.site.register(ResearchGroupFaculty)
admin.site.register(ResearchGroupStudent)
admin.site.register(ResearchGroupResource)
admin.site.register(ResearchGroupProject)
admin.site.register(PublicationType)
admin.site.register(Publication)