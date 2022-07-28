from django.urls import path
from . import views

urlpatterns = [
    # path('blog/', views.post_list_view, name='post_list'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('', views.home_page, name='home_page'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),
    path('aboutus/', views.about_us, name='about_us'),
]
