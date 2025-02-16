<template>
  <v-container>
    <v-card>
      <v-card-title>割り勘設定</v-card-title>
      <v-card-text>
        <v-text-field v-model.number="totalAmount" label="合計金額" type="number" @update:modelValue="recalculate" />
        <v-list>
          <v-list-item v-for="(amount, userId) in amounts" :key="userId">
            <v-list-item-content>
              <v-list-item-title>{{ selectedUsers.find((user) => user.id === userId)?.title }}</v-list-item-title>
              <v-text-field 
                :model-value="amounts[userId]"
                type="number"
                :disabled="lockedUsers.has(userId)"
                @blur="lockUser(userId)"
                @input="setAmount(userId, $event)"
              />
              <v-btn v-if="lockedUsers.has(userId)" color="error" small @click="unlockUser(userId)">解除</v-btn>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider />
        <v-row justify="space-between" align="center" class="mt-4">
          <v-col>Total: ¥{{ computedTotal }}</v-col>
          <v-spacer />
          <v-col>
            <v-btn color="success" @click="submitSplit">割り勘を確定</v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import type { PostSplitRequest } from '@/types';

const loanStore = useLoanStore();
const router = useRouter();

// 合計金額
const totalAmount = ref(0);
// 割り勘額
const amounts = reactive<Record<string, number>>({});
// 固定されたユーザー
const lockedUsers = ref(new Set<string>());

const selectedUsers = computed(() => Array.from(loanStore.splitSelectedUserList.values()));

// 割り勘金額の再計算
const recalculate = (newTotal: number) => {
  const lockedTotal = Array.from(lockedUsers.value).reduce((sum, id) => sum + (amounts[id] || 0), 0);
  const remainingUsers = selectedUsers.value.filter(u => !lockedUsers.value.has(u.id));
  const newAmount = remainingUsers.length > 0 ? Math.floor((newTotal - lockedTotal) / remainingUsers.length) : 0;

  remainingUsers.forEach(user => amounts[user.id] = newAmount);
};

// **合計金額が変更されたら再計算**（ただし、ユーザーが手動変更した場合は影響しない）
watch(totalAmount, (newTotal) => {
  recalculate(newTotal);
}, { immediate: true });

const setAmount = (userId: string, event: Event) => {
  const value = Number((event.target as HTMLInputElement).value);
  amounts[userId] = value;
};

// **合計金額を手動変更した場合は他の金額に影響を与えない**
watch(() => Object.values(amounts), (newValues) => {
  // `amounts` の合計と `totalAmount` がズレている場合は変更しない
  const sum = newValues.reduce((a, b) => a + b, 0);
  if (sum !== totalAmount.value) return;
}, { deep: true });

// 特定ユーザーの金額をロック
const lockUser = (userId: string) => {
  lockedUsers.value.add(userId);
  recalculate(totalAmount.value)
};

// ロック解除
const unlockUser = (userId: string) => {
  lockedUsers.value.delete(userId);
  recalculate(totalAmount.value);
};

// 合計金額を算出
const computedTotal = computed(() => Object.values(amounts).reduce((sum, val) => sum + val, 0));

// 割り勘を確定
const submitSplit = async () => {
  console.log("割り勘データ送信", amounts);
  const participants = Object.entries(amounts).map(([k,v]) => ({
    participant_id: k,
    amount: v
  }))
  const req = {
    total_amount: computedTotal.value,
    participants,
    description: "",
    due_date: "2025-03-01",
  } satisfies PostSplitRequest
  const isSuccess = await loanStore.postSplit(req)
  if (isSuccess) navigateTo("/asset/loan")
};
</script>
