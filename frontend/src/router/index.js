import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/previa/:faturamento_id',
    name: 'ItemPreviaView',
    component: () => import('../views/ItemPreviaView.vue')
  },
  {
    path: '/previa/:faturamento_id/conteudo/:id',
    name: 'ItemConteudoView',
    component: () => import('../views/ItemConteudoView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
