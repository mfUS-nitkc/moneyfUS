<template>
  <v-container fluid>
    <v-card>
      <v-card-title style="font-size: 1rem;">ユーザーを選択</v-card-title>
      <v-list class="scrollable-list">
        <v-list-item v-for="item in items" :key="item.id">
          <template v-slot:prepend>
            <v-icon>mdi-account</v-icon>
          </template>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
          <v-list-item-subtitle v-if="item.subtitle">{{ item.subtitle }}</v-list-item-subtitle>
          <template v-slot:append>
            <v-btn v-if="modelValue.has(item.id)" color="primary" @click="unselectUser(item.id)">解除</v-btn>
            <v-btn v-else color="primary" @click="selectUser(item)">選択</v-btn>
          </template>
        </v-list-item>
      </v-list>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
interface ListItem {
  id: string;
  title: string;
  subtitle?: string;
}

const props = defineProps<{
  items: ListItem[];
  modelValue: Map<string, ListItem>; // v-model 用のデータ
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: Map<string, ListItem>): void;
}>();

const selectUser = (user: ListItem) => {
  const newSelection = new Map(props.modelValue);
  newSelection.set(user.id, user);
  emit('update:modelValue', newSelection);
};

const unselectUser = (id: string) => {
  const newSelection = new Map(props.modelValue);
  newSelection.delete(id);
  emit('update:modelValue', newSelection);
};
</script>

<style scoped>
.scrollable-list {
  max-height: 60vh;
  overflow-y: auto;
}
</style>
