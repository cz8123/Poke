from .models import *
from .serializers import *
from .filters import PokemonFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'pokemon':reverse('poke:pokemon-list', request=request, format=format),
#         'type':reverse('poke:type-list', request=request, format=format),
#         'ability':reverse('poke:ability-list', request=request, format=format),
#         'move':reverse('poke:ability-list', request=request, format=format),
#     })
class PokePage(PageNumberPagination):
    page_size = 50 # 默认每页显示的个数
    page_size_query_param = 'page_size' # 在url传入参数?page=1&page_size=30，可以动态改变每页显示的个数
    page_query_param = 'page' # url传入的页码参数?page=1
    max_page_size = 100 # 最多能显示多少页
class AbilityPage(PokePage):
    page_size = 20
class MovePage(PokePage):
    page_size = 200
class ItemPage(PokePage):
    page_size = 150
class PokemonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	pagination_class = PokePage
	queryset = Pokemon.objects.all()
	serializer_class = PokemonSerializer
	filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
	filter_class = PokemonFilter
	search_fields = ('name', '=num')
    # ordering_fields = ('num',)
class TypeViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	queryset = Type.objects.all()
	serializer_class = TypeSerializer
	filter_backends = (DjangoFilterBackend,filters.SearchFilter)
	search_fields = ('name',)
class AbilityViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	pagination_class = AbilityPage
	queryset = Ability.objects.all()
	serializer_class = AbilitySerializer
	filter_backends = (DjangoFilterBackend,filters.SearchFilter)
	search_fields = ('name',)
class MoveViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	pagination_class = MovePage
	queryset = Move.objects.all()
	serializer_class = MoveSerializer
	filter_backends = (DjangoFilterBackend,filters.SearchFilter)
	search_fields = ('name',)
class ItemViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	pagination_class = ItemPage
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	filter_backends = (DjangoFilterBackend,filters.SearchFilter)
	search_fields = ('name',)
class CategoryViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	pagination_class = PokePage
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
