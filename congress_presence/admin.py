from django.contrib import admin
from models import Participant


def make_absent(modeladmin, request, queryset):
    queryset.update(here=False)
make_absent.short_description = "Mark selected participants as missing"


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'lc']
    ordering = ['lc']
    actions = [make_absent]

admin.site.register(Participant, ParticipantAdmin)
