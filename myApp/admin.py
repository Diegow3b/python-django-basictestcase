from django.contrib import admin
from myApp.models import myModel

# Register your models here.
class AdminMyModel(admin.ModelAdmin):
    list_display = ('atributo_string',
                    'atributo_int',
                    'atributo_boolean')
    list_filter = ('atributo_string',)

admin.site.register(myModel, AdminMyModel)