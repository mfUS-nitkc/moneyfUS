<template>
  <v-container>
    <index-card class="my-5">
      <v-card-title style="font-size: 1rem">今月の家計簿</v-card-title>
      <v-card-text>
        <v-row v-for="log in assetLogs" :key="log.asset_id">
          <v-col cols="4">{{ log.issued_at }}</v-col>
          <v-col cols="4">{{ log.usage_category.usage_category_name }}</v-col>
          <v-col cols="4">{{ log.amount }}</v-col>
        </v-row>
      </v-card-text>
    </index-card>
  </v-container>
</template>
<script setup lang="ts">
import type { AssetLog } from '@/types';

const assetStore = useAssetStore()
const assetLogs = ref<AssetLog[]>([])

onMounted(async () => {
  await assetStore.fetchAssetLogs()
  assetLogs.value = assetStore.assetLogs
})
</script>