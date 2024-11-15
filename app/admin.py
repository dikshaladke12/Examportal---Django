from django.contrib import admin
from .models import *

admin.site.register(User)

# admin.site.register(UserTable)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(AnswerTable)
admin.site.register(resetuuid)