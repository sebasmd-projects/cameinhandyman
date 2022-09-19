from django.contrib import admin

from apps.backendApps.api_guide.models import ApiGuideTitleModel, ApiGuideContentModel

@admin.register(ApiGuideTitleModel)
class ApiGuideTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(ApiGuideContentModel)
class ApiGuideContentAdmin(admin.ModelAdmin):
    list_display = ('short_name',)