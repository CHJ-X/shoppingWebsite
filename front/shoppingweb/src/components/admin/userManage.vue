<template>
  <div id="user-manage">
    <!-- 表格开始 -->
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column prop="username" label="用户名" width="120">
      </el-table-column>
      <el-table-column prop="gender" label="性别" width="120">
      </el-table-column>
      <el-table-column prop="mail" label="邮箱" width="120">
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="200">
        <template slot-scope="scope">
          <el-button type="primary" size="small">锁定</el-button>
          <el-button type="danger" size="small" @click="deleteUser(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 表格结束 -->
    <!-- 分页开始 -->
    <el-pagination layout="prev, pager, next" @current-change="currentPageChange" :page-size="nums" :total="userTotal">
    </el-pagination>
    <span>一共{{userTotal}}条</span>
    <!-- 分页结束 -->
  </div>
</template>
<script>
export default {
  name: 'UserManage',
  created() {
    this.getUserTotal()
    this.getPageData(1)
  },
  data() {
    return {
      userTotal: 30,
      nums: 15,
      loading: null,
      tableData: []
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
    deleteUser(row) {
      var id = row._id 
      this.openLoading("删除中...")
      this.$axios.delete("/admin/deleteUsers",{data:{
        id:id
      }})
      .then(res=>{
        this.closeLoading()
        console.log(res)
        if(res.data.code == 200){

        }else{
          this.$message({
            message:"删除失败",
            type:"warning"
          })
        }
      })
      .catch(err=>{
        this.closeLoading()
        console.log(err)
      })    
    },
    currentPageChange(page) {
      console.log(page)
      this.getPageData(page)
    },
    getUserTotal() {
      this.openLoading("数据加载中...")
      this.$axios.get("/admin/getUsers")
        .then(res => {
          this.closeLoading()
          console.log(res)
          if (res.data.code == 200) {
            this.userTotal = res.data.data.nums
          }
        })
        .catch(err => {
          this.closeLoading()
          console.log(err)
        })
    },
    getPageData(pageNum) {
      this.openLoading("数据加载中...")
      this.$axios.post("/admin/getUsers", {
          start: (pageNum - 1) + 1,
          nums: 15
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
  }
}

</script>
<style>
</style>
