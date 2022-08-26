from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from django.contrib import admin
from apps.suscription.models import SuscriptionModel


class SuscriptionResource(resources.ModelResource):
    class Meta:
        model = SuscriptionModel
        fields = (
            'order',
            'id',
            'email',
            'created',
            'updated',
        )
        export_order = fields


@admin.register(SuscriptionModel)
class SuscriptionAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = SuscriptionResource

    list_display = (
        'order',
        'id',
        'email',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'email',
        'created',
        'updated',
    )

    search_fields = (
        'order',
        'id',
        'email',
        'created',
        'updated',
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
                'id',
                'order',
                'created',
                'updated',
            )
        }),
    )
