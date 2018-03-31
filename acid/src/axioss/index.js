import Vue from 'vue'
import axios from 'axios'

// 全局状态控制引入
import store from '../store/store'

import * as types from '../store/mutation_types'

import router from '../router/'

// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (store.state.userInfo.token) {
      // config.headers['Content-Type'] = 'application/x-www-form-urlencoded'
      /// 判断是否存在token，如果存在的话，则每个http header都加上token 换成了jwt验证
      config.headers.Authorization = `JWT ${store.getters.userInfo.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  })
axios.interceptors.response.use(
  undefined,
  function (error) {
    let res = error.response
    switch (res.status) {
      case 401:
        // store.commit(types.logout)
        //     router.replace({
        //       path: '/login',
        //       query: {redirect: router.currentRoute.fullPath}
        //     })
        console.log('未登录')
        break
      case 403:
        console.log('您没有该操作权限')
        break

      // alert('您没有该操作权限');
      case 500:
        console.log('服务器错误')
        break
    }
    return Promise.reject(error.response.data)
  }
)
