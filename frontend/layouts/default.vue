<template>
  <v-app dark>
  <nav>
     <v-toolbar >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>X Army</v-toolbar-title>

      <v-spacer></v-spacer>

      <h4>
       X-Army
      </h4>
    </v-toolbar>
  </nav>
  <div class="mt-5">
    <Nuxt />
  </div>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>
