from rest_framework import serializers
from .models import *

class FaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = ['id', 'bo_regra_cobranca', 'dt_mes_referencia',
                  'qt_contabilizado', 'vl_total_grupo', 'vl_total_mensal', 'dt_cadastro', 'bo_diario']

class FaturamentoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaturamentoItem
        fields = '__all__'

class ItemConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaturamentoItemConteudo
        fields = ['id','js_contabilizado','js_nao_contabilizado','js_condicional','js_diversidade','faturamento_item']
