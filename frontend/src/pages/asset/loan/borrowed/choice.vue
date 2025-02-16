<template>
  <LoanBasefield tag="借りる">
    <LoanUserlist to="/asset/loan/borrowed/proceed" :users="users" @select="selectUser" title="誰から借りますか？"/>
  </LoanBasefield>
</template>
<script lang="ts" setup>
import type { User, UserId } from '@/types';

const users = ref<User[]>([])

const userStore = useUserStore()
const loanStore = useLoanStore()

onMounted(async () => {
  await userStore.fetchFriendList();
  users.value = userStore.friendList || []
})

const selectUser = (id: UserId ,user: User) => {
  loanStore.setBorrowedByUser(user);
  console.log(user)
}
</script>
