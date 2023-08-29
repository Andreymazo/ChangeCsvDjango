from django.contrib import admin
from change_csv.models import Sdelka, CounterAgent#, CellValue
from mptt.admin import MPTTModelAdmin
from change_csv.models import CellValue

admin.site.register(CellValue, MPTTModelAdmin)
admin.site.register(CounterAgent)
# admin.site.register(Sdelka)
#############################################################3
class CellValueInline(admin.TabularInline):
    model = CellValue
class ModelForBuild1Admin(admin.ModelAdmin):
    inlines = [
        CellValueInline,
    ]
    list_display = ['id', 'name',]
    list_filter = ['name']
    search_fields = ("name", )
# class SdelkaAdmin(admin.ModelAdmin):
    # '','preview', , 'date_of_creation', 'date_last_change'
    

admin.site.register(Sdelka, ModelForBuild1Admin)




# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     pass
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['name', ]
#     list_filter = ['name']
#     admin.site.register(Person)
