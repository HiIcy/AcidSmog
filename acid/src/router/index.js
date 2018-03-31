import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '../components/HelloWorld'
import login from '../views/login/login'
import folders from '../views/mainbd/folders'
import navi from '../components/navigation'
import sidebar from '../components/sidebar'
import register from '../views/login/register'
import gallery from '../views/mainbd/gallery'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      // redirect: '',
      components: {
        default: folders,
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
    },
    {
      path: '/folders',
      name: 'folders',
      components: {
        default: folders,
        sidebar: sidebar,
        navi: navi
      }
    },
    {
      path: '/folder/:folder_id',
      name: 'gallery',
      components: {
        default: gallery,
        sidebar: sidebar,
        navi: navi
      }
    }
  ]
})
