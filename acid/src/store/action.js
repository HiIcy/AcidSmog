import * as types from './mutation_types'
// Action 提交的是 mutation，而不是直接变更状态。
// Action 可以包含任意异步操作。
function makeAction (type) {
  // 参数解构 提交mutation
  return ({ commit }, ...args) => commit(type, ...args)
}

export const setInfo = makeAction(types.SET_INFO)
export const setFolder = makeAction(types.SET_FOLDER)
