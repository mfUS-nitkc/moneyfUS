<template>
  <div>
    <div class="mb-3">{{ label }}</div>
    <slot />
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  label?: string
}>()
</script>