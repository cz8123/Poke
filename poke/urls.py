from django.conf.urls import url
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'poke'
pokemon_list = PokemonViewSet.as_view({'get':'list'}) # 'post':'create'
pokemon_detail = PokemonViewSet.as_view({'get': 'retrieve'}) # 'put': 'update', 'patch':'partial_update','delete':'destroy'
type_list = TypeViewSet.as_view({'get':'list'})
type_detail = TypeViewSet.as_view({'get': 'retrieve'})
ability_list = AbilityViewSet.as_view({'get':'list'})
ability_detail = AbilityViewSet.as_view({'get': 'retrieve'})

urlpatterns = format_suffix_patterns([
    path('', api_root),
	path('pokemon/', pokemon_list, name='pokemon-list'),
	path('pokemon/<int:pk>/', pokemon_detail, name='pokemon-detail'),
    path('type/', type_list, name='type-list'),
	path('type/<int:pk>/', type_detail, name='type-detail'),
    path('ability/', ability_list, name='ability-list'),
	path('ability/<int:pk>/', ability_detail, name='ability-detail'),
])
