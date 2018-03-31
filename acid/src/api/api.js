import axios from 'axios'

export const login = params => {
  return axios.post(`/login/`, params)
}

export const register = params => {
  return axios.post(`/user/`, params)
}
// 全文件夹第一个主界面
export const getFolderItem = paramss => {
  return axios.get(`/folders/`, { params: paramss })
}
export const getFolderContent = paramss => {
  return axios.get(`/folders/gallery/`, { params: paramss })
}
