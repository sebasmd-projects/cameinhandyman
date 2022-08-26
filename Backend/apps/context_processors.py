from django.conf import settings

def custom_processors(request):
    ctx = {}
    
    # URL Base
    ctx['url_base'] = settings.BASE_URL
    
    
    return ctx