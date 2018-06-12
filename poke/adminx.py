import xadmin
from .models import *

class PokemonAdmin():
    list_display = ['num', 'name', 'name1', 'name_en', 'hp', 'atk', 'defen', 'satk', 'sdef', 'sp', 'type1', 'type2', 'ability1', 'ability2', 'icon']
    search_fields = ['num', 'name']
    list_filter = ['num', 'name', 'type1', 'type2']
class TypeAdmin():
    list_display = ['name', 'color', 'pgl_typeid']
    search_fields = ['num']

class AbilityAdmin():
    list_display = ['name', 'detail']
    search_fields = ['name']
class MoveAdmin():
    list_display = ['name', 'detail']
    search_fields = ['name']
class ItemAdmin():
    list_display = ['name', 'detail']
    search_fields = ['name']

xadmin.site.register(Pokemon, PokemonAdmin)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Ability, AbilityAdmin)
xadmin.site.register(Move, MoveAdmin)
xadmin.site.register(Item, ItemAdmin)