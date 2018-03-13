from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from mygame.models import GamePlay
# Create your views here.

class GameListView(ListView):
    model = GamePlay
    paginate_by = 10

    def get_ordering(self):
        return "-created_date"

class GameDetailView(TemplateView):
    template_name = 'mygame/detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        count_lt = GamePlay.objects.filter(usr = user, leftright = "LT").count()
        count_rt = GamePlay.objects.filter(usr = user, leftright = "RT").count()
        last_login = GamePlay.objects.filter(usr = user).order_by("-created_date")[0]
        context = super().get_context_data(**kwargs)
        context['user_id'] = user
        context['count_lt'] = count_lt
        context['count_rt'] = count_rt
        context['last_login'] = last_login
        return context