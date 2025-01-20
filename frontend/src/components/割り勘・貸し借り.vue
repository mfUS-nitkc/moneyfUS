<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="3">
          <v-btn
            class="custom-button"
            :style="{ backgroundColor: '#A8D08D', width: '180px', height: '60px', borderRadius: '8px' }"
            elevation="2"
            outlined
          >
            <v-icon left size="28px" class="custom-icon">
              mdi-scale-balance
            </v-icon>
            <div class="button-text">割り勘・貸し借り</div>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
    export default {
      name: 'SharingAndBorrowingButton',
    }
  </script>
  
  <style scoped>
    .custom-button {
      font-size: 14px;
      font-weight: bold;
      color: white;
      text-transform: none;
      display: flex;
      align-items: center; /* Vertically centers icon and text */
      justify-content: flex-start; /* Ensures left alignment */
      gap: 12px; /* Adds space between the icon and the text */
      padding-left: 12px; /* Adds some left padding for balance */
    }
  
    .custom-icon {
      color: white;
    }
  
    .button-text {
      text-align: left; /* Keeps text left-aligned */
      display: flex;
      flex-direction: column;
      justify-content: center; /* Ensures the text lines are centered vertically */
      line-height: 1.2; /* Sets a good line height for readability */
      font-size: 14px; /* Ensures consistency with button font size */
      margin-left: 8px; /* Adjust spacing between icon and text */
    }
  </style>
  