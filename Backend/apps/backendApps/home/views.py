from django.views.generic import TemplateView
from apps.backendApps.home.models import HomeTitleModel, HomeContentModel

class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        context['title'] = HomeTitleModel.objects.all()
        
        context['content'] = HomeContentModel.objects.all()

        return context

