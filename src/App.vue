<template>
  <Info name="cqqthu20"></Info>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import HelloWorld from './components/HelloWorld.vue'
import Info from './components/Info.vue'

@Options({
  components: {
    HelloWorld,
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
  margin: 100px;
}
body {
  background: #E6E6E6;
}
</style>
