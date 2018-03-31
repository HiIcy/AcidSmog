<template>
  <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm">
    <el-form-item label="用户名" prop="username">
      <el-input type="text" v-model="ruleForm2.username"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="pass">
      <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm2')">提交</el-button>
      <el-button @click="resetForm('ruleForm2')">重置</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
import cookie from '../../static/js/cookie'
import { login } from '../../api/api'
export default {
  name: 'login',
  data () {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('用户名不能为空'))
      }
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleForm2.checkPass !== '') {
          this.$refs.ruleForm2.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm2.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      userNameError: '',
      passwordError: '',
      error: false,
      ruleForm2: {
        pass: '',
        checkPass: '',
        username: ''
      },
      rules2: {
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
        username: [
          { validator: checkName, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    login () {
      var _this = this
      login({
        username: this.ruleForm2.username,
        password: this.ruleForm2.pass
      }).then((response) => {
        console.log('response是什么', response)
        cookie.setCookie('name', this.ruleForm2.username, 7)
        cookie.setCookie('token', response.data.token, 7)
        // vuex 分发action
        _this.$store.dispatch('setInfo')
        // 路由转移
        this.$router.push({name: 'folders'})
      }).catch(function (error) {
        if ('non_field_errors' in error) {
          _this.error = error.non_field_errors[0]
        }
        if ('username' in error) {
          _this.userNameError = error.username[0]
        }
        if ('password' in error) {
          _this.passwordError = error.password[0]
        }
      })
    },
    submitForm (formName) {
      // refs 获取ref属性的值
      this.login()
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  },
  beforeRouteLeave (to, from, next) {
    this.$store.dispatch('setFolder')
    next()
  },
  created () {
    cookie.delCooike('name')
    cookie.delCooike('token')
  }
}
</script>

<style scoped>

</style>
