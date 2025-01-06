<template>
    <v-app>
      <v-container>
        <!-- Button Design -->
        <v-row justify="center">
          <v-btn
            class="budget-btn"
            elevation="0"
            tile
            outlined
            height="100px"
            width="100px"
          >
            <v-col class="text-center">
              <v-icon class="budget-icon" size="36px">mdi-notebook-edit-outline</v-icon>
              <div class="budget-text">家計簿</div>
            </v-col>
          </v-btn>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    name: "BudgetButton",
  };
  </script>
  
  <style scoped>
  .budget-btn {
    background-color: #d9d9d9; /* Light grey background */
    border: 1px solid black; /* Black border */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .budget-icon {
    color: black; /* Black icon color */
  }
  
  .budget-text {
    font-size: 14px; /* Match the size of "家計簿" text */
    color: black; /* Black text color */
    font-weight: bold;
    margin-top: 5px; /* Space between icon and text */
  }
  </style>