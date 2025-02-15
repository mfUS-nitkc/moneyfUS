<template>
  <form-input-element :label="label">
    <v-text-field
    :label="label"
    v-model="value"
    :rules="rules"
    outlined
    :type="type || ''"
    bg-color="white"
    ></v-text-field>
  </form-input-element>
</template>

<script lang="ts" setup>
import { computed, defineProps, defineEmits } from 'vue'
const value = defineModel()
const props = defineProps<{
  label?: string
  rules?: Array<(value: any) => boolean | string>
  type?: string
}>()
</script>

<style scoped>
</style>
