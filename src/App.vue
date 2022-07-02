<template>
  <Info name="cqqthu20"></Info>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import Info from './components/Info.vue'

@Options({
  components: {
    Info
  }
})
export default class App extends Vue {
  data () {
    return {
      name: 'cqqthu20'
    }
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
}
body {
  background: #E6E6E6;
}
</style>
