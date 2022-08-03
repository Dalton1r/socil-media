from django.urls import path
from accounting import views


urlpatterns = [
    path('detail/<int:pk>/', views.accountingdetail, name='accounting-detail'),
    path('list/', views.accountinglist, name='accounting-list'),
    path('create/', views.accountingcreate, name='accounting-create'),
    path('update/<int:pk>/', views.accountingupdate, name='accounting-update'),
    path('delete/<int:pk>/', views.accountingdelete, name='accounting-delete'),
    path('', views.apiaccountingoverview, name='overview')
]
