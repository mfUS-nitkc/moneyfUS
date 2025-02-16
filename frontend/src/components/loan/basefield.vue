<template>
  <v-container>
    <v-row>
      <v-col cols="auto" class="py-0">
        <v-chip variant="flat" color="#83B178" :rounded=1>
          <div class="px-2">
            {{ tag }}
          </div>
        </v-chip>
      </v-col>
      <v-spacer />
      <div v-if="props.btn">
        <v-col cols="auto" class="py-0 align-center">
          <v-btn :to="props.btn.to" nuxt>
            {{ props.btn.label }}
          </v-btn>
        </v-col>
      </div>
    </v-row>
    <v-row>
      <slot />
    </v-row>
  </v-container>
</template>
<script setup lang="ts">
const props = defineProps<{
  tag: string,
  btn?: {label: string, to: string},
}>() 
</script>