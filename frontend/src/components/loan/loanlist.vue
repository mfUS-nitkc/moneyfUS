<template>
  <v-container>
    <v-card>
      <v-card-title style="font-size: 1rem;">{{ isLenderView ? '貸している人' : '借りている人' }}</v-card-title>
      <v-list class="scrollable-list">
        <v-list-item
          v-for="loan in loans"
          :key="loan.loan_id"
          @click="handleSelect(loan.loan_id)"
        >
          <v-list-item-title>
            <v-row>
              <v-col cols="6">
                <div style="overflow-x:scroll;">
                  {{ isLenderView ? loan.borrower.username : loan.lender.username }}
                </div>
              </v-col>
              <v-spacer />
              <v-col cols="5" class="text-right">
                {{ numberToAmountString(loan.amount) + ' 円' }}
              </v-col>
            </v-row>
          </v-list-item-title>
          <v-list-item-subtitle>
            返済期限: {{ loan.due_date }}
          </v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import type { Loan } from '@/types';
import { numberToAmountString } from '@/libs';

const { isLenderView = true, ...props } = defineProps<{ loans: Loan[], title: string, to?: string, isLenderView?: boolean }>();

const emit = defineEmits<{ (e: "select", id: string, loan: Loan): void }>();

const handleSelect = (id: string) => {
  const selectedLoan = props.loans.find(loan => loan.loan_id === id);
  if (selectedLoan) {
    emit("select", id, selectedLoan);
  }
};
</script>
