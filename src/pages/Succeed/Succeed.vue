<template>
  <Info :name="name" :usageVolume="usageVolume"></Info>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import Info from '../../components/Info.vue'

@Options({
  components: {
    Info
  }
})
export default class Succeed extends Vue {
  name!: string
  usageVolume!: number
  data () {
    return {
      name: this.name,
      usageVolume: this.usageVolume
    }
  }

  mounted () {
    // get and show username
    this.axios.get('/api/get_username').then(res => {
      console.log(res.data)
      this.name = res.data
    })
    // get and show user usage
    this.axios.get('/api/usage_volume').then(res => {
      console.log(res.data)
      this.usageVolume = Number(res.data)
    })
  }
}
</script>

<style>
#succeed {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  /* display: flex;
  width: 100%;
  height: 100%;
  justify-content: center; */
}
body {
  background: #E6E6E6;
}
</style>
