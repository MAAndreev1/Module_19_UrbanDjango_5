from django.contrib import admin
from task1.models import *

# Register your models here.
# admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', 'size', 'age_limited')
    fieldsets = (
        ('Description', {
            'fields':
                ('title', 'description')
        }),
        ('More', {
            'fields':
                ('cost', 'size', 'age_limited')
        })
    )