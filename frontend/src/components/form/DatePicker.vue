<template>
  <FormInputElement :label="label">
    <v-menu v-model="menu" :close-on-content-click="false" transition="scale-transition" offset-y min-width="auto">
      <template v-slot:activator="{ props }">
        <v-text-field
        v-bind="props"
        :model-value="formattedDate"
        label="日付を選択"
        readonly
        variant="outlined"
        prepend-inner-icon="mdi-calendar"
        bg-color="white"
        ></v-text-field>
      </template>
      <v-date-picker
      v-model="selectedDate"
      @update:model-value="emitDate"
      ></v-date-picker>
    </v-menu>
  </FormInputElement>
</template>

<script setup lang="ts">
// 親コンポーネントから受け取る日付
const props = defineProps<{ label?: string, modelValue: Date | null }>();

// 親コンポーネントに値を渡す
const emit = defineEmits<{ (event: 'update:modelValue', value: Date | null): void }>();

// 選択された日付（内部状態）
const selectedDate = ref<Date | null>(props.modelValue ?? null);
// メニュー開閉状態
const menu = ref<boolean>(false);

// `modelValue` が変更されたときに `selectedDate` も更新
watch(() => props.modelValue, (newValue) => {
  selectedDate.value = newValue ?? null;
});

// YYYY-MM-DD → YYYY年MM月DD日 に変換する（`null` チェックを追加）
const formattedDate = computed(() => {
  if (!selectedDate.value) return ""; // `null` の場合は空文字
  const date = selectedDate.value.toLocaleDateString()
  return date
});

// 親コンポーネントに値を渡す
const emitDate = (date: Date | null) => {
  selectedDate.value = date;
  emit('update:modelValue', date);
  menu.value = false; // 日付を選択したらピッカーを閉じる
};
</script>
