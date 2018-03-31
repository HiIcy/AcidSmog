import cookie from '../static/js/cookie'
import * as types from './mutation_types'
import { getFolderItem } from '../api/api'
import Vue from 'vue'
import axios from 'axios'
// 更改 Vuex 的 store 中的状态的唯一方法是提交 mutation
Vue.prototype.$http = axios
export default {

  [types.SET_INFO] (state) {
    state.userInfo = {
      name: cookie.getCookie('name'),
      token: cookie.getCookie('token')
    }
  },

  [types.SET_FOLDER] (state) {
    if (cookie.getCookie('name') != null) {
      getFolderItem({'user-id':cookie.getCookie('name')}).then((response) => {
        let totalNum = 0;
        console.log('folder_list',response)
        response.data.forEach(function(value,index) {
          totalNum += 1;
        });
        state.folder_list.totalNum = totalNum;
        state.folder_list.folder_list = response.data
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
