<template>
  <div id="main-index">
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex2" :router="true" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item index="/center">商城中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的菜单</template>
            <el-menu-item index="/personal">个人信息</el-menu-item>
            <el-menu-item index="/court">购物车</el-menu-item>
            <el-menu-item index="/receipt">我的订单</el-menu-item>
          </el-submenu>
          <el-menu-item index="4" :disabled="loginStatus">
            <span @click="login">登录</span>
          </el-menu-item>
          <el-menu-item index="5" :disabled="!loginStatus">
            <span @click="quit">退出</span>
          </el-menu-item>
        </el-menu>
      </el-header>
      <router-view />
    </el-container>
  </div>
</template>
<script>
export default {
  name: 'MainIndex',
  created() {
    // 初始化页面加载需要加载商品信息
    // 判断用户是否登录
    this.isLogin()
    // 当页面是从注册页面或者是登录页面跳转过来的需要更新信息
  },
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      loginStatus: false,
      loading: null,
    }
  },
  methods: {
    isLogin() {
      this.$axios.get("/login")
        .then(res => {
          if (res.data.code == 200) {
            this.loginStatus = true
          } else {

          }
        })
        .catch(err => {

        })
    },
    openLoading(text = "数据加载...") {
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
    quit() {
      if (this.loginStatus) {
        this.openLoading("退出中...")
        this.$axios.post("/quit",{
          type:"xx"
        })
          .then(res => {
            console.log(res)
            this.closeLoading()
              this.$router.push("/login")
          }).catch(err => {
            console.log(err)
            this.closeLoading()
          })
      }
    },
    login() {
      if (!this.loginStatus) {

        this.$router.push("/login")
      }
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },

  }
}

</script>
<style>
#main-index section header {
  margin: 0;
  padding: 0;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body>.el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

</style>
