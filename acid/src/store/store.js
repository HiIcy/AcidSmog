/* eslint-disable camelcase */
import Vue from 'vue'
// 全局状态管理
import Vuex from 'vuex'
import cookie from '../static/js/cookie'
import * as actions from './action'
import * as getters from './getters'
import mutations from './mutations'

Vue.use(Vuex)

const userInfo = {
  name: cookie.getCookie('name') || '',
  token: cookie.getCookie('token') || ''
}
const folder_list = {
  totalNum: '',
  folder_list: []

}
const state = {
  userInfo,
  folder_list
}
// 全局状态管理
export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
