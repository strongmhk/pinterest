from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import  AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"  # "127.0.0.1:8000/account/hello_world"을 호출할 필요없이 "accountapp:hello_world"로 치환해줌


urlpatterns = [

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]
