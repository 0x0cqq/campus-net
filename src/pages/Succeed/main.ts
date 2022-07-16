import { createApp } from 'vue'
import Succeed from './Succeed.vue'
import Chart from './Chart.vue'

import axios from 'axios'
import VueAxios from 'vue-axios'

createApp(Succeed).use(VueAxios, axios).mount('#succeed')
createApp(Chart).mount('#chart')
