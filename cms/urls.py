from django.urls import path
from cms import views


urlpatterns = [
    path('keyword/', views.keyword_list, name='keyword_list'),  # 一覧
]
