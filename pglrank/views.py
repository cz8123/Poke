import json, mysql.connector, requests, time
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from poke.serializers import PokemonSerializer, TypeSerializer
from poke.models import Pokemon, Type

database = {'db':'pgl','user':'root', 'passwd':'666666','host':'localhost', 'charset':'utf8'}

def allpokelist():
    conn = mysql.connector.connect(**database)
    cur = conn.cursor()
    cur.execute('select value from pgl_getSeasonPokemon where name=%s',('pglPokemon',))
    a = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return a.decode('utf-8')

def ranklist(s, n, rank):
    conn = mysql.connector.connect(**database)
    cur = conn.cursor()
    cur.execute('select value from pgl_getseasonpokemon where name=%s', ('ranking%s-%s'%(s, n), ))
    rank_list = json.loads(cur.fetchall()[0][0])
    cur.close()
    conn.close()
    return rank_list[:rank]

def updateDate(s):
    conn = mysql.connector.connect(**database)
    cur = conn.cursor()
    cur.execute('select value from pgl_getseasonpokemon where name=%s', ('updateDate%s'%s, ))
    updateDate = json.loads(cur.fetchall()[0][0])
    cur.close()
    conn.close()
    return updateDate

def getpokemonDetail(s, n, id_):
    conn = mysql.connector.connect(**database)
    cur = conn.cursor()
    cur.execute('select value from pgl_getseasonpokemonD_%s_%s where name=%%s'%(s, n),(id_, ))
    r = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return r.decode('utf-8')

@csrf_exempt
def pgl(request, s=310):
    context = {}
    if request.method == 'POST':
        poke_id = request.POST.get('poke_id')
        type_id = request.POST.get('type_id')
        season_id = request.POST.get('season_id')
        r= json.loads(getpokemonDetail(season_id, type_id, poke_id))
        pokemonId = r['rankingPokemonInfo']['pokemonId']
        pokemonName = r['rankingPokemonInfo']['name']
        type1 = Type.objects.get(pgl_typeid=r['rankingPokemonInfo']['typeId1'])
        serializer2 = TypeSerializer(type1)
        context['type1'] = serializer2.data
        if r['rankingPokemonInfo']['typeId2'] and (0<r['rankingPokemonInfo']['typeId2']<19):
            type2 = Type.objects.get(pgl_typeid=r['rankingPokemonInfo']['typeId2'])
            serializer3 = TypeSerializer(type2)
            context['type2'] = serializer3.data
        else:
            context['type2'] = None
        try:
            pokemodal = Pokemon.objects.get(pic=pokemonId)
        except Pokemon.DoesNotExist:
            pokemodal = Pokemon.objects.filter(name=pokemonName)[0]
        serializer1 = PokemonSerializer(pokemodal)
        allpoke = json.loads(allpokelist())['pokemonInfo']
        context['trend'] = r['rankingPokemonTrend']
        context['poke'] = r['rankingPokemonInfo']
        context['pokemodal'] = serializer1.data
        context['allpoke'] = allpoke
        return HttpResponse(json.dumps(context), content_type='application/json')
    for n in ['1', '2', '5', '6']:
        context['s%s'%n] = ranklist(s, n, 10)
    context['updateDate'] = updateDate(s)
    return HttpResponse(json.dumps(context), content_type='application/json')
    
