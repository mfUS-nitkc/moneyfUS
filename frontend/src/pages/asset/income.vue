<template>
  <v-container>
    <v-row>
      <asset-income-card>
        <v-card-item>
          <template v-slot:prepend>
            <v-icon icon="mdi-cash"></v-icon>
          </template>
        <v-card-title>
          収入入力
        </v-card-title>
      </v-card-item>
      <v-card-text>
        <v-row align="baseline">
          <v-col cols="9">
            <FormDatePicker v-model="selectedDate" />
          </v-col>
          <v-col cols="3">
            <div style="font-size:1rem">
              の収入
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-0">
            <v-text-field v-model="currentInputIncomeAmount" bg-color="white" type="number" label="収入を入力" />
          </v-col>
        </v-row>
        <v-row justify="end" class="mt-0">
          <v-col cols="auto" class="py-0 d-flex justify-end">
            <v-btn height="1.2rem" >登録</v-btn>
            <!-- TODO: Replace me with miniButton -->
          </v-col>
        </v-row>
        <v-row>
          <v-spacer />
          <div style="font-size: 1.5rem">↓</div>
          <v-spacer />
        </v-row>
        <v-row>
          <v-col class="py-0">
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col>
            <div class="text-h6">
              今月の収入
            </div>
          </v-col>
          <v-col cols="auto" class="d-flex justify-end">
            <div class="text-h5">
              ¥{{ numberToAmountString(123456) }}
            </div>
            </v-col>
          </v-row>
      </v-card-text>
      </asset-income-card>
    </v-row>
    <v-row justify="center">
      <AssetIncomeCard>
        <v-card-item>
          <template v-slot:prepend>
            <v-icon icon="mdi-export-variant"></v-icon>
          </template>
        <v-card-title>
          予算入力
        </v-card-title>
        </v-card-item>
        <v-card-text>
          <v-row>
            <v-col>
              <v-text-field v-model="currentInputBudgetAmount" bg-color="white" type="number" label="予算を入力" />
            </v-col>
        </v-row>
        <v-row>
          <v-col class="d-flex justify-center pt-0">
            <v-btn height="1.2rem" >登録</v-btn>
          </v-col>
        </v-row>
        </v-card-text>
      </AssetIncomeCard>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { numberToAmountString } from '@/libs';

const selectedDate = ref<Date|null>(null)
const currentInputIncomeAmount = ref<number>(0)
const currentInputBudgetAmount = ref<number>(0)
</script>
