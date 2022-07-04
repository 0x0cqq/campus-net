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
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import noteLogo from '@/assets/note.svg'

@Options({
  props: {
    targetUrl: {
      type: String,
      default: 'https://www.baidu.com'
    }
  }
})

export default class Login extends Vue {
  targetUrl!: string
  username!: string
  password!: string
  noteImg : string = noteLogo
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
  margin: auto;
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
</style>
