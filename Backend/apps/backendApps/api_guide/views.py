from django.views.generic import TemplateView
from apps.backendApps.api_guide.models import ApiGuideTitleModel, ApiGuideContentModel

class ApiGuideView(TemplateView):
    template_name = 'api_guide/api_guide.html'
    
    def get_context_data(self, **kwargs):
        context = super(ApiGuideView, self).get_context_data(**kwargs)
        
        context['title'] = ApiGuideTitleModel.objects.all()
        
        context['content'] = ApiGuideContentModel.objects.all()

        return context