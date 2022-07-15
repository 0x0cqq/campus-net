<template>
  <canvas ref="canvas" :x-data="data" :width="width" :height="height"></canvas>
</template>

<script>
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
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  TimeScale,
  Tooltip
)

export default {
  name: 'LineChart',
  props: ['data', 'width', 'height'],
  setup (props) {
    const canvas = ref(null)
    const chartValue = ref(null)
    const chartDeviation = ref(null)

    let chart = null

    onMounted(() => {
      const ctx = canvas.value
      chart = new Chart(ctx, {
        type: 'line',
        data: props.data,
        options: {
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
          interaction: {
            intersect: false,
            mode: 'nearest'
          },
          animation: false,
          maintainAspectRatio: false,
          resizeDelay: 200
        }
      })
    })

    onUnmounted(() => chart.destroy())

    watch(
      () => props.data,
      (data) => {
        // update chart
        chart.data = data
        chart.update()
      }
    )

    return {
      canvas,
      chartValue,
      chartDeviation
    }
  }
}
</script>
<style>
</style>
