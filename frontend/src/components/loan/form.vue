<template>
  <v-container>
    <v-card>
      <v-form ref="form" @submit.prevent="submit">

      <v-card-text>
        <v-card flat>
          <v-card-text>
              <form-textfield
                    :rules="[aboveZero]"
                    label="金額を入力"
                    v-model="inputAmount"
                    suffix="円"
                  ></form-textfield>
          </v-card-text>
        </v-card>
        <v-card flat>
          <v-card-text>
            <FormDatePicker v-model="inputDueDate" label="返済予定日">
            </FormDatePicker>
          </v-card-text>
        </v-card>
        <v-row class="d-flex justify-center">
          <v-col cols="auto">
            <FormMiniButton base-color="light-blue-lighten-4" type="submit">決定</FormMiniButton>
          </v-col>
        </v-row>
      </v-card-text>
    </v-form>
    </v-card>
  </v-container>
</template>
<script lang="ts" setup>
import type { NewLoanBase } from '@/types';
import type { VForm } from 'vuetify/components';

const emit = defineEmits<{
  (e: 'submit', value: NewLoanBase): void
}>()

const aboveZero = (v: number) => v > 0 || "1以上を入力してください．";
const inputAmount = ref<number>();
const inputDueDate = ref<Date | null>(null);
const form = ref<InstanceType<typeof VForm> | null>(null)

const submit = async () => {
  if (!form.value?.isValid) {return}

  emit('submit', {amount: inputAmount.value!, due_date: inputDueDate.value!.toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      })
      .split("/")
      .join("-"),} satisfies NewLoanBase)
}
</script>
