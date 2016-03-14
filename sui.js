import Vue from 'vue'
import VueRouter from 'vue-router'
import MainSUI from './MainSUI'

Vue.use(VueRouter)

Vue.config.debug = true

var router = new VueRouter()
import ListBlockRoute from './components_sui/ListBlockRoute'
import Show from './components_sui/Show'

router.map(
  {
    '/ListBlockRoute': { name: 'ListBlockRoute', component: ListBlockRoute },
    '/': {component: Show }
  }
)
router.start(MainSUI, '#app')
