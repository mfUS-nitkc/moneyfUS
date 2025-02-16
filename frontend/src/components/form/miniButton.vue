<template>
  <v-btn height="1.2rem" :base-color="baseColor" :disabled="disabled" :loading="loading" v-bind="$attrs" @click="handleClick">
    <slot/>
  </v-btn>
</template>

<script setup lang="ts">
defineProps<{disabled?: boolean, loading?: boolean, baseColor?: string}>()
defineOptions({ inheritAttrs: false });

const emit = defineEmits<{
  (e: "click", event: MouseEvent): void;
}>();

function handleClick(event: MouseEvent) {
  emit("click", event);
}
</script>
