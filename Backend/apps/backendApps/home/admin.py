from django.contrib import admin
from apps.backendApps.home.models import HomeTitleModel, HomeContentModel

@admin.register(HomeTitleModel)
class HomeTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(HomeContentModel)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('short_name',)