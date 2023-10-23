from django.contrib import admin
from pro13app.models import Sangdata

# Register your models here.
class SangAdmin(admin.ModelAdmin):
    list_display=('code','sang','su','dan')
    
admin.site.register(Sangdata, SangAdmin)