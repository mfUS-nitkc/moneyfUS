<template>
    <v-app>
      <v-container
        class="d-flex justify-center align-center"
        style="background-color: #e0e0e0; height: 100vh;"
      >
        <v-card
          outlined
          style="width: 100%; max-width: 414px;" <!-- iPhone screen width -->
        >
          <!-- Title -->
          <v-card-title class="text-center text-h6 font-weight-bold">
            マネーフォワードUS
          </v-card-title>
  
          <!-- Subtitle -->
          <v-card-subtitle class="text-center mb-4">
            <v-icon class="mr-2">mdi-cat</v-icon> ログイン
          </v-card-subtitle>
  
          <!-- Form -->
          <v-card-text>
            <v-form>
              <!-- Email Field -->
              <v-text-field
                label="メールアドレス（ログインID）"
                required
              ></v-text-field>
              <!-- Password Field -->
              <v-text-field
                label="パスワード"
                type="password"
                required
              ></v-text-field>
            </v-form>
          </v-card-text>
  
          <!-- Login Button -->
          <v-card-actions class="justify-center">
            <v-btn
              block
              class="blue-button"
            >
              ログイン
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    data: () => ({}),
  };
  </script>
  
  <style>
  html,
  body,
  #app {
    margin: 0;
    padding: 0;
    height: 100%;
  }
  
  /* Style for Blue Button */
  .blue-button {
    background-color: #2196f3 !important; /* Bright blue */
    color: white !important; /* White text */
    font-weight: bold;
  }
  </style>