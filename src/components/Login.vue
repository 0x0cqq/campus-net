<template>
  <div id="login">
    <div id="greeting">
      <div id="greeting-text">
        <p class="english">;)</p>
        <p>你好,Hi,</p>
      </div>
      <div id="greeting-triangle"></div>
      <div id="noticing-box">
        <div id="note-bar">
          <embed :src="noteImg" type="image/svg+xml" />
          <p>通知</p>
          <p class="english">Notification</p>
        </div>
        <div id="notice-container">
          <div class="scrolling">
            <p>{{message}}</p>
          </div>
        </div>
      </div>
      <div id="corner"></div>
    </div>
    <div id="login-box">
      <form action="" method="get">
        <div class="login-form">
          <div id="username-line" class="line">
            <div id="username-label" class="label-text">
              <p>用户名</p>
              <p class="english">User ID</p>
            </div>
            <div id="username-input">
              <input class="input-box" type="text" v-model="username" />
            </div>
          </div>
          <div id="password-line" class="line">
            <div id="password-label" class="label-text">
              <p>密码</p>
              <p class="english">Password</p>
            </div>
            <div id="password-input">
              <input class="input-box" type="password" v-model="password" />
            </div>
          </div>
        </div>
        <div id="button-line" class="line">
          <button id="submit-button" @click="submit()">
            <p>连接</p>
            <p class="english">Connect</p>
          </button>
        </div>
      </form>
      <div id="login-triangle"></div>
    </div>
  </div>
  <div style="display:flex; flex-direction:row; justify-content:center;">
    <div id="foot-bar">
      <div id="download-block">
        <div id="download-title-bar">
          <embed :src="downloadImg" type="image/svg+xml" />
          <p> 下载客户端 </p>
          <p class="english">Client Download</p>
        </div>
        <div id="download-list">
          <template v-for="item in download_list" :key="item.name">
            <div class="download-item">
              <a :href="item.link">
                <img :src="item.img" />
                <p>{{item.name}}</p>
              </a>
            </div>
          </template>
        </div>
      </div>
      <div id="links">
        <div id="bookmark-link" class="link">
          <img :src="bookmarkLogo"/>
          <a class="link-label-text" href="javascript:addBookmark('THUNet 无线网登录');">
            <p>收藏本站</p>
            <p class="english">Bookmark This Page</p>
          </a>
        </div>
        <div id="help-link" class="link">
          <img :src="helpLogo"/>
          <a class="link-label-text" href="https://www.bilibili.com/video/BV1GJ411x7h7">
            <p>帮助</p>
            <p class="english">Help</p>
          </a>
        </div>
        <div id="contact-link" class="link">
          <img :src="contactLogo"/>
          <a class="link-label-text" href="https://www.bilibili.com/video/BV1GJ411x7h7">
            <p>联系</p>
            <p class="english">contact</p>
          </a>
        </div>
        <div class="link">
          <a class="link-label-text" href="https://www.bilibili.com/video/BV1GJ411x7h7">
            <p>+86-10-62784859</p>
            <p class="english">its@tsinghua.edu.cn</p>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import noteLogo from '@/assets/note.svg'
import downloadLogo from '@/assets/download.svg'
import windowsLogo from '@/assets/windows.gif'
import androidLogo from '@/assets/android.gif'
import iosLogo from '@/assets/ios.gif'
import linuxLogo from '@/assets/linux.gif'
import macosLogo from '@/assets/mac.gif'
import bookmarkLogo from '@/assets/bookmark.gif'
import helpLogo from '@/assets/help.gif'
import contactLogo from '@/assets/contact.gif'

@Options({
  props: {
    targetUrl: {
      type: String,
      default: 'https://www.baidu.com'
    },
    message: {
      type: String,
      default:
`
为保障师生的密码安全，学校即日起组织开展2022年度电子身份年审工作。具体通知如下：

一、年审范围：全校师生员工（包含离退休人员）

二、年审方式：

用户可以通过以下任意一种渠道修改个人密码：

1、登录学校用户电子身份服务系统（https://id.tsinghua.edu.cn）；

2、进入“清华大学信息服务”微信公众号的“认证助手”；

3、访问学校信息门户（http://info.tsinghua.edu.cn）。

具体操作请见附件《电子身份年审用户操作说明（2022年度）》。

三、特别提示：

用户电子身份服务系统具备绑定手机找回密码功能，建议用户在修改个人密码的同时绑定手机号。
`
    }
  }
})

export default class Login extends Vue {
  targetUrl!: string
  username!: string
  password!: string
  noteImg : string = noteLogo
  downloadImg : string = downloadLogo
  message!: string
  bookmarkLogo : string = bookmarkLogo
  helpLogo : string = helpLogo
  contactLogo : string = contactLogo
  download_list: Array<{name: string, img: string, link : string}> = [
    {
      name: 'Windows',
      img: windowsLogo,
      link: 'https://www.bilibili.com/video/BV1GJ411x7h7'
    },
    {
      name: 'MacOS',
      img: macosLogo,
      link: 'https://www.bilibili.com/video/BV1GJ411x7h7'
    },
    {
      name: 'Linux',
      img: linuxLogo,
      link: 'https://www.bilibili.com/video/BV1GJ411x7h7'
    },
    {
      name: 'Android',
      img: androidLogo,
      link: 'https://www.bilibili.com/video/BV1GJ411x7h7'
    },
    {
      name: 'iOS',
      img: iosLogo,
      link: 'https://www.bilibili.com/video/BV1GJ411x7h7'
    }
  ]

  public submit (): void {
    // empty now
    alert('submit')
  }
}

</script>
<style scoped>
* {
  margin: 0;
  padding: 0;
}

#login {
  position: relative;
  margin: auto;
  width: auto;
}

.line {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

#login-box {
  position: absolute;
  left: calc(50% - 56px);
  top: 32px;
  max-width: 400px;
  min-height: 240px;
  width: 100%;
  padding: 32px;
  background: #F2F2F2;
  -webkit-box-shadow: 0 0 8px rgb(0 0 0 / 10%);
  -moz-box-shadow: 0 0 4px rgba(0,0,0,0.1);
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
}
#greeting {
  position: relative;
  margin: 0px auto 50px auto;
  max-width: 720px;
  width: auto;
  height: 304px;
  background-color: #E64E2E;
}
#login-triangle {
  position: absolute;
  bottom: -48px;
  right: 32px;
  border-color: #F2F2F2 transparent;
  border-width: 48px 48px 0 0;
}

#login-triangle, #corner, #greeting-triangle{
  width: 0;
  height: 0;
  border-style: solid;
}

.input-box {
  height: 42px;
  width: 298px;
  /* width: 100%; */
}

input {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 34px;
  padding: 2px;
  border: #E6E6E6 solid 1px;
  outline: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  border-radius: 0;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  float: right;

}

input:hover {
  border-color: #CCCCCC;
}

input:focus {
  border-color: #FBB03B;
  -webkit-box-shadow: 0 0 8px rgb(251 176 59 / 80%);
  -moz-box-shadow: 0 0 4px rgba(251, 176, 59, 0.8);
  box-shadow: 0 0 8px rgb(251 176 59 / 80%);
}

#submit-button {
  margin: 16px auto;
  width: 100%;
  height: 46px;
  border: #9CB22E solid 1px;
  background: #C0CE55;
}
#submit-button:hover {
  background: #D2E042;;
}
#submit-button:active {
  background: #AAC30B;
}
.label-text p {
  font-size: 21px;
}

.label-text p.english {
  font-size: 16px;
}

.english {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}

#submit-button p {
  font-size: 20px
}

#submit-button p.english {
  font-size: 18px;
  font-family: Dengxian;
  /* font-weight: lighter; */
}
#greeting-text {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: center;
  color: #ffffff;
  margin : 20px 0 0 20px;
}
#greeting-text p {
  font-size: 50px;
  /* font-weight: lighter; */
  font-family: "FZLTCXHJW", DengXian, "PingFang SC";
}
#greeting-text .english {
  font-size: 96px;
  /* margin: 0 10px; */
  font-family: 'SimSun'
}
#noticing-box {
  display: flex;
  flex-direction: column;
  height: 160px;
  max-width : 320px;
  width: calc(50% - 40px);
  position: absolute;
  left: -16px;
  bottom: 0px;
  background-color: #e6562e;
  z-index: 1;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
}
#corner {
  border-color: transparent #AD3B23;
  border-width: 16px 16px 0 0;
  position: absolute;
  left: -16px;
  bottom: 160px;
}
#greeting-triangle {
  border-color: transparent #E64E2E;
  border-width:  0 0 48px 48px;
  position: absolute;
  left: 48px;
  bottom: -48px;
}
#note-bar {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  margin: 10px;
  color: rgba(255,255,255,0.8);
  font-family: FZLTCXHJW, DengXian, "PingFang SC";
  font-size: 22px;
}
#note-bar embed {
  margin: 0px 5px;
}
#note-bar p {
  margin: 0px 2px;
}
#note-bar .english{
  font-size: 14px;
  font-family: Dengxian;
}
#notice-container {
  overflow: hidden;
  height: 100%;
  padding: 20px 10px;
  color: rgba(255,255,255, 0.8);
}
.scrolling {
  animation: marquee 10s linear infinite;
}

@keyframes marquee {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(-110%);
  }
}
#foot-bar {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-around;
  max-width: 800px;
  width: 100%;
  margin-top:50px
}
#download-block {
  max-width: 304px;
  width: 100%;
}
#download-title-bar {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  margin: 10px 0;
}
#download-title-bar p {
  font-size: 20px;
  font-family: "Microsoft YaHei", DengXian, "PingFang SC";
  margin: 0px 0px 0px 5px;
}
#download-title-bar .english {
  font-size: 14px;
  font-family: Dengxian;
}
#download-list {
  background: linear-gradient( #C5C5C5, 40%, #DADADA);
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-around;
  flex-wrap: wrap;
}
.download-item a {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}
.download-item a p {
  text-decoration: none;
  font-size: 13px;
  font-family: Helvetica,Arial, sans-serif;
  margin: 12px 10px 2px 0px;
}
.download-item a img{
  width: min-content;
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
  align-items: center;
  justify-content: center;
}
.link-label-text p{
  font-size: 12px;
  color: #4F4F4F;
}
.link {
  display: flex;
  flex-direction: row;
  margin: 0px 0px 0px 5px;
}
</style>
