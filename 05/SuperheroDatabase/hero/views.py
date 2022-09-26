from django.views.generic import TemplateView
#from markdown import markdown

from .models import Hero


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'note': Hero.objects.get(pk=kwargs['pk'])
        }