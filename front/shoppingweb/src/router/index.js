import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import Register from '@/components/register'
import AdminIndex from '@/components/admin/adminIndex'
import GoodsManage from '@/components/admin/goodsManage'
import UserManage from '@/components/admin/userManage'
import MainIndex from '@/components/front/mainIndex'
import Center from '@/components/front/center'
import Court from '@/components/front/court'
import Personal from '@/components/front/personal'
import Receipt from '@/components/front/receipt'
import GoodsDetail from '@/components/front/goodsDetail'

Vue.use(Router)

export default new Router({
  routes: [{
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: "/register",
      name: "Register",
      component: Register
    },
    {
      path: "/admin/index",
      name: "AdminIndex",
      component: AdminIndex,
      children: [{
          path: 'goods',
          component: GoodsManage
        },
        {
          path: 'user',
          component: UserManage
        }
      ]
    },
    {
      path: "/",
      name: "MainIndex",
      component: MainIndex,
      children: [{
        path: 'center',
        component: Center
      },{
        path: 'receipt',
        component: Receipt
      },{
        path: 'goods/detail',
        name:"GoodsDetail",
        component: GoodsDetail
      },{
        path:'court',
        component:Court
      },{
        path:'personal',
        component:Personal
      }]
    }
  ]
})
