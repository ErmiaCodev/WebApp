<template>
	<div class="container mt-5">
		<div class="row">
	     <div class="col d-flex justify-content-center">
	       <b-card
		      style="width: 30rem;"
		      class="mb-2 mt-3"
		    >
	    <b-card-text>
	      <h3 class="text-center"> Register </h3>
	      <hr>
	      <div v-if="status">
	        <div v-if="status == 500">
	           <b-alert show variant="danger">
	              <h5 class="alert-heading">Worng</h5>
	              <hr>
	              <p class="mb-0">
	                Username & Password not Match
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
	          v-model="pass1"
	          placeholder="Password"
	          required
	        ></b-form-input>
	      </b-form-group>
	      <b-form-group
	          id="input-group-2"
	          label="Password Confirm*"
	          label-for="input-2"
	        >
	        <b-form-input
	          id="input-2"
	          type="password"
	          v-model="pass2"
	          placeholder="Password"
	          required
	        ></b-form-input>
	      </b-form-group>
	      <button @click="register()" class="btn btn-block btn-success">
	        Create
	      </button>
	      <hr />
	      <NuxtLink to="/auth/login/" > <p class="text-info"> Already Have An Account? login Here </p> </NuxtLink>
	    </b-card-text>

	  </b-card>

	  
	  </div>

	  </div>
	</div>
</template>

<script>
import axios from 'axios'

	export default {
		data() {
			return {
				username: '',
				pass1: '',
				pass2: '',
				token: '',
				status: null
			}
		},
		methods: {
			register() {
				axios
					.post('/api/register/', {
						username: this.username,
						pass1: this.pass1,
						pass2: this.pass2,
					})
					.then(response => {this.status = response.data.status, this.$router.push("/auth/login")})
			}
		}
	};
</script>