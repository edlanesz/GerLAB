from django.urls import path
from autenticacao import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import deslogar
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('auth/', views.login_view, name='autenticacao'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='authentication.html'), name='login'),
    path('deslogar/', deslogar, name='deslogar'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Adicione a URL de mídia
