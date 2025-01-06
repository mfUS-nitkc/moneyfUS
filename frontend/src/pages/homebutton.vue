<template>
    <v-app>
      <v-container>
        <!-- Button Design -->
        <v-row justify="center">
          <v-btn
            class="home-btn"
            elevation="0"
            tile
            outlined
            height="100px"
            width="100px"
          >
            <v-col class="text-center">
              <v-icon class="home-icon" size="36px">mdi-home</v-icon>
              <div class="home-text">HOME</div>
            </v-col>
          </v-btn>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
    export default {
      name: 'HomeButton',
    }
  </script>
  
  <style scoped>
    .home-btn {
      background-color: #d9d9d9; /* Match the grey background color */
      border: 1px solid black; /* Match the black border */
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    .home-icon {
      color: black; /* Black icon color */
    }
  
    .home-text {
      font-size: 14px;
      color: black; /* Black text color */
      font-weight: bold;
      margin-top: 5px; /* Space between icon and text */
    }
  </style>
  