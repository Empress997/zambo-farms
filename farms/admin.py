from django.contrib import admin
from farms.models import *
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    prepopulated_fields = {"slug": ("title", )}

class CropAdmin(ImportExportActionModelAdmin , admin.ModelAdmin):
    pass
    fieldsets = (
        ("Crop Description", {"fields": ("title", "slug", "category","crop_description","crop_image")}),
        ("Crop Methodology", {"fields": ("crop_preparation", "crop_planting", "crop_management")}),
        ("Risk Assessment For Dry Season", {"fields": ("risk_dry_pest", "risk_dry_disease", "prevention_dry_pest", "prevention_dry_disease")}),
        ("Risk Assessment For Rainy Season", {"fields": ("risk_rainy_pest", "risk_rainy_disease", "prevention_rainy_pest", "prevention_rainy_disease")}),
    )
    list_per_page = 10
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Crop, CropAdmin)
admin.site.register(NewsLetter)
admin.site.register(Contact)
admin.site.register(WhatsNew)