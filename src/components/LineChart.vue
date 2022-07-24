<template>
  <canvas ref="canvas" :x-data="data" :width="width" :height="height"></canvas>
</template>

<script lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  TimeScale,
  Tooltip
} from 'chart.js'
import 'chartjs-adapter-moment'

Chart.register(
  LineController, LineElement, PointElement, LinearScale, TimeScale, Tooltip
)

export default {
  name: 'LineChart',
  props: ['data', 'width', 'height'],
  setup (props: any) {
    const chartDev = ref(null)
    const canvas = ref(null)
    const chartValue = ref(null)

    let chart: Chart | null = null

    onMounted(() => {
      const ctx = canvas.value
      chart = new Chart(ctx as any, {
        type: 'line',
        data: props.data,
        options: {
          borderColor: 'rgb(75, 192, 192)',
          scales: {
            x: {
              type: 'time',
              time: {
                parser: 'hh:mm:ss',
                unit: 'second',
                tooltipFormat: 'MMM DD, H:mm:ss a',
                displayFormats: {
                  second: 'H:mm:ss'
                }
              }
            }
          },
          animation: false,
          maintainAspectRatio: false,
          resizeDelay: 200,
          interaction: {
            intersect: false,
            mode: 'nearest'
          }
        }
      })
    })

    // destroy
    onUnmounted(() => { if (chart !== null) chart.destroy() })

    // reactive data update
    watch(
      () => props.data,
      (data) => {
        if (chart !== null) {
          chart.data = data
          chart.update()
        }
      }
    )

    return { canvas, chartValue, chartDeviation: chartDev }
  }
}
</script>
<style>
</style>
