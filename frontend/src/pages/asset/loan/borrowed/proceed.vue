<template>
  <LoanForm @submit="submit">
  </LoanForm>
</template>
<script setup lang="ts">
import type { NewLoanBase, PostBorrowedRequest } from '@/types';

const loanStore = useLoanStore()

const submit = async(value: NewLoanBase) => {
  const borrowedByUser = loanStore.borrowedByUser
  if (!borrowedByUser) {return}
  const request = {
    ...value,
    borrowed_by_user_id: borrowedByUser.user_id
  } satisfies PostBorrowedRequest

  const isSuccess = await loanStore.postBorrowed(request)
  if (isSuccess) {
    navigateTo('/asset/loan/borrowed')
  }
}
</script>