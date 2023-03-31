<template>
    <div>
        <v-card>
            <v-card-title>
                Previa: {{ this.faturamento_id }}
            </v-card-title>
            <v-data-table
                :headers="title" 
                :items="valor"
                hide-default-footer
                class="tableone"
            >
                <template v-slot:[`item.bo_regra_cobranca`]="{ item }">
                    <v-chip :color="getColor(item.bo_regra_cobranca)" dark>
                        {{ item.bo_regra_cobranca }}
                    </v-chip>
                </template>
            </v-data-table>
        </v-card>
        <br>
        <v-card>
            <v-card-title>
                Itens Faturados
                <v-spacer></v-spacer>
                <v-text-field 
                v-model="search" 
                append-icon="mdi-magnify" 
                label="Buscar" 
                single-line hide-details
                ></v-text-field>
            </v-card-title>
            <v-data-table 
            :headers="headers" 
            :items="items" 
            :search="search"
            >
                <template #[`item.actions`]="{ item }">
                    <div>
                        <v-icon small @click="visualizar(item.id)"> mdi-eye </v-icon>
                    </div>
                </template>
            </v-data-table>
        </v-card>
    </div>
</template>

<script>
import Previa from '@/services/previa'

export default {
    name: 'ItemPreviaView',

    data() {
        return {
            search: '',
            faturamento_id: this.$route.params.faturamento_id,
            // Tabela Itens Faturados
            headers: [
                {
                    key: 'item_configuracao',
                    text: 'Descrição',
                    value: 'item_configuracao'
                },
                {
                    key: 'qt_contabilizado',
                    text: "Quantidade de objetos do grupo de IC's na infraestrutura",
                    value: 'qt_contabilizado'
                },
                {
                    key: 'nu_relevancia',
                    text: 'Relevância (Vlr)',
                    value: 'nu_relevancia'
                },
                {
                    key: 'vl_relevancia',
                    text: "Relevância (%)",
                    value: 'vl_relevancia'
                },
                {
                    key: 'nu_diversidade',
                    text: "Diversidade (Vlr)",
                    value: 'nu_diversidade'
                },
                {
                    key: 'vl_diversidade',
                    text: "Diversidade (%)",
                    value: 'vl_diversidade',
                },
                {
                    key: 'vl_item',
                    text: "Quantidade de US's estimada para consumo unitário",
                    value: 'vl_item',
                },
                {
                    key: 'vl_total_item',
                    text: "Quantidade de US's estimada para consumo por grupo de IC's",
                    value: 'vl_total_item',
                },
                {
                    key: 'vl_total_faturado',
                    text: "Valor mensal para a sustentação do item",
                    value: 'vl_total_faturado',
                },
                {
                    text: "Ação",
                    value: 'actions',
                }
            ],
            items: [],
            // Tabela Previa
            valor: [],
            title: [{
                key: 'id',
                text: 'Código',
                value: 'id'
            },
            {
                key: 'bo_regra_cobranca',
                text: 'Regra de Faturamento',
                value: 'bo_regra_cobranca'
            },
            {
                key: 'dt_mes_referencia',
                text: 'Dia/Mês de Referência',
                value: 'dt_mes_referencia'
            },
            {
                key: 'qt_contabilizado',
                text: "Qtd. IC's Contabilizado(s)",
                value: 'qt_contabilizado'
            },
            {
                key: 'vl_total_grupo',
                text: "Vlr. Total em US's",
                value: 'vl_total_grupo'
            },
            {
                key: 'vl_total_mensal',
                text: "Vlr. Total Mensal",
                value: 'vl_total_mensal',
            },
            {
                key: 'dt_cadastro',
                text: "Dt. Processada",
                value: 'dt_cadastro',
            }
            ]
        }
    },
    mounted() {
        Previa.listaritem(this.faturamento_id).then(resposta => {
            this.items = resposta.data;
        }),
        Previa.listarid(this.faturamento_id).then(response => {
            this.valor = response.data;
        })
    },
    methods: {
        getColor(bo_regra_cobranca) {
            if (bo_regra_cobranca == 'APLICADA') return 'orange'
            else return 'blue'
        },
        visualizar(id) {
            this.$router.push({ path: '/previa/' + this.faturamento_id + '/conteudo/' + id });
        },
    },
}
</script>

<style scoped>
.tableone{
    width:90%;
    padding-bottom: 7vh;
    margin: auto;
}
.v-card {
    max-width: 90%;
    margin: auto;
}
</style>