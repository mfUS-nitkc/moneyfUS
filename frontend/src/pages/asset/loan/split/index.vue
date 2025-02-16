<template>
  <LoanBasefield tag="割り勘" :btn="{to: '/asset/loan/split/proceed', label: '作る'}">
    <LoanUserselectlist v-model="selectedUsers" :items="listItems"></LoanUserselectlist>
  </LoanBasefield>
</template>
<script lang="ts" setup>
import type { User, UserId } from '@/types';

const users = ref<User[]>([])
const selectedUsers = ref(new Map<string, { id: string; title: string }>());

const userStore = useUserStore()
const loanStore = useLoanStore()

onMounted(async () => {
  await userStore.fetchFriendList();
  users.value = userStore.friendList
})

const listItems = computed(() => users.value.map(user => ({
  id: user.user_id,
  title: user.username,
  subtitle: "あなたのともだち"
})));

watch(selectedUsers, (newSelection) => {
  loanStore.splitSelectedUserList = newSelection
}, {deep:true})
</script>
