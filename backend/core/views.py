from rest_framework.views import APIView
from rest_framework.response import Response

from .helpness import *
from .models import *
from .serializers import FaturamentoSerializer, FaturamentoItemSerializer, ItemConteudoSerializer


# 01.PRIMEIRA TELA
class FaturamentoView(APIView):
    def get(self, request):

        faturamentos = Faturamento.objects.filter(st_situacao='previa').order_by('-id')
        serializer = FaturamentoSerializer(faturamentos, many=True)

        for previa in serializer.data:
            if previa['bo_diario'] == False:
                previa['dt_mes_referencia'] = dmreferenciafalse(
                    previa['dt_mes_referencia'])
            else:
                previa['dt_mes_referencia'] = dmreferenciatrue(
                    previa['dt_mes_referencia'])

            previa['dt_cadastro'] = dataProcessada(previa['dt_cadastro'])
            previa['vl_total_grupo'] = valorus(previa['vl_total_grupo'])
            previa['vl_total_mensal'] = valormes(previa['vl_total_mensal'])
            previa['bo_regra_cobranca'] = regra_cobranca(previa['bo_regra_cobranca'])
        
        return Response(serializer.data)

# 02.SEGUNDA TELA
class FaturamentoItemView(APIView):
    def get(self, request, pk):
        faturamento_items = FaturamentoItem.objects.filter(
            faturamento=pk).order_by('item_configuracao')
        serializer = FaturamentoItemSerializer(faturamento_items, many=True)

        for item_faturamento in serializer.data:
            item_config = ItemConfiguracao.objects.filter(
                id=item_faturamento['item_configuracao'])
            
            for item in item_config:
                item_faturamento['item_configuracao'] = item.no_item

        return Response(serializer.data)

# 03.TERCEIRA TELA
class ItemConteudoView(APIView):
    def get(self, request, id):
        item_config = FaturamentoItemConteudo.objects.filter(
            faturamento_item=id)
        serializer = ItemConteudoSerializer(item_config, many=True)

        items = []
        headers = []

        # acessar o serializer, acessar os dados e modifica-los
        for valor in serializer.data:
            items.append(valor['js_contabilizado'])

            listaTitulo=[]
            for titulo in valor['js_contabilizado']:
                for index in titulo:
                    listaTitulo.append({ "text":index, "value":index })
                
                headers.append(listaTitulo)
                break

            items.append(valor['js_nao_contabilizado'])
            listaTitulo=[]
            for titulo in valor['js_nao_contabilizado']:
                for index in titulo:
                    listaTitulo.append({ "text":index, "value":index })
                
                headers.append(listaTitulo)
                break

            items.append(valor['js_condicional'])
            listaTitulo=[]
            for titulo in valor['js_condicional']:
                for index in titulo:
                    listaTitulo.append({ "text":index, "value":index })
                
                headers.append(listaTitulo)
                break

            items.append(valor['js_diversidade'])
            listaTitulo=[]
            for titulo in valor['js_diversidade']:
                for index in titulo:
                    listaTitulo.append({ "text":index, "value":index })
                
                headers.append(listaTitulo)
                break

        return Response({
            "items":items,
            "headers":headers
        })


# 02.01 PRIMEIRA TABELA DA SEGUNDA TELA
class FaturamentoIdView(APIView):
    def get(self, request, pk):
        faturamento_id = Faturamento.objects.filter(
            st_situacao='previa', id=pk).order_by('-id')
        serializer = FaturamentoSerializer(faturamento_id, many=True)

        for previa in serializer.data:
            if previa['bo_diario'] == False:
                previa['dt_mes_referencia'] = dmreferenciafalse(
                    previa['dt_mes_referencia'])
            else:
                previa['dt_mes_referencia'] = dmreferenciatrue(
                    previa['dt_mes_referencia'])

            previa['dt_cadastro'] = dataProcessada(previa['dt_cadastro'])
            previa['vl_total_grupo'] = valorus(previa['vl_total_grupo'])
            previa['vl_total_mensal'] = valormes(previa['vl_total_mensal'])
            previa['bo_regra_cobranca'] = regra_cobranca(
                previa['bo_regra_cobranca'])
            
        return Response(serializer.data)            


# 03.02 SEGUNDA TABELA DA TERCEIRA TELA
class ItemConfigIdView(APIView):
    def get(self, request, pk):
        item_faturamento = FaturamentoItem.objects.filter(
            id=pk)
        serializer = FaturamentoItemSerializer(item_faturamento, many=True)

        for item_faturamento in serializer.data:
            item_config = ItemConfiguracao.objects.filter(
                id=item_faturamento['item_configuracao'])            
            for item in item_config:
                item_faturamento['item_configuracao'] = item.no_item
        
        return Response(serializer.data)