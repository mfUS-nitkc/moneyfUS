<template>
    <v-app>
      <v-container>
        <!-- Button Design -->
        <v-row justify="center">
          <v-btn
            class="post-btn"
            elevation="0"
            tile
            outlined
            height="100px"
            width="100px"
          >
            <v-col class="text-center">
              <v-icon class="post-icon" size="36px">mdi-account-group-outline</v-icon>
              <div class="post-text">投稿</div>
            </v-col>
          </v-btn>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    name: "PostButton",
  };
  </script>
  
  <style scoped>
  .post-btn {
    background-color: #d9d9d9; /* Light grey background */
    border: 1px solid black; /* Black border */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .post-icon {
    color: black; /* Black icon color */
  }
  
  .post-text {
    font-size: 14px; /* Match the size of "投稿" text */
    color: black; /* Black text color */
    font-weight: bold;
    margin-top: 5px; /* Space between icon and text */
  }
  </style>