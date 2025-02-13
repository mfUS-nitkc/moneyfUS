<template>
  <NuxtRouteAnnouncer />
  <v-layout>
    <Navbar />
    <v-main>
      <v-container fluid>
        <slot />
      </v-container>
    </v-main>
    <Footer />
  </v-layout>
</template>
