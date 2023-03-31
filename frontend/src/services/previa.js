import { http } from './config'

export default {

    // PRIMEIRA TELA
    listar:() => {
        return http.get('previa')
    },

    // SEGUNDA TELA
    listaritem:(faturamento_id) => {
        return http.get('/previa/' + faturamento_id + '/')
    },

    // PEGA ID DA PREVIA
    listarid:(id) => {
        return http.get('/item/' + id + '/')
    },

    // PEGA O ID DO IC
    listarItemConfig:(itemconfig) => {
        return http.get('/itemconfig/' + itemconfig + '/')
    },

    // TERCEIRA TELA
    listaritemconteudo:(id) => {
        return http.get('/previa/conteudo/' + id )
    }
    
}