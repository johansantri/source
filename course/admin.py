from django.contrib import admin

# Register your models here.
from .models import Partner, Course, Category
from django.contrib.auth.models import User


admin.site.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display=('partner_name','partner_join')
    list_filter = ('status')
    search_fields = ('partner_name')
    
admin.site.register(Course)


admin.site.register(Category)

