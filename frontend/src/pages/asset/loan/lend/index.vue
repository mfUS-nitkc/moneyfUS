<template>
  <LoanBasefield tag="貸す" :btn="{label: '新規', to: '/asset/loan/lend/choice'}">
    <LoanLoanlist :is-lender-view="true" :loans="lendLoans" @select="selectLoan" title="現在の貸し状況"></LoanLoanlist>
    <v-dialog v-model="isDialogOpen">
      <v-card>
        <v-card-title>
          清算しますか？
        </v-card-title>
        <v-card-text>
          {{ selectedLoan?.borrower.username }} さんから {{ selectedLoan?.amount }} 円を受け取る清算をします．
        </v-card-text>
        <v-card-actions class="d-flex justify-center">
          <v-btn @click="checkoutLoan">
            はい
          </v-btn>
          <v-btn @click="() => isDialogOpen = false">
            いいえ
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </LoanBasefield>
</template>
<script setup lang="ts">
import type { Loan, LoanId } from '@/types';

const lendLoans = ref<Loan[]>([])
const loanStore = useLoanStore()

const isDialogOpen = ref(false)
const selectedLoan = ref<Loan>()

onMounted(async () => {
  const result = await loanStore.getLendList()
  if (result) lendLoans.value = loanStore.lendLoanList
  console.log(result, lendLoans.value)
})

const checkoutLoan = async () => {
  if (selectedLoan.value) 
    await loanStore.postCheckout(selectedLoan.value)
  isDialogOpen.value = false
}

const selectLoan = (id: LoanId, loan: Loan) => {
  selectedLoan.value = loan
  isDialogOpen.value = true
}
</script>