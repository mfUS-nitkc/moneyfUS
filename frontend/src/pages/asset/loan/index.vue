<template>
  <v-container justify="center">
    <v-row v-for="(elm, i) in elements" :key="i" class="my-0">
      <v-col class="py-0">
        <MajorButton :link="elm.link" :text="elm.text" color="green">

        </MajorButton>
      </v-col>
    </v-row>
    <v-row>

    </v-row>
  </v-container>
</template>
<script lang="ts" setup>
const elements = [
  {
    text: "貸し管理",
    link: "loan/lend",
  },
  {
    text: "催促",
    link: "loan/remind",
  },
  {
    text: "借り管理",
    link: "loan/borrowed"
  },
  {
    text: "割り勘入力",
    link: "loan/split"
  }
]
</script>
