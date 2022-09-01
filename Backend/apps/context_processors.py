from django.conf import settings

def custom_processors(request):
    ctx = {}
    ctx['url_base'] = settings.BASE_URL
    return ctx