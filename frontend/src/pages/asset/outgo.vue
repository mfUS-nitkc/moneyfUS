<template>
  <v-container>
    <v-row>
      <asset-outgo-card>
        <v-card-item>
          <template v-slot:prepend>
            <v-icon icon="mdi-keyboard-outline"></v-icon>
          </template>
          <v-card-title> 手動で入力 </v-card-title>
        </v-card-item>
        <v-card-text>
          <v-form ref="form" @submit.prevent="submit">
            <v-container>
              <v-row>
                <v-col>
                  <form-select
                    :rules="[required]"
                    v-model="selectedCategory"
                    label="種類を選択"
                    :items="usageCategoryComputed"
                  ></form-select>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <form-textfield
                    :rules="[aboveZero]"
                    label="金額を入力"
                    v-model="inputAmount"
                    type="string"
                    suffix="円"
                  ></form-textfield>
                </v-col>
              </v-row>
              <v-row justify="center">
                <v-col cols="auto">
                  <FormMiniButton
                    type="submit"
                    :disable="isProgress"
                    :loading="isProgress"
                  >
                    登録
                  </FormMiniButton>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
      </asset-outgo-card>
    </v-row>
  </v-container>
</template>
<script setup lang="ts">
import type { PostAssetRequestById, UsageCategory } from "@/types";
import type { VForm } from "vuetify/components";
const assetStore = useAssetStore();

const required = (v: any) => !!v || "必須項目です．";
const aboveZero = (v: number) => v >= 0 || "0以上を入力してください．";

const isProgress = ref(false);

const submit = async () => {
  if (!form.value?.isValid) return;
  isProgress.value = true;

  const newRequest: PostAssetRequestById = {
    issued_at: new Date()
      .toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      })
      .split("/")
      .join("-"),
    usage_category_id: selectedCategory.value.value,
    amount: inputAmount.value!,
  };
  await assetStore.postAsset(newRequest).then((result) => {
    if (result) form.value?.reset();
    isProgress.value = false;
  });
};

const usageCategoryComputed = computed(() => {
  return usageCategory.value.map((usageCategory) => {
    return {title: usageCategory.usage_category_name,
    value: usageCategory.usage_category_id}
  })
})

onMounted(async() => {
  await assetStore.fetchUsageCategory();
  usageCategory.value = assetStore.usageCategories
  console.log(usageCategory)
})

const form = ref<InstanceType<typeof VForm> | null>(null);
const usageCategory = ref<UsageCategory[]>([]);
const selectedCategory = ref();
const inputAmount = ref<number>();
</script>
