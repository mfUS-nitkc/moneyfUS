<template>
  <v-app-bar elevation="0" class="navbar" density="comfortable">
    <v-app-bar-title class="title-container">
      <span>マネーフォワードUS</span>
      <svg
        class="title-icon"
        width="25"
        height="22"
        viewBox="0 0 25 22"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M13.9976 8.25H14.8289C15.9032 9.8957 17.9157 11 20.2198 11C20.7546 11 21.2796 10.9398 21.7754 10.8281V20.625C21.7754 21.3855 21.0803 22 20.2198 22C19.3594 22 18.6643 21.3855 18.6643 20.625V14.575L12.0532 19.25H14.7754C15.6358 19.25 16.331 19.8645 16.331 20.625C16.331 21.3855 15.6358 22 14.7754 22H7.7754C5.19901 22 3.10874 20.1523 3.10874 17.875V8.27148C3.10874 7.57969 2.5254 6.99102 1.74763 6.90508L1.3636 6.86211C0.512904 6.76758 -0.0947352 6.08008 0.0122092 5.32812C0.119154 4.57617 0.896932 4.03906 1.74763 4.13359L2.13165 4.17656C4.46499 4.43437 6.21985 6.1875 6.21985 8.27148V11.9367C7.89207 9.71523 10.7504 8.25 13.9976 8.25ZM21.7754 9.38867C21.2893 9.53906 20.7643 9.625 20.2198 9.625C18.8393 9.625 17.5948 9.09219 16.7393 8.25C16.5594 8.07383 16.399 7.88477 16.258 7.68281C15.8108 7.04688 15.5532 6.29922 15.5532 5.5V0.459766C15.5532 0.20625 15.7817 0.00429688 16.0685 0H16.0782C16.2386 0 16.3893 0.06875 16.4865 0.180469V0.184766L17.1087 0.915234L18.431 2.475L18.6643 2.75H21.7754L22.0087 2.475L23.331 0.915234L23.9532 0.184766V0.180469C24.0504 0.06875 24.2011 0 24.3615 0H24.3712C24.658 0.00429688 24.8865 0.20625 24.8865 0.459766V5.5C24.8865 6.24336 24.6629 6.94375 24.274 7.54531C23.7247 8.39609 22.8351 9.05781 21.7754 9.38867ZM19.4421 5.5C19.4421 5.31766 19.3601 5.1428 19.2143 5.01386C19.0684 4.88493 18.8706 4.8125 18.6643 4.8125C18.458 4.8125 18.2602 4.88493 18.1143 5.01386C17.9685 5.1428 17.8865 5.31766 17.8865 5.5C17.8865 5.68234 17.9685 5.8572 18.1143 5.98614C18.2602 6.11507 18.458 6.1875 18.6643 6.1875C18.8706 6.1875 19.0684 6.11507 19.2143 5.98614C19.3601 5.8572 19.4421 5.68234 19.4421 5.5ZM21.7754 6.1875C21.9817 6.1875 22.1795 6.11507 22.3254 5.98614C22.4712 5.8572 22.5532 5.68234 22.5532 5.5C22.5532 5.31766 22.4712 5.1428 22.3254 5.01386C22.1795 4.88493 21.9817 4.8125 21.7754 4.8125C21.5691 4.8125 21.3713 4.88493 21.2254 5.01386C21.0796 5.1428 20.9976 5.31766 20.9976 5.5C20.9976 5.68234 21.0796 5.8572 21.2254 5.98614C21.3713 6.11507 21.5691 6.1875 21.7754 6.1875Z"
          fill="black"
        />
      </svg>
    </v-app-bar-title>
    <template v-slot:append>
      <v-btn
        icon
        height="100%"
        flat
        rounded="0"
        :color="isDrawerOpen ? 'text-white bg-primary' : 'black'"
        @click="isDrawerOpen = !isDrawerOpen"
      >
        <template v-if="isDrawerOpen">
          <svg
            width="32"
            height="23"
            viewBox="0 0 43 23"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M41.8333 1.0005C41.8333 1.0005 30.3061 21.8338 16.7045 21.8338C10.1181 21.8859 4.05842 17.8651 1 11.4172C4.05842 4.96925 10.1181 0.948417 16.7045 1.0005C30.3061 1.0005 41.8333 21.8338 41.8333 21.8338"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </template>
        <template v-else>
          <v-icon>mdi-menu</v-icon>
        </template>
      </v-btn>
    </template>
  </v-app-bar>

  <v-navigation-drawer
    v-model="isDrawerOpen"
    temporary
    :floating="true"
    elevation="0"
    class="mini-drawer"
    location="right"
  >
    <v-card class="drawer-card" color="primary">
      <v-list density="comfortable">
        <v-list-item>
          <v-list-item-title class="text-lg"
            ><strong>MENU</strong></v-list-item-title
          >
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item>
          <template v-slot:prepend>
            <v-icon>mdi-account-circle</v-icon>
          </template>
          <v-list-item-title class="my-2 text-black">
            マイページ
          </v-list-item-title>
        </v-list-item>

        <v-divider></v-divider>
        <v-list-item>
          <template v-slot:prepend>
            <v-icon>mdi-account-plus</v-icon>
          </template>
          <v-list-item-title class="my-2 text-black"
            >友だち追加</v-list-item-title
          >
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item>
          <template v-slot:prepend>
            <v-icon>mdi-account-box-multiple</v-icon>
          </template>
          <v-list-item-title class="my-2 text-black"
            >友だち一覧</v-list-item-title
          >
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item @click="logout">
          <template v-slot:prepend>
            <v-icon>mdi-account-off</v-icon>
          </template>
          <v-list-item-title class="my-2 text-red"
            >ログアウト</v-list-item-title
          >
        </v-list-item>
      </v-list>
    </v-card>
  </v-navigation-drawer>
</template>

<script lang="ts" setup>
const isDrawerOpen = ref(false);
const userStore = useUserStore();

const logout = async () => {
  await userStore.logout()
  if (!userStore.isAuthenticated) {
    useRouter().push("/login")
  }
}
</script>

<style>
.v-toolbar__append {
  margin-inline: auto 0px !important;
}
</style>

<style lang="css" scoped>
/* 小型のナビゲーションドロワー（v-card 風に調整） */
.mini-drawer {
  position: absolute;
  top: 56px; /* v-app-bar の下に配置 */
  right: 16px;
  width: 250px; /* v-card っぽいサイズ */
  border-radius: 0px;
  background: transparent; /* デフォルトの背景色を透明に */
}

/* v-card 風のデザイン */
.drawer-card {
  border-radius: 0px; /* 丸み */
}

.navbar {
  background-color: snow;
  padding: 0;
}

.title-container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  width: 100%;
  text-align: center;
}

.title-icon {
  position: absolute;
  top: -50%;
  left: 75%;
  pointer-events: none;
}
</style>
