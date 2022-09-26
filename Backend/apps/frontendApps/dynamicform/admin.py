from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from django.contrib import admin
from apps.frontendApps.dynamicform.models import (
    TVSizeModel,
    TVSurfaceModel,
    TVWallMountModel,
    TVHandleCordsModel,
    TVOtherInstallsModel,
    TVQuestionsModel,
    TVWallMountInstallationModel
)


class TVSizeResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'title',
            'description',
            'size',
            'price',
            'created',
            'updated',
        )
        export_order = fields


class TVSurfaceResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'title',
            'description',
            'price',
            'created',
            'updated',
        )
        export_order = fields


class TVWallMountResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'title',
            'description',
            'price',
            'created',
            'updated',
        )
        export_order = fields


class TVHandleCordsResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'title',
            'description',
            'price',
            'created',
            'updated',
        )
        export_order = fields


class TVOtherInstallsResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'title',
            'description',
            'price',
            'created',
            'updated',
        )
        export_order = fields


class TVQuestionsResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'title',
            'description',
            'price',
            'created',
            'updated',
        )
        export_order = fields


class TVOtherQuestionsResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'questions',
            'created',
            'updated',
        )
        export_order = fields


class TVWallMountInstallationResource(resources.ModelResource):
    class Meta:
        model = TVSizeModel
        fields = (
            'order',
            'id',
            'helpTechnician',
            'takeDownTV',
            'comments',
            'TVsize',
            'TVsurface',
            'TVWallMount',
            'TVHandleCords',
            'TVOtherInstalations',
            'otherQuestions',
            'created',
            'updated',
        )
        export_order = fields


@admin.register(TVSizeModel)
class TVSizeAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVSizeResource

    list_display = (
        'order',
        'id',
        'title',
        'description',
        'size',
        'price',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'title',
    )

    list_filter = (
        'size',
        'price',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'size',
        'price',
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
                'order',
                'id',
                'title',
                'description',
                'size',
                'price',
                'img',
                'created',
                'updated',
            )
        }),
    )


@admin.register(TVSurfaceModel)
class TVSurfaceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVSurfaceResource

    list_display = (
        'order',
        'id',
        'title',
        'description',
        'price',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'title',
    )

    list_filter = (
        'price',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'price',
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
                'order',
                'id',
                'title',
                'description',
                'price',
                'img',
                'created',
                'updated',
            )
        }),
    )


@admin.register(TVWallMountModel)
class TVWallMountAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVWallMountResource

    list_display = (
        'order',
        'id',
        'title',
        'description',
        'price',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'title',
    )

    list_filter = (
        'price',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'price',
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
                'order',
                'id',
                'title',
                'description',
                'price',
                'img',
                'created',
                'updated',
            )
        }),
    )


@admin.register(TVHandleCordsModel)
class TVHandleCordsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVHandleCordsResource

    list_display = (
        'order',
        'id',
        'title',
        'description',
        'price',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'title',
    )

    list_filter = (
        'price',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'price',
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
                'order',
                'id',
                'title',
                'description',
                'price',
                'created',
                'updated',
            )
        }),
    )


@admin.register(TVOtherInstallsModel)
class TVOtherInstallsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVOtherInstallsResource

    list_display = (
        'order',
        'id',
        'title',
        'description',
        'price',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'title',
    )

    list_filter = (
        'price',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'price',
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
                'order',
                'id',
                'title',
                'description',
                'price',
                'img',
                'created',
                'updated',
            )
        }),
    )


@admin.register(TVQuestionsModel)
class TVQuestionsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVQuestionsResource

    list_display = (
        'order',
        'id',
        'title',
        'description',
        'price',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
        'title',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'price',
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
                'order',
                'id',
                'title',
                'description',
                'price',
                'img',
                'created',
                'updated',
            )
        }),
    )


@admin.register(TVWallMountInstallationModel)
class TVWallMountInstallationAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TVWallMountInstallationResource

    list_display = (
        'order',
        'id',
        'helpTechnician',
        'takeDownTV',
        'comments',
        'created',
        'updated',
    )

    list_display_links = (
        'order',
        'id',
    )

    filter_horizontal = (
        'otherQuestions',
    )

    search_fields = (
        'order',
        'id',
        'title',
        'description',
        'price',
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
                'order',
                'id',
                'helpTechnician',
                'takeDownTV',
                'comments',
                'TVsize',
                'TVsurface',
                'TVWallMount',
                'TVHandleCords',
                'TVOtherInstalations',
                'otherQuestions',
                'created',
                'updated',
            )
        }),
    )
