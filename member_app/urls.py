from django.urls import path
from . import views
 

# 요청 url에 따른 view에 등록된 함수 호출
urlpatterns = [
  path('', views.home, name='home'),  # home 뷰를 views에서 참조
  path('members/', views.members, name='members'),
  path('members/details/<int:id>', views.details, name='details'),
  path('test/', views.testing , name='testing'),
]