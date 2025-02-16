<template>
  <v-container>
    <!-- 例: 保存ボタンとして利用 -->
    <MajorButton
      icon="mdi-content-save"
      text="保存する（とても長いテキストでも折り返して表示されます）"
      color="#1976D2"
      @click="handleSave"
    />
    <!-- 例: 白っぽい背景でも自動的に黒基調文字色になる -->
    <MajorButton
      icon="mdi-home"
      text="てすと"
      color="#f0f0f0"
      @click="handleSave"
    />
  </v-container>
</template>

<script lang="ts" setup>
const handleSave = () => {
  console.log('保存ボタンがクリックされました。')
}
</script>
