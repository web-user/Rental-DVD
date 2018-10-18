from django.contrib import admin

# Register your models here.
from .models import Dvd

class DvdAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    class Meta:
        model = Dvd

admin.site.register(Dvd, DvdAdmin)
