import django_filters
from .models import Pokemon

class PokemonFilter(django_filters.rest_framework.FilterSet):
    #name是要过滤的字段，lookup是执行的行为’
    atk_min = django_filters.NumberFilter(name='atk', lookup_expr='gte')
    atk_max = django_filters.NumberFilter(name='atk', lookup_expr='lte')
    class Meta:
        model = Pokemon
        fields = ['atk_min', 'atk_max']