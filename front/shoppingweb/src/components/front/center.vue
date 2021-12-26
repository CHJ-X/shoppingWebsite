<template>
  <div id="center">
    <div class="search">
      <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
        
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </div>
    <div class="container">
      <div class="item" @click="goodsDetail(goods.id)" v-for="(goods,index) in tableGoodsData" :key="index">
        <img :src="goods.image | imageFliter" alt="">
        <div class="price">
          <span class="price">{{goods.price}}$</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Center',
  created() {
  },
  data() {
    return {
      loading: null,
      input3: '',
      tableGoodsData: []
    }
  },
  methods: {
    
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
    
    goodsDetail(_id) {
      console.log(_id)
      this.$router.push({
        path: "/goods/detail",
        name: "GoodsDetail",
        params: {
          "_id": _id
        }
      })

    }
  }
}

</script>
<style scoped>
#center .tag {
  height: 50px;
  cursor: pointer;
}

#center .search {
  margin: 10px;
}

#center .tag:hover {
  color: darkred;
}

.el-select .el-input {
  width: 130px;
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
}

#center .container {
  width: 100%;
  margin: 10px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

#center .container .item {
  width: 15%;
  height: 240px;
  cursor: pointer;
  margin: 5px;
}

#center .container .item img {
  width: 100%;
  height: 123px;
  border-radius: 5px;
  margin: 2px;
}

#center .container .item .intro {
  font-size: 1rem;
  color: #333;
  line-height: 1.4rem;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  margin-top: 10px;
}

#center .container .item .price {
  margin: 2px;
  margin-top: 20px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

</style>
