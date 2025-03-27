from django.contrib import admin # type: ignore
from django.urls import path, include  # type: ignore
from django.conf import settings  # type: ignore # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib.auth import views as auth_views  # type: ignore
from home.views import grammarlevels, a1Topics  # type: ignore
from home.urls import get_static_urls # type: ignore

# Set DISTILL_URLS for django-distill to process all URLs from get_static_urls
DISTILL_URLS = get_static_urls

# Customize Django admin
admin.site.site_header = "Zasem Admin"
admin.site.site_title = "Zasem Admin Portal"
admin.site.index_title = "Welcome to Zasem Portal"

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel (not for static generation)
    path('', include('home.urls')),  # Include all URLs from home/urls.py
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('grammar-levels.html', grammarlevels, name='grammar-levels'),
    path('a1-topics.html', a1Topics, name='a1-topics'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)