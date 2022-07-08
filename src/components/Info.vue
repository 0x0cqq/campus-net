<template>
  <div id="info">
    <div id="greeting">
      <div id="welcome-text">
        <p id="laugh-welcome">:P</p>
        <p id="chinese-welcome">欢迎,</p>
        <p id="english-welcome">Welcome.</p>
      </div>
      <div id="greeting-triangle"></div>
    </div>
    <div id="info-block">
      <h2 id="user-name">{{ name }}</h2>
      <div style="height:22px"></div>
      <div id="info-content">
        <div class="info-block" id="connect-info">
          <div class="label-text">
            <p>已连接</p>
            <p class="english">Duration</p>
          </div>
          <div class="info-block-content" id="connect-time">
            <p id="display-connect-time">{{hour}}:{{minute}}:{{second}}</p>
          </div>
        </div>
        <div class="info-block" id="usage-info">
          <div class="label-text">
            <p>已用流量</p>
            <p class="english">Usage</p>
          </div>
          <div class="info-block-content" id="usage">
            <div id="usage-volume">
              <p>&nbsp;&nbsp;&nbsp;</p>
              <p>&nbsp;&nbsp;&nbsp;</p>
              <p>&nbsp;50</p>
              <p>&nbsp;75</p>
              <p>100</p>
              <p>125</p>
            </div>
            <div id="usage-bar">
              <div id="usage-bar-fill" :style="{width : usageNumberLength}"></div>
              <div id="usage-number">{{usageNumberText}}</div>
              <div id="usage-bar-50"></div>
              <div id="usage-bar-50-75"></div>
              <div id="usage-bar-75-100"></div>
              <div id="usage-bar-100-125"></div>
            </div>
          </div>
        </div>
      </div>
      <div id="bar">
        <div id="corner"></div>
        <button id="disconnect-button" @click="clickDisconnect()">
          <p id="chinese-disconnect">断开连接</p>
          <p class="english" id="english-disconnect">Disconnect</p>
        </button>
      </div>
      <div id="links">
        <div v-for="item in links" :key="item.name" class="link">
          <img class="link-img" :src="item.img" />
          <a class="link-text english" :href="item.link">{{item.name}}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import infoImg from '@/assets/popup_info.gif'
import libImg from '@/assets/popup_lib.gif'
import learnImg from '@/assets/popup_learn.gif'
import mailImg from '@/assets/popup_mail.gif'

@Options({
  props: {
    name: {
      type: String,
      default: 'NO-NAME'
    },
    usageVolume: {
      type: Number,
      default: 1
    }
  }
})

export default class Info extends Vue {
  name!: string
  hour!: string
  minute!: string
  second!: string
  startDate!: Date
  usageVolume!: number // record as bytes
  buttonColor!: string
  /* eslint-disable-next-line */
  links!: Array<{name : string, link : string, img : any}>

  data () {
    return {
      hour: '00',
      minute: '00',
      second: '00',
      startDate: new Date(),
      usageVolume: this.usageVolume,
      buttonColor: '#c0bdcc',
      links: [
        {
          name: 'Info',
          img: infoImg,
          link: 'http://info.tsinghua.edu.cn'
        },
        {
          name: 'Lib',
          img: libImg,
          link: 'https://lib.tsinghua.edu.cn'
        },
        {
          name: 'Learn',
          img: learnImg,
          link: 'https://learn.tsinghua.edu.cn'
        },
        {
          name: 'Mail',
          img: mailImg,
          link: 'https://mails.tsinghua.edu.cn'
        }
      ]
    }
  }

  mounted () {
    this.startDate = new Date()
    setInterval(() => {
      this.updateTime()
    }, 500)
  }

  public updateTime () : void {
    const now = new Date()
    const diff = now.getTime() - this.startDate.getTime()
    const hour = Math.floor(diff / (1000 * 60 * 60))
    const minute = Math.floor(diff / (1000 * 60)) % 60
    const second = Math.floor(diff / 1000) % 60
    this.hour = hour.toString().padStart(2, '0')
    this.minute = minute.toString().padStart(2, '0')
    this.second = second.toString().padStart(2, '0')
  }

  public clickDisconnect () : void {
    this.axios.post('/api/usage_volume', {
      // 0 to 1 GB
      new_usage_volume: this.usageVolume + Math.floor(Math.random() * 1024 * 1024 * 1024)
    }).then(() => {
      document.cookie = 'userid=; Max-Age=0'
    }).catch(() => {
      console.log('update usage failed')
    })
    alert('您已断开连接')
    window.location.href = '/'
  }

  get usageNumberLength () : string {
    const percentage = Math.ceil(Math.min(this.usageVolume / (125 * 1024 * 1024 * 1024), 1) * 100)
    return `${percentage}%`
  }

  get usageNumberText () : string {
    // as bytes
    if (this.usageVolume < 1024) {
      return `${this.usageVolume}B`
    } else if (this.usageVolume < 1024 * 1024) {
      return `${(this.usageVolume / 1024).toFixed(2)}KB`
    } else if (this.usageVolume < 1024 * 1024 * 1024) {
      return `${(this.usageVolume / (1024 * 1024)).toFixed(2)}MB`
    } else {
      return `${(this.usageVolume / (1024 * 1024 * 1024)).toFixed(2)}GB`
    }
  }
}
</script>

<style scoped>
* {
  margin: 0%;
  padding: 0%;
  border: 0;
}
#info{
  position: relative;
  margin: 10% 5% ;
}
#greeting {
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  max-width: 512px;
  height: 224px;
  background-color: #E64E2E;
  z-index: -1;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
  color: #FFFFFF;
}
#greeting-triangle {
  position: absolute;
  bottom: -48px;
  left: 32px;
  border-color: #E64E2E transparent ;
  border-width: 48px 48px 0 0;
  border-style: solid;
}
#laugh-welcome {
  margin-top: -15px;
  font-size: 80px;
  font-weight: lighter;
}
#chinese-welcome {
  margin-top: 20px;
  font-family: "Dengxian";
  font-weight: lighter;
  font-size: 30px;
  margin-top: 0px;
}
#english-welcome {
  margin-top: 15px;
  font-size: 20px;
  color: rgba(255,255, 255,0.9);
  font-family: "Dengxian";
  font-weight: lighter
}
#welcome-text {
  margin: 32px 0 0 32px;
}
#info-block {
  position: absolute;
  top: 32px;
  left: 128px;
  width: calc(80% - 32px);
  max-width: 352px;
  min-width: 200px;
  min-height: 208px;
  padding: 32px;
  background-color: #f2f2f2;
}
#user-name {
  text-align: start;
  color: #E64E2E;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 34px;
  font-weight: lighter;
}
#display-connect-time {
  color: #Ec6677;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 28px;
  font-weight: lighter;
  margin: 0px;
}
#usage-bar {
  position: relative;
  width: 100%;
  max-width: 280px;
  height: 32px;
}
#usage-volume {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 280px;
}
#usage-volume p {
  font-family: Verdana, Geneva, sans-serif;
  font-size: 13px;
  text-align: right;
  color: #969696;
  margin: 0px;
}
#usage-bar-50 {
  float: left;
  position: absolute;
  left: 0%;
  width: 40%;
  height: 100%;
  z-index: 1;
  background-color: #D8D8D8;
}
#usage-bar-50-75 {
  float: left;
  position: absolute;
  left: 40%;
  width: 20%;
  height: 100%;
  z-index: 1;
  background-color: #E7E3E4;
}
#usage-bar-75-100 {
  float: left;
  position: absolute;
  left: 60%;
  width: 20%;
  height: 100%;
  z-index: 1;
  background-color: #DBD5D7;
}
#usage-bar-100-125 {
  float: left;
  position: absolute;
  left: 80%;
  width: 20%;
  height: 100%;
  z-index: 1;
  background-color: #CFC8CB;
}
#usage-number{
  float: left;
  position: absolute;
  left: 0%;
  font-size : 24px;
  color: #5C5C5C;
  text-align: left;
  z-index: 3;
  margin-left: 10px;
}
#usage-bar-fill{
  float: left;
  position: absolute;
  left: 0%;
  height: 100%;
  background-color: #E64E2E;
  z-index: 2;
}
#bar {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: -16px;
  right: -16px;
  width: 208px;
  height: 80px;
  background-color: #FFFFFF;
  box-shadow: 0 0 8px rgba(0,0,0,0.1);
}
#disconnect-button {
  width: 174px;
  height: 46px;
  background-color: #c0bdcc;
  border: #B2AABE solid 1px;
}
#disconnect-button:hover {
  background-color: #d6d2e0;
}
#disconnect-button:active {
  background-color: #b1aac4;
}
#chinese-disconnect {
  font-family: "Dengxian";
  font-weight: bold;
  color: #444444;
  font-size: 22px;
  margin-top: 0px;
}
#english-disconnect {
  font-size: 20px;
  margin-top: -3px;
  color:#555555;
  font-family: "Dengxian"
}
.info-block-content {
  margin: 0px 10px;
  width: 100%;
}
.info-block {
  width: auto;
  display: flex;
  flex-direction: row;
}
.label-text {
  color: #303030;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.label-text p {
  font-size: 12px;
  /* float: left; */
  text-align: right;
  margin: 0%;
  white-space:nowrap;
}
.english {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
#corner{
  position: absolute;
  top: -16px;
  right: 0px;
  border-color: transparent #CCCCCC;
  border-width: 16px 0 0 16px;
  border-style: solid;
}
.link-text {
  color: #AD3B23;
  font-size: 11px;
  margin: 0px 5px;
}
.link {
  margin: 0px 5px;
}
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
#links {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  position: absolute;
  right: 0px;
  top: 300px;
}
@media (max-width: 600px) {
  #info-block {
    position: relative !important;
    left: 0px;
    top: 48px;
  }
  #greeting {
    position: relative !important;
    height: auto !important;
  }
  #welcome-text p {
    display: inline-block;
  }
}
</style>
