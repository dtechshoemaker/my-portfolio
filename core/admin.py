from django.contrib import admin
from .models import Project, Stack
from django.utils.safestring import mark_safe


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'stack', 'image_preview')  # Display fields in list view
    list_filter = ('stack',)  # Add filters based on stack
    search_fields = ('title', 'description')  # Enable search fields
    readonly_fields = ('image_preview',)  # Display image preview as readonly field

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
        else:
            return 'No Image'

    image_preview.short_description = 'Image Preview'

@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display fields in list view

admin.site.register(Project, ProjectAdmin)
