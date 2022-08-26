from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from django.contrib import admin

from apps.contactinfo.models import ContactInfoModel


class ContactInfoResource(resources.ModelResource):
    class Meta:
        model = ContactInfoModel
        fields = (
            'email',
            'zipCode',
            'state',
            'celPhone',
            'created',
            'updated',
            'order'
        )
        export_order = fields


@admin.register(ContactInfoModel)
class ContactInfoAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = ContactInfoResource

    list_display = (
        'id',
        'email',
        'celPhone',
        'state',
        'zipCode',
        'created',
        'updated',
        'order'
    )

    list_display_links = (
        'order',
        'id',
        'email',
    )

    list_filter = (
        'zipCode',
    )

    search_fields = (
        'email',
        'celPhone',
        'state',
        'zipCode',
    )

    readonly_fields = (
        'id',
        'created',
        'updated',
    )

    ordering = (
        "order",
    )

    fieldsets = (
        ("Data: ", {
            "fields": (
                'email',
                'celPhone',
                'state',
                'zipCode',
                'created',
                'updated',
                'order'
            )
        }),
    )
