from django.urls import path
from . import views

urlpatterns = [
    #测试
    path('test_function/', views.test_function),

    #企微
    path('query_wecom_account/', views.query_wecom_account),
    path('del_wecom_account/', views.del_wecom_account),

    #钉钉
    path('query_dd_account/', views.query_dd_account),
    path('del_dd_account/', views.del_dd_account)
]