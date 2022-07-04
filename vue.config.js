const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/campus-net/'
    : '/',
  pages: {
    // 先配置主页
    index: {
      entry: 'src/main.ts',
      template: 'public/index.html',
      title: '华清大学无线校园网 Tsinghua University Wireless Network'
    },
    // 再配置各个子页面
    succeed: {
      entry: 'src/pages/Succeed/main.ts',
      template: 'public/succeed.html',
      title: '华清大学校园网 Tsinghua University Network'
    }
  }
}
