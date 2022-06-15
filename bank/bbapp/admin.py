from django.contrib import admin
from .models import District,Branches,Gender,CardPreference,AccountDetails,AccountPreferance

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


class CenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', ]
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(District, DistrictAdmin)
admin.site.register(Branches, CenterAdmin)
admin.site.register(Gender)
admin.site.register(CardPreference)
admin.site.register(AccountDetails)
admin.site.register(AccountPreferance)