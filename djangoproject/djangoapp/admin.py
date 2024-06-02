from django.contrib import admin
from .models import ExampleVariety,ExampleReview,ExampleStore,ExampleCertificate

# Register your models here.
class ExampleReviewInline(admin.TabularInline):
    model = ExampleReview
    extra = 2

class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ExampleReviewInline]

class ExampleStoreAdmin(admin.ModelAdmin):
    list_display = ('storeName','location')
    filter_horizontal = ('exampleVarieties',)

class ExampleCertificateAdmin(admin.ModelAdmin):
    list_display = ('exampleCertificateName','certificateNumber')

admin.site.register(ExampleVariety,ExampleModelAdmin)
admin.site.register(ExampleStore,ExampleStoreAdmin)
admin.site.register(ExampleCertificate,ExampleCertificateAdmin)