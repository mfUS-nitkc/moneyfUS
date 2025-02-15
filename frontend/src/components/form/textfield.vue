<template>
  <div>
    <div>{{ label }}</div>
    <v-text-field
    :label="label"
    v-model="internalValue"
    :rules="rules"
    outlined
    :type="password ? 'password':''"
    ></v-text-field>
  </div>
</template>

<script lang="ts" setup>
import { computed, defineProps, defineEmits } from 'vue'

const props = defineProps<{
  label?: string
  value: string | number
  rules?: Array<(value: any) => boolean | string>
  password?: Boolean
}>()

const emit = defineEmits<{
  (e: 'update:value', value: string | number): void
}>()

const internalValue = computed({
  get: () => props.value,
  set: (value: string | number) => emit('update:value', value)
})
</script>

<style scoped>
</style>
