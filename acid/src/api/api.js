import axios from 'axios'
let host = ''

export const login = params => {
  return axios.post(`/user/login`, params)
}

export const register = params => {
  return axios.post(`/user/`, params)
}
// 全文件夹第一个主界面
export const getFolderItem = params => {
  return axios.get(`${host}/FolderItem/`, params)
}
