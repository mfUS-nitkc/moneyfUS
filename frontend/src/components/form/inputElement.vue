<template>
  <div>
    <div>{{ label }}</div>
    <slot />
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  label?: string
}>()
</script>