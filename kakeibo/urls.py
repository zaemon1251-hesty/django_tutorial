from django.urls import path

from . import views

app_name = 'kakeibo'

from django.conf.urls import handler500

# 自作の 500 エラーハンドラー。
handler500 = views.my_error_handler

urlpatterns = [
    path('kakeibo_list/', views.KakeiboListView.as_view(), name='kakeibo_list'),
    path('kakeibo_create/', views.KakeiboCreateView.as_view(), name='kakeibo_create'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.KakeiboUpdateView.as_view(), name='kakeibo_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.KakeiboDeleteView.as_view(), name='kakeibo_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
    path('circle/',views.show_circle_graph,name='kakeibo_circle')
    ]

