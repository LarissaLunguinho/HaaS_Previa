<template>
  <v-card>
    <v-card-title>
      <v-spacer></v-spacer>
      
      <v-text-field 
      v-model="search" 
      append-icon="mdi-magnify" 
      label="Buscar" 
      single-line 
      hide-details
      ></v-text-field>
    </v-card-title>

    <v-data-table
    :headers="headers" 
    :items="items" 
    :search="search" 
    class="table-header"
    >
      <template v-slot:[`item.bo_regra_cobranca`]="{item}">
        <v-chip :color="getColor(item.bo_regra_cobranca)" dark>
          {{ item.bo_regra_cobranca }}
        </v-chip>
      </template>
  
      <template #[`item.actions`]="{item}">
        <div>
          <v-icon small @click="visualizar(item.id)"> mdi-eye </v-icon>
          <v-icon small> mdi-delete </v-icon>
        </div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
  import Previa from '@/services/previa'

export default {
  name: 'HomeView',

  data() {
    return {
      search: '',
      headers: [
          {
            key: 'id',
            text: 'Código',
            value: 'id'
          },
          {
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
          },
          {
            text: "Ação",
            value: 'actions',
          }
      ],
      items: [],
    }
  },
  mounted() {
    Previa.listar().then(resposta => {
      this.items = resposta.data;
    })
  },

  methods: {
    getColor (bo_regra_cobranca) {
      if (bo_regra_cobranca == 'APLICADA') return 'orange'
      else return 'blue'
    },

    visualizar(id) {
      this.$router.push({ path: "/previa/" + id});
    },
  },
}
</script>

<style scoped>
.v-card{
  max-width: 90%;
  margin: auto;
}
</style>