<template>
  <LineChart :data="chartData" width="595" height="248" />
</template>

<script lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import LineChart from './LineChart.vue'

export default {
  name: 'DataCard',
  components: {
    LineChart
  },
  setup () {
    const counter = ref(0)
    const range = ref(10)
    const currentDate = ref(new Date())

    // list of range number of 0
    const sampleData = ref(Array<number>(range.value).fill(0))

    // Generate fake dates from now to back in time
    const generateDates = () => {
      const dates = [] as Date[]
      sampleData.value.forEach((v, i) => {
        dates.push(new Date((Math.floor(currentDate.value.getTime() / 1000) - i * 2) * 1000))
      })
      return dates
    }

    const sampleLabels = ref(generateDates().reverse())

    // Loop through data array and update
    watch(counter, () => {
      currentDate.value = new Date((Math.floor(currentDate.value.getTime() / 1000) + 2) * 1000)
      sampleLabels.value.shift()
      sampleLabels.value.push(currentDate.value)
      sampleData.value.shift()
      sampleData.value.push(sampleData.value[sampleData.value.length - 1] + Math.random() * 10)
    })

    const chartData = computed(() => {
      return {
        labels: sampleLabels.value,
        datasets: [
          {
            data: [...sampleData.value]
          }
        ]
      }
    })

    // Fake update every 2 seconds
    const interval = ref<number>(0)
    onMounted(() => {
      interval.value = setInterval(() => {
        counter.value++
      }, 2000)
    })

    onUnmounted(() => {
      clearInterval(interval.value)
    })

    return {
      counter,
      range,
      sampleData,
      sampleLabels,
      interval,
      chartData
    }
  }
}
</script>
<style>
</style>
