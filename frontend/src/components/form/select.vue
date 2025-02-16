<template>
  <FormInputElement :label="label">
    <v-select :rules="rules" :label="label" bg-color="white" v-model="selected" :items="items" return-object></v-select>
  </FormInputElement>
</template>
<script setup lang="ts">
type SelectElement = {
  title: string,
  value: string
}

const props = defineProps<{
  label?: string,
  rules?: Array<(v: any) => boolean | string>,
  items: Array<SelectElement>
}>()

const selected = defineModel<SelectElement>()
</script>
