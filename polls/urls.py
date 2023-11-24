from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ct'
urlpatterns = [
    path('home/', views.post_list_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('post/', views.post_view, name='post'),
    path('post_list/', views.post_list_view, name='post_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)