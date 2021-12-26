<template>
  <div id="goods-manage">
    <div class="left">
      <!-- 商品展示开始 -->
      <el-table :data="tableData" style="width: 100%">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="商品名称">
                <span>{{ props.row.name }}</span>
              </el-form-item>
              <el-form-item label="商品 ID">
                <span>{{ props.row._id }}</span>
              </el-form-item>
              <el-form-item label="售价">
                <span>{{ props.row.price }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="商品 ID" prop="_id">
        </el-table-column>
        <el-table-column label="商品名称" prop="name">
        </el-table-column>
      </el-table>
      <!-- 商品展示结束 -->
      <!-- 分页开始 -->
      <el-pagination layout="prev, pager, next" @current-change="currentPageChange" :page-size="nums" :total="goodsTotal">
      </el-pagination>
      <span>一共{{goodsTotal}}条</span>
      <!-- 分页结束 -->
    </div>
    <el-divider direction="vertical"></el-divider>
    <div class="right">
      <!-- 添加商品表单开始 -->
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="商品名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-upload action="https://jsonplaceholder.typicode.com/posts/" list-type="picture-card" :before-upload="handleBeforeUpload" :on-remove="handleRemove">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-form-item label="售价">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="addGoods">立即创建</el-button>
        </el-form-item>
      </el-form>
      <!-- 添加商品表单结束 -->
    </div>
  </div>
</template>
<script>
export default {
  name: 'GoodsManage',
  created() {
    this.getAllTags()
    this.getAllAddress()
    this.getGoodsTotal()
    this.getPageData(1)

  },
  data() {
    return {
      nums: 15,
      goodsTotal: 0,
      faceImage: null,
      form: {
        price: null,
        name: '',
      },
      tableData: []
    }
  },
  methods: {
    // 获取商品总数
    getGoodsTotal() {
      this.$axios.get("/admin/checkGoods")
        .then(res => {
          if (res.data.code == 200) {
            this.goodsTotal = res.data.data.nums
          }
        })
        .catch(err => {

        })
    },
    // 获取某页的数据 @pageNum 第几页
    getPageData(pageNum) {
      this.openLoading("数据加载中...")
      this.$axios.post("/admin/checkGoods", {
          start: (pageNum - 1) + 1,
          nums: this.nums
        })
        .then(res => {
          this.closeLoading()
          console.log(res.data.data)
          if (res.data.code == 200) {
            this.tableData = res.data.data.data
          }
        })
        .catch(err => {
          this.closeLoading()
          console.log(err)
        })
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handleBeforeUpload(file) {
      this.faceImage = file;
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
    currentPageChange(pageNum) {
      this.getPageData(pageNum)
    },
    addGoods() {
      var formData = new FormData()
      for (var key in this.form) {
        
        formData.append(key, this.form[key])
      }
      formData.append("image", this.faceImage)
      this.openLoading("商品添加中...")
      this.$axios.post("/admin/goodsAdd", formData)
        .then(res => {
          this.closeLoading()
          console.log(res)
          if (res.data.code == 200) {
            this.form = {
              price: null,
              name: ''
            }
          } else {
          }
        })
        .catch(err => {
          this.closeLoading()
          this.form.expireTime = null
          this.form.produceTime = null
          console.log(err)
        })
    }
  }
}

</script>
<style scoped>
#goods-manage {
  width: 100%;
  display: flex;
  justify-items: center;
}

#goods-manage .left {
  width: 50%;
  margin: 20px;
}

#goods-manage .right {
  width: 50%;
  margin: 20px;
}

#goods-manage .demo-table-expand {
  font-size: 0;
}

#goods-manage .demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}

#goods-manage .demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}

</style>
