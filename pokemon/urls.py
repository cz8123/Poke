"""pokemon URL Configuration

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
from django.contrib import admin
import xadmin # pip install git+https://github.com/sshwsfc/xadmin.git@django2
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls # pip install coreapi
from poke import views
from django.views.generic.base import TemplateView

router = DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)
router.register(r'type', views.TypeViewSet)
router.register(r'ability', views.AbilityViewSet)
router.register(r'move', views.MoveViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
    path('docs', include_docs_urls(title='pokemon rest')),
    path('', include('pglrank.urls', namespace='pglrank')),
    path('index/', TemplateView.as_view(template_name='index.html')),
    # path('', include('poke.urls', namespace='poke')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
