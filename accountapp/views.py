from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

# Create your views here.

has_ownership = [account_ownership_required, login_required]



class AccountCreateView(CreateView):
    model = User # 장고가 User 모델을 기본으로 제공, 이것을 상속받아 새로운 필드 추가 가능
    form_class = UserCreationForm # 회원가입을 할 때 사용할 form
    success_url = reverse_lazy('accountapp:login') # 계정을 만들기에 성공했을 때, 어느 경로로 다시 연결할 것인지
    # 함수형 뷰에서는 reverse만을, class형 뷰에서는 reverse_lazy만 사용할 수 있다
    template_name = 'accountapp/create.html' # 회원가입시에 렌더링해줄 html


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/update.html'




@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

