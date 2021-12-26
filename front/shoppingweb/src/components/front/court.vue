<template>
  <div id="court">
    <el-row>
      <el-col :span="8" v-for="(good, index) in goods" :key="index">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="good.image|imageFliter" class="image">
          <div style="padding: 14px;">
            <span>{{good.name}}</span>
            <div class="bottom clearfix">
              <span>售价：{{good.price}}</span>
              <el-button type="text" class="button" @click="removeCourt(good)">移除购物车</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <div class="btn">
      <el-button type="primary" @click="buy">提交订单</el-button>
    </div>
  </div>
</template>
<script>


export default {
  name: 'Court',

  created() {
    this.initGoodsList()

  },
  data() {
    return {
      formLabelWidth: "120px",
      loading: null,
      goods: [],
    }
  },
  methods: {
    removeCourt(goods) {
      this.openLoading("移除中...")
      this.$axios.post("/user/rmFromCourt", { goodsId: goods._id })
        .then(res => {
          this.closeLoading()
          console.log(res)
          if (res.data.code == 200) {
            this.goods.splice(this.goods.indexOf(goods), 1);
          }
        }).catch(err => {
          this.closeLoading()
        })
    },
    buy() {
      this.openLoading("订单提交中...")
      var payValue = 0.0
      var goodsList = []
      this.goods.forEach(good => {
        payValue = payValue + good.sellPrice
        goodsList.unshift({
          id: good._id,
          number: 1
        })
      })
      this.$axios.post("/user/buyGoods", {
        payValue: payValue,
        goodsList: goodsList,
        cutoffValue: payValue
      }).then(res => {
        this.closeLoading()
        if (res.data.code == 200) {
          this.$message({
            message: "购买成功！",
            type: "success"
          })
          this.goods = []
        } else {
          this.$message({
            message: res.data.data.info,
            type: "warning"
          })
        }
      }).catch(err => {
        this.closeLoading()
      })
    },
    initGoodsList() {
      this.openLoading()
      this.$axios.get("/user/checkCourt")
        .then(res => {
          this.closeLoading()
          if (res.data.code == 200) {
            this.goods = res.data.data.data
          }
        }).catch(err => {
          this.closeLoading()
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

  }
}

</script>
<style scoped="">
#court {
  margin: 25px;
}

#court .btn {
  float: right;
  margin: 50px;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 50%;
  height: 256px;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

</style>
