from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.




@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})



class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated: # 로그인 돼있으면 해당 유저가 프로젝트를 구독하고 있는지를 subscription에 담아 템플릿으로 넘겨줌
            subscription = Subscription.objects.filter(user=user, project=project)
        else: # subscription을 return 해줘야하기 때문에 None으로 초기화
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())

        # 최종적으로 템플릿에 context_data안에 구독 정보를 우리가 찾은 'subscription'으로 대체
        # 이런식으로 구독 정보가 있는지 없는지 확인
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25

