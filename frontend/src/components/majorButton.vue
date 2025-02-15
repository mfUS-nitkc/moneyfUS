<template>
  <v-col cols="12">
    <v-btn :style="buttonStyle" block height="80" @click="handleClick" class="common-button" :to="link" nuxt>
      <!-- アイコン部分 -->
      <v-icon size="40" class="button-icon" :style="{color: textColor}">{{ icon }}</v-icon>
      <!-- テキスト部分 -->
      <span class="button-text" :style="{color: textColor}">{{ text }}</span>
    </v-btn>
  </v-col>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, computed } from 'vue'

/**
 * Props定義  
 * - icon: ボタン左側に表示するアイコン名  
 * - text: ボタンに表示するテキスト  
 * - color: ボタンの背景色（例: '#673AB7' や 'blue'）  
 * - link: ボタンのリンク
 */
const props = defineProps<{
  icon: string
  text: string
  color: string
  link?: string
}>()

/**
 * Emit定義（クリック時に発火）
 */
const emit = defineEmits<{
  (e: 'click'): void
}>()

/**
 * 背景色を適用
 */
const buttonStyle = computed(() => ({
  backgroundColor: props.color,
  borderRadius: '0px'
}))

const textColor = computed(() => {
  const hex = props.color.replace('#', '') // `#`を削除
  if (hex.length !== 6) return '#FFFFFF' // 不正な場合はデフォルト白
  const r = parseInt(hex.substring(0, 2), 16)
  const g = parseInt(hex.substring(2, 4), 16)
  const b = parseInt(hex.substring(4, 6), 16)

  // 輝度（luminance）の計算
  const luminance = 0.299 * r + 0.587 * g + 0.114 * b

  // 128より明るいなら黒、暗いなら白を返す
  return luminance > 128 ? '#000000' : '#FFFFFF'
})

/**
 * クリック時の処理
 */
const handleClick = () => {
  emit('click')
}
</script>

<style scoped>
/* ボタンスタイル */
.common-button {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 12px;
  text-align: left;
  white-space: normal;
}

/* アイコンのスタイル */
.button-icon {
  margin-right: 12px;
}

/* テキストのスタイル */
.button-text {
  flex: 1;
  font-size: 18px;
  white-space: normal;
  word-break: break-word;
  text-align: left;
}
</style>
