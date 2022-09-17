from django.contrib import admin
from .models import Portfolio,ServiceIcon,AboutUs,Enquiry
# Register your models here.
# for configuration of models 
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name','url','field')
    search_fields = ('name','url','field')
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('head','about')
    search_fields = ('head','about')
class ServiceIconAdmin(admin.ModelAdmin):
    list_display = ('Icon1','Icon2','Icon3','Icon4','Icon5','Icon6')
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','email','msg')
    search_fields = ('name','email','msg')
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(AboutUs,AboutusAdmin)
admin.site.register(ServiceIcon,ServiceIconAdmin)
admin.site.register(Enquiry,EnquiryAdmin)