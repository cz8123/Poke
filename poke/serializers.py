from rest_framework import serializers
from .models import *

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = "__all__"

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        # fields = ['url', 'name', 'color']
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cate
        fields = "__all__"
class MoveRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveRange
        fields = "__all__"
class MoveSerializer(serializers.ModelSerializer):
    types = TypeSerializer()
    cate = CateSerializer()
    move_range = MoveRangeSerializer()
    class Meta:
        model = Move
        fields = "__all__"
class PokemonSerializer(serializers.ModelSerializer):
    # 覆盖外键字段, 嵌套显示
    type1 = TypeSerializer()
    type2 = TypeSerializer()
    ability1 = AbilitySerializer()
    ability2 = AbilitySerializer()
    ability3 = AbilitySerializer()
    class Meta:
        model = Pokemon
        fields = "__all__"
class PokemonSerializer1(serializers.ModelSerializer):
    # 覆盖外键字段, 嵌套显示
    type1 = TypeSerializer()
    type2 = TypeSerializer()
    class Meta:
        model = Pokemon
        fields = ['id', 'num', 'name', 'name1', 'name_en', 'pic', 'type1', 'type2']
class CategorySerializer(serializers.ModelSerializer):
    # cate_poke对应外键中设置的related_name，注意使用StringRelatedField只返回字符串
    # cate_poke = serializers.HyperlinkedRelatedField(many=True, view_name='pokemon-detail', read_only=True)
    # cate_poke = serializers.StringRelatedField(many=True)
    cate_poke = PokemonSerializer1(many=True)
    class Meta:
        model = Category
        fields = "__all__"

