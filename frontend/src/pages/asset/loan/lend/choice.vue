<template>
  <LoanBasefield tag="貸す">
    <LoanUserlist :users="users" to="/asset/loan/lend/proceed" @select="selectUser" title="誰に貸しますか？"/>
  </LoanBasefield>
</template>
<script lang="ts" setup>
import type { User, UserId } from '@/types';

const users = ref<User[]>([])

const userStore = useUserStore()
const loanStore = useLoanStore()

onMounted(async () => {
  await userStore.fetchFriendList();
  users.value = userStore.friendList
})

const selectUser = (id: UserId ,user: User) => {
  loanStore.setLendToUser(user);
  console.log(user)
}
</script>
