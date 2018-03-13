from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from mygame.models import GamePlay
from django.http import JsonResponse

class HomeView(TemplateView):
    template_name = 'home.html'


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    # 타이밍 로딩 문제로 reverse를 사용시 에러가 발생
    success_url = reverse_lazy('register_done')


class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'


def myGamePlay(request):
    user = request.user
    myDir = request.GET['dir']
    GamePlay.objects.create(usr=user, leftright=myDir)
    myCount = GamePlay.objects.filter(usr=user, leftright=myDir).count()
    result = { 'myDir':myDir, 'myCount':myCount }
    return JsonResponse(result)