<template>
  <LoanForm @submit="submit">
  </LoanForm>
</template>
<script setup lang="ts">
import type { NewLoanBase, PostLendRequest } from '@/types';

const loanStore = useLoanStore()

const submit = async(value: NewLoanBase) => {
  const lendToUser = loanStore.lendToUser
  if (!lendToUser) {return}
  const request = {
    ...value,
    lend_to_user_id: lendToUser.user_id
  } satisfies PostLendRequest

  const isSuccess = await loanStore.postLend(request)
  if (isSuccess) {
    navigateTo('/asset/loan/lend')
  }
}
</script>