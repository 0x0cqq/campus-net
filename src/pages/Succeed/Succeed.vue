<template>
  <Info name="cqqthu20"></Info>
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
  data () {
    return {
      name: 'cqqthu20'
    }
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
