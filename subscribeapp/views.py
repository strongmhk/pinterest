from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

# 로그인을 해야지 구독을 할 수 있도록 하기, 숨길건 없으므로 get 방식
@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    # redirect 로직
    def get_redirect_url(self, *args, **kwargs):
        # detail 안에서 구독 버튼을 누를 수 있도록 하기 위해 되돌아갈 곳은 projectapp 에서 detail 페이지
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    # project_pk를 get 방식으로 받아서 해당 pk를 가지고 있는 project의 상세 화면으로 이동

    # 구독 로직
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) # 존재하지 않는 프로젝트면 404 예외처리
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists(): # 구독 정보 있으면 -> 구독 취소
            subscription.delete()
        else: # 구독 정보 없으면 -> 구독
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project') # 사용자가 구독한 프로젝트들 list로 가져오기
        article_list = Article.objects.filter(project__in=projects) # project에 해당하는 article 전부 가져오기
        return article_list