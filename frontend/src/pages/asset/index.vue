<template>
  <MajorButton v-for="(elm, i) in elements" :key="i" :icon="elm.icon" :text="elm.text" :color="elm.color" :link="elm.link" />
</template>

<script lang="ts" setup>
const elements = [
  {
    "icon": "mdi-account",
    "text": "収入入力・予算入力",
    "color": "#82328F",
    "link": "/asset/income"
  },
  {
    "icon": "mdi-keyboard-outline",
    "text": "手動で入力",
    "color": "#78AEB1",
    "link": "/asset/outgo"
  },
  {
    "icon": "mdi-cash-multiple",
    "text": "割り勘・貸し借り",
    "color": "#83B178",
    "link": "/asset/loan"
  }
]
</script>
