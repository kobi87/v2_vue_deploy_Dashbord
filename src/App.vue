<template>
  <v-app id="app" 
   >
    <v-app-bar app color="teal lighten-2" dark>
      <v-icon left>mdi-view-dashboard</v-icon>
      <router-link to="/Dashboard"><v-btn text rounded>Dashboard</v-btn></router-link>
      <router-link to="/"><v-btn text rounded>AI</v-btn></router-link> 
      <v-spacer></v-spacer>
      <v-toolbar-title> <img src="./assets/white-labs-plain.png" height="50" />   </v-toolbar-title>
    </v-app-bar>
    <v-content>
      <router-view/>
      <!--<HelloWorld/> -->
    </v-content>
  <v-footer color="teal lighten-3" padless>
    <v-row justify="center" no-gutters >
      <v-btn v-for="link in links" :key="link" color="white" text rounded class="my-2">
        {{ link }}
      </v-btn>
      <v-col class="teal lighten-2 py-4 text-center white--text" cols="12">
        {{ new Date().getFullYear() }} — <strong>© by Bewave</strong>
      </v-col>
    </v-row>
    </v-footer>  
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
    
  },

  data: () => ({
    links: [
        ''
      ],
  }),
};
</script>

<style>
   #app {
     background-image: url('./assets/Home-Wallpaper-9.jpg');
     /* background-color: #8f2c2c; */
    height: 100%;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
  }
</style>
