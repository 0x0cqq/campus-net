<template lang="html">
  <div id="header">
    <div id="header-img">
      <div id="wifi-logo">
        <embed :src="wifi" type="image/svg+xml" />
      </div>
      <div id="header-text">
        <div id="school-logo">
          <embed :src="logo" type="image/svg+xml" />
        </div>
        <p id="title">无线校园网</p>
        <p id="english-title">Tsinghua University Wireless Network</p>
      </div>
    </div>
    <div id="header-qrcode">
      <img id="qrcode" :src="qrcode" alt="二维码">
      <p style="white-space: nowrap; font-size:13px; margin: 5%;">欢迎关注“清华大学信息服务”</p>
    </div>
    <div id="header-mobile">
      <img id="mobile-qrcode" :src="atTsinghua" alt="atTsinghua">
    </div>
  </div>
  <Login>
  </Login>
</template>
<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import Login from '@/components/Login.vue'
import schoolLogo from '@/assets/logo.svg'
import wifiLogo from '@/assets/wifi.svg'
import qrcodeImg from '@/assets/qrcode.jpg'
import atTsinghuaImg from '@/assets/attsinghua.png'

@Options({
  components: {
    Login
  }
})
export default class App extends Vue {
  logo: string = schoolLogo
  wifi: string = wifiLogo
  qrcode: string = qrcodeImg
  atTsinghua : string = atTsinghuaImg
}
</script>

<style scoped>
* {
  margin: 0%;
  padding: 0%;
}
#title {
  font-family: 'Microsoft YaHei', 'Dengxian';
  color: #db6851;
  font-size: 34px;
  margin-top: -8px;
}
#english-title {
  font-weight: lighter;
  font-size: 18px;
}
#school-logo {
  width: 100%;
  margin-left: 3px;
}
#header {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 16px;
}
#header-img {
  margin: 10px 50px 10px 0px;
  display: flex;
}
#header-text {
  margin-left: -15px;
}
#header-qrcode {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#qrcode {
  width: 129px;
  height: 129px;
}
#header-mobile{
  margin: auto 10px;
}
</style>
