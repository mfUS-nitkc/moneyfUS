<template>
    <v-app>
      <v-container>
        <!-- Button Design -->
        <v-row justify="center">
          <v-btn
            class="expense-btn"
            elevation="0"
            tile
            outlined
            height="100px"
            width="100px"
          >
            <v-col class="text-center">
              <v-icon class="expense-icon" size="36px"
                >mdi-piggy-bank-outline</v-icon
              >
              <div class="expense-text">支出入力</div>
            </v-col>
          </v-btn>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
    export default {
      name: 'ExpenseButton',
    }
  </script>
  
  <style scoped>
    .expense-btn {
      background-color: #d9d9d9; /* Light grey background */
      border: 1px solid black; /* Black border */
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    .expense-icon {
      color: black; /* Black icon color */
    }
  
    .expense-text {
      font-size: 14px; /* Match the size of "支出入力" text */
      color: black; /* Black text color */
      font-weight: bold;
      margin-top: 5px; /* Space between icon and text */
    }
  </style>
  