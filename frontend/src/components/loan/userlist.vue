<template>
  <LoanBaselist :to="to" :title="title" :items="listItems" @select="handleSelect" />
</template>

<script setup lang="ts">
import type { User } from '@/types';

const props = defineProps<{ users: User[], title: string, to: string }>();

// User[] → BaseList 用の { id, title }[] に変換
const listItems = computed(() => props.users.map(user => ({
  id: user.user_id,
  title: user.username,
  subtitle: "あなたのともだち"
})));

const emit = defineEmits<{ (e: "select", id: string, user: User): void }>();

const handleSelect = (id: string) => {
  const selectedUser = props.users.find(user => user.user_id === id);
  if (selectedUser) {
    emit("select", id, selectedUser);
  }
};
</script>
