<template>
  <DataCard></DataCard>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import DataCard from '@/components/DataCard.vue'

@Options({
  components: {
    DataCard
  }
})

export default class Chart extends Vue {

}
</script>

<style scoped>
</style>
