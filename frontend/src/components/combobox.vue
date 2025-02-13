<template>
    <v-app>
      <v-container>
        <v-combobox
          label="出費の種類"
          :items="['出費全般', '食費', '生活費', '通販', 'その他', '自分で入力']"
          v-model="selectedExpense"
          outlined
        ></v-combobox>
      </v-container>
    </v-app>
  </template>
  
  <script>
    export default {
      data() {
        return {
          selectedExpense: null,
        }
      },
    }
  </script>
  
  <style scoped></style>
  