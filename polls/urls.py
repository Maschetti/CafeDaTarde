from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ct'
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('post/', views.post_view, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)