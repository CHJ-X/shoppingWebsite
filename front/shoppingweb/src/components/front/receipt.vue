<template>
  <div id="receipt">
  	<el-table :data="receipts" style="width: 100%">
        
        <el-table-column label="订单号" prop="orderNum">
        </el-table-column>
        <el-table-column label="实际支付" prop="payValue">
        </el-table-column>
        <el-table-column label="商品" prop="goodsList">
        </el-table-column>
      </el-table>
  	<el-empty v-show="receipts.length==0" description="没有任何订单"></el-empty>
    {{receipts}}
  </div>
</template>
<script>
export default {
  name: 'Receipt',
  created() {
    this.getAllReceipt()
  },
  data() {
    return {
      loading: null,
      receipts: []
    }
  },
  methods: {
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
    getAllReceipt() {
      this.openLoading()
      this.$axios.get("/user/checkReceipt")
        .then(res => {
          this.closeLoading()
          if (res.data.code == 200) {
            this.receipts = res.data.data.data
          }
        })
        .catch(err => {
          this.closeLoading()
        })
    }
  }
}

</script>
<style>
</style>
