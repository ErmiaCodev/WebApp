<template>
  <div class="container p-3">
   <div class="row">
     <div class="col d-flex justify-content-center">
       <b-card
        style="width: 30rem;"
        class="mb-2 mt-5"
      >
    <b-card-text>
      <h3 class="text-center"> Login </h3>
      <hr>
      <div v-if="status">
        <div v-if="status == 200">
          {{ this.$router.push("/auth/profile") }}
        </div>
        <div v-if="status == 500">
           <b-alert show variant="danger">
              <h5 class="alert-heading">Worng</h5>
              <hr>
              <p class="mb-0">
                Make Sure Username & PassWord. is correct
              </p>
            </b-alert>
        </div>
        <div v-if="status == 502">
           <b-alert show variant="warning">
              <h5 class="alert-heading">Warn</h5>
              <hr>
              <p class="mb-0">
                Not Valid User Or Empty Field!
              </p>
            </b-alert>
        </div>
      </div>
       <b-form-group
          id="input-group-1"
          label="Username*"
          label-for="input-1"
        >
        <b-form-input
          id="input-1"
          type="text"
          v-model="username"
          placeholder="Username"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group
          id="input-group-2"
          label="Password*"
          label-for="input-2"
        >
        <b-form-input
          id="input-2"
          type="password"
          v-model="pass"
          placeholder="Password"
          required
        ></b-form-input>
      </b-form-group>
      <button @click="login()" class="btn btn-block btn-success">
        Login
      </button>
      <hr />
      <NuxtLink to="/auth/register/" > <p class="text-info"> No Account ? Register Here </p> </NuxtLink>
    </b-card-text>

  </b-card>

  
  </div>

  </div>
    
    
  </div>
</template>

<script>
import axios from 'axios'

// Extra Functions

function validate(data) {
 if (data.status == 200) {
  localStorage.setItem("token", data.token)

  return 200
 } else if (data.status == 502) {
  return 502
 } else {
  return 500
 }
}

export default {
  data() {
    return {
      username: '',
      pass: '',
      token: '',
      status: null,
    }
  },
  methods: {
    login() {
      axios
      .post('/api/login/', {
        username: this.username,
        pass: this.pass
      })
      .then(response => {this.status = validate(response.data), n = response.data.status})
    }
  },
  created() {
    if (process.browser) {
      this.token = localStorage.getItem('token')
    }
  }
};
</script>