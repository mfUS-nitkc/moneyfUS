<template>
  <NuxtRouteAnnouncer />
  <v-layout>
    <Navbar />
    <v-main>
      <v-container fluid style="height: calc(100vh - 160px); overflow-y: scroll">
        <slot />
      </v-container>
    </v-main>
    <Footer />
  </v-layout>
</template>
