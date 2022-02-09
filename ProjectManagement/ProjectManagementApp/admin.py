from django.contrib import admin
from .models import Disasters,Projects,Enrichment,Csvs

'''from import_export.admin import ImportExportModelAdmin
@admin.register(Csvs)
class CsvsAdmin(ImportExportModelAdmin):
    pass'''

admin.site.register(Disasters)
admin.site.register(Projects)
admin.site.register(Enrichment)
admin.site.register(Csvs)



