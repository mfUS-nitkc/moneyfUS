<template>
  <LoanBasefield tag="借りる" :btn="{label: '新規', to: '/asset/loan/borrowed/choice'}">
    <LoanLoanlist :is-lender-view="false" :loans="borrowedLoans" @select="selectLoan" title="現在の借り状況"></LoanLoanlist>
  </LoanBasefield>
</template>
<script setup lang="ts">
import type { Loan, LoanId } from '@/types';

const borrowedLoans = ref<Loan[]>([])
const loanStore = useLoanStore()

onMounted(async () => {
  const result = await loanStore.getBorrowedList()
  if (result) borrowedLoans.value = loanStore.borrowedLoanList
  console.log(result, borrowedLoans.value)
})

const selectLoan = (id: LoanId, loan: Loan) => {
  console.log(loan)
}
</script>