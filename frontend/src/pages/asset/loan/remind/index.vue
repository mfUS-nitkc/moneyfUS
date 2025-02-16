<template>
  <LoanBasefield tag="催促">
    <LoanLoanlist :is-lender-view="true" :loans="lendLoans" @select="selectLoan" title="現在の貸し状況"></LoanLoanlist>
    <v-dialog v-model="isDialogOpen">
      <v-card>
        <v-card-title>
          催促しますか？
        </v-card-title>
        <v-card-text>
          {{ selectedLoan?.borrower.username }} さんに {{ selectedLoan?.amount }} 円の催促をします．
        </v-card-text>
        <v-card-actions class="d-flex justify-center">
          <v-btn @click="sendNotify">
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
const selectedLoan = ref<Loan>()

const isDialogOpen = ref<boolean>(false)

onMounted(async () => {
  const result = await loanStore.getLendList()
  if (result) lendLoans.value = loanStore.lendLoanList
  console.log(result, lendLoans.value)
})

const selectLoan = async (id: LoanId, loan: Loan) => {
  selectedLoan.value = loan
  isDialogOpen.value = true
}

const sendNotify = async () => {
  if (selectedLoan.value)
    await loanStore.postLoanNotify(selectedLoan.value)
  isDialogOpen.value = false
}
</script>