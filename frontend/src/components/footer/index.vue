<template>
  <v-footer app class="pa-0">

    <v-container class="pa-1">
      <v-row justify="center" style="flex-wrap:nowrap;" class="ma-0">
        <v-col class="pa-2" v-for="menu in menus" :key="menu.name" style="aspect-ratio: 1; display: flex; align-items: center; " cols="3">
          <FooterButton :icon="menu.icon" :link="menu.link">
            {{ menu.name }}
          </FooterButton>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script setup lang="ts">

// FIXME: 実際のデータへ変更する
const menus = [
  {
    name: 'Home',
    icon: 'mdi-home-outline',
    link: '/',
  },{
    name: '家計簿',
    icon: 'mdi-notebook-edit-outline',
    link: '/log',
  },{
    name: '収支入力',
    icon: 'mdi-piggy-bank-outline',
    link: '/asset',
  },{
    name: '投稿',
    icon: 'mdi-account-group-outline',
    link: '#',
  },
]
</script>

<style>
.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}
</style>