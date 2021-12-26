import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import Axios from 'axios'
import './default.css'

import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

Vue.use(ElementUI)

Axios.defaults.baseURL = "http://1.15.151.123:5000"
Axios.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
Axios.defaults.headers['Access-Control-Allow-Origin'] = '*Access-Control-Allow-Credentials: true'
Vue.prototype.$axios = Axios

Vue.filter('imageFliter', function(image) {
  var list = image.split("\/");
  return "http://1.15.151.123/var/www/eshop/static/goods/" + list[list.length-1];
})


new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
