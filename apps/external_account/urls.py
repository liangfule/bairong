from django.urls import path
from . import views

urlpatterns = [
    path('query_wecom_account/', views.query_wecom_account),
    path('del_wecom_account/', views.del_wecom_account)
]