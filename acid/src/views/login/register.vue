<template>
  <el-form :model="ruleForm1" status-icon :rules="rules2" ref="ruleForm1" label-width="100px" class="demo-ruleForm">
      <el-form-item label="邮箱" prop="email">
      <el-input type="email" v-model="ruleForm1.email"></el-input>
    </el-form-item>
    <el-form-item label="用户名" prop="username">
      <el-input type="text" v-model="ruleForm1.username"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="pass">
      <el-input type="password" v-model="ruleForm1.pass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item label="确认密码" prop="checkPass">
      <el-input type="password" v-model="ruleForm1.checkPass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm1')">注册</el-button>
      <el-button @click="resetForm('ruleForm1')">重置</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
import cookie from '../../static/js/cookie'
import { register } from '../../api/api'
export default {
  name: 'register',
  data () {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('用户名不能为空'))
      }
    }
    var checkEmail = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('邮箱不能为空'))
      }
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleForm1.checkPass !== '') {
          this.$refs.ruleForm1.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm1.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      userNameError: '',
      passwordError: '',
      error: false,
      ruleForm1: {
        email: '',
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
        ],
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    register () {
      var _this = this
      register({
        email: this.ruleForm1.email,
        username: this.ruleForm1.username,
        password: this.ruleForm1.pass
      }).then(response => {
        console.log(response)
        cookie.setCookie('name', response.data.name, 5)
        cookie.setCookie('token', response.data.token, 5)
        // 存储在store，更新store数据
        _this.$store.dispatch('setInfo')
        _this.$router.push({name: 'login'})
      }).catch(function (error) {
        console.log(error)
      })
    },
    submitForm (formName) {
      console.log(',,,,,i')
      // refs 获取ref属性的值
      console.log('sfsf')
      console.log('sbumit')
      this.register()
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style scoped>

</style>
