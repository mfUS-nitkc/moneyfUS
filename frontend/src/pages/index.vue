<template>
  <v-container>
    <index-card class="my-5">
      <v-card-title style="font-size: 1rem">今月の家計簿</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="6"></v-col>
          <v-col cols="6"></v-col>
        </v-row>
      </v-card-text>
    </index-card>
    <index-card class="my-5">
      <v-card-title style="font-size: 1rem;">直近のメッセージ</v-card-title>
      <v-card-text>
        <v-text-field disabled v-for="notify in notifies" :key="notify.notify_id" v-model="notify.content"></v-text-field>
      </v-card-text>
    </index-card>
  </v-container>
</template>

<script lang="ts" setup>
import type { Notify } from '@/types';

definePageMeta({
  middleware: "auth"
})

const notifies = ref<Notify[]>()

const notifyStore = useUserStore()

onMounted(async () => {
  await notifyStore.fetchNotifyList()
  notifies.value = notifyStore.notifyList.slice(0, 2)
})
</script>
