"""AcidSmog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from AcidSmog import settings
from smog.views import UserViewset,UserFolderViewset, FolderContentViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('folders', UserFolderViewset, base_name='folders')
router.register('folders/gallery',FolderContentViewset, base_name='gallery')
# router.register('tags', TageViewset, base_name='tags')
router.register('user', UserViewset, base_name='user')

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('', TemplateView.as_view(template_name='index.html')),
	path('', include(router.urls)),
	path('upload/', include('smog.urls', namespace='smog')),
	path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	# drf 自带的token认证模式
	path(r'api-token-auth/', views.obtain_auth_token),
	# jwt认证
	path(r'login/', obtain_jwt_token)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
