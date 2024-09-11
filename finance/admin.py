from django.contrib import admin
from finance.models import Organization, Campaign, Donor, Textmessage, Sponsor, Transaction, paymentMethod



# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['ID', 'NAME']

class DonorAdmin(admin.ModelAdmin):
    list_display = ['donorID', 'username']

class CampaignAdmin(admin.ModelAdmin):
    list_display = ['CamID', 'Name']


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['Sponsor_id', 'Name', 'Address']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'amount']

class TextmessageAdmin(admin.ModelAdmin):
    list_display = ['MesID', 'Timestamp']

class paymentMethodAdmin(admin.ModelAdmin):
    list_display = ['method']




admin.site.register(Donor, DonorAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Textmessage, TextmessageAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(paymentMethod, paymentMethodAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Transaction, TransactionAdmin)

