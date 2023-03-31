<template>
  <v-app>
    <v-app-bar
      app
      color="white"
      dark
    >
      <img class="img-logo" src="@/assets/logo.png" alt="logo haas" />
      <v-app-bar-nav-icon color="black"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon color="black">mdi-message-text</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon color="black" x-large>mdi-account</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main class="bg-color">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style scoped>
.img-logo {
  min-width: 180px;
}
.bg-color{
  background-color: rgb(224, 223, 223);
  margin-top: 17px;
}
</style>