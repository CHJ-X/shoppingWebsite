<template>
  <div id="register">
    <h1>注册</h1>
    <div class="info">
      <div>
        <el-input placeholder="请输入用户名" v-model="username"></el-input>
      </div>
      <div>
        <el-input placeholder="请输入密码" v-model="password" show-password></el-input>
      </div>
      <div>
        <el-input placeholder="请输入邮箱" v-model="mail" ></el-input>
      </div>
      <div>
        <el-input placeholder="请输入地址" v-model="address" ></el-input>
      </div>
    </div>
    <div class="btn">
      <el-button style="width:100%;height: 40px;margin-top: 10px;" @click="register" type="primary">注册</el-button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      password: '',
      mail: '',
      address: '',
      loading: null
    }
  },
  methods: {
    register() {
      if (!this.username) {
        this.$message({
          message: '请输入用户名',
          type: 'warning'
        });
        return
      } else if (!this.password) {
        this.$message({
          message: '请输入您的密码',
          type: 'warning'
        });
        return
      }
      this.openLoading("注册中...")
      this.$axios.post("/register", {
          username: this.username,
          password: this.password,
          mail: this.mail,
          address: this.address
        })
        .then(res => {
          this.closeLoading()
          console.log(res)
          if (res.data.code == 200) {
            this.$router.push("/")
          } else {
            this.$message.error(res.data.data.info)
          }
        })
        .catch(err => {
          this.closeLoading()
          console.log(err)
        })
    },
    openLoading(text = "加载...") {
      this.loading = this.$loading({
        lock: true,
        text: text,
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
    },
    closeLoading() {
      if (this.loading) {
        this.loading.close()
      }
    },
  }
}

</script>
<style scoped="">
#register {
  width: 80%;
  height: 100%;
  margin: 100px auto;
}

#register h1 {
  width: 200px;
  margin: 10px auto;
}

#register .info {
  width: 60%;
  margin: 0 auto;
}
#register .btn{
  width: 60%;
  margin: 0 auto;
}

#register .info input {
  margin-top: 20px;
}

</style>
