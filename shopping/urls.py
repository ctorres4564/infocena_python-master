from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from siteweb import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
    path('', include('siteweb.urls')),
    path('produtos/', views.produtos_publicos, name='produtos_publicos'),
    path('contato/', views.contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='siteweb/login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
