from django.urls import path
from . import views

urlpatterns = [
    path('group-list/', views.GroupList.as_view(), name='group-list'),
    path('group-details/<int:group_id>/', views.group_detail, name='group-details'),
    path('join_group/<int:group_id>/', views.join_group, name='join_group'),
]