from django.contrib import admin

# Register your models here.
from .models import Dvd, Rent


class DvdAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    class Meta:
        model = Dvd

admin.site.register(Dvd, DvdAdmin)


class RentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rent._meta.fields]

    class Meta:
        model = Rent

    def date_took(self, obj):
        return obj.date.strftime('%d %b %Y %H:%M')
    date_took.short_description = 'Date'

admin.site.register(Rent, RentAdmin)