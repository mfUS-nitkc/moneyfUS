<template>
  <form-input-element :label="label">
    <v-text-field
    :label="label"
    v-model="value"
    :rules="rules"
    variant="outlined"
    :suffix="suffix"
    :type="type || ''"
    bg-color="white"
    ></v-text-field>
  </form-input-element>
</template>

<script lang="ts" setup>
import { computed, defineProps, defineEmits } from 'vue'
const value = defineModel()
const props = defineProps<{
  label?: string,
  suffix?: string,
  rules?: Array<(value: any) => boolean | string>
  type?: string
}>()
</script>

<style scoped>
</style>
