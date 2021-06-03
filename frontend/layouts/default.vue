<template>
  <div>
    <div>
  <b-navbar toggleable="lg" type="dark" style="background-color: #0C4B33">
    <b-navbar-brand href="#">GeekyChunk</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
          <NuxtLink to="/">
            <div class="nav-item">
              <div class="nav-link">
                Home
              </div>
            </div>
          </NuxtLink>
        
          <NuxtLink to="/blog">
            <div class="nav-item">
              <div class="nav-link">
                blog
              </div>
            </div>
          </NuxtLink>

          <NuxtLink to="/message">
            <div class="nav-item">
              <div class="nav-link">
                message
              </div>
            </div>
          </NuxtLink>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>Authentication</em>
          </template>
          <NuxtLink to="/auth/login">
            <div class="dropdown-item">Log</div>
          </NuxtLink>
          <hr>
          <NuxtLink to="/auth/profile">
            <div class="dropdown-item">Profile</div>
          </NuxtLink>
          <NuxtLink to="/auth/logout">
            <div class="dropdown-item">logout</div>
          </NuxtLink>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
    <Nuxt />
  </div>
</template>

<style>
body {
  background-color: #e3e3e3;
}
</style>