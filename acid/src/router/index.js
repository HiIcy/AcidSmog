import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '../components/HelloWorld'
import login from '../views/login/login'
import mainbd from '../views/mainbd/allfolder'
import navi from '../components/navigation'
import sidebar from '../components/sidebar'
import register from '../views/login/register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      components: {
        default: mainbd,
        sidebar: sidebar,
        navi: navi
      }
    },
    {
      path: '/login',
      name: 'login',
      components: {
        default: login,
        // sidebar: sidebar,
        navi: navi
      }
    },
    {
      path: '/register',
      name: 'register',
      components: {
        default: register,
        // sidebar: sidebar,
        navi: navi
      }
    }
  ]
})
