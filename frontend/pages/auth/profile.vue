<template>
	<div class="container">
		 <div class="row d-flex justify-content-center">
    	<div class="col-md-10 mt-5 pt-5">
    		<div class="row z-depth-3">
    			<div class="col-sm-4 bg-info rounded">
    				<div class="card-block text-center text-white pt-3">
    					<img src="/media/ca.jpg" alt="Profile" class="img-thumbnail rounded-circle">
    					<h2 class="font-weight-bold mt-4 text-capitalize"> 
                              {{id.username}}  <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
</svg> 
                         </h2>
    					<p> {{status}} </p>

    				</div>
    			</div>
    			<div class="col-sm-8 bg-white rounded-right">
    				<h3 class="mt-3 font-Info text-center text-capitalize"> {{id.username}}'s Profile </h3>
    				<hr class="badge-primary mt-0 w-25">
    				
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Name:</p>
    						<h6 class="text-muted"> 
    							<input v-model="id.name" type="text" class="form-control">
    						</h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">LastName:</p>
    						<h6 class="text-muted"> 
    							<input v-model="id.lname" type="text" class="form-control">
    						</h6>
    					</div>
    				</div>
    				<hr class="badge-light mt-0">
                    
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Email:</p>
    						<h6 class="text-muted">
    							<input v-model="id.email" type="text" class="form-control">
    						</h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">AvatarName:</p>
    						<input v-model="id.avatar" type="text" class="form-control">
    					</div>
    				</div>

                <div class="row mb-3 mt-2">
                    <div class="col-sm-12">
                    	<button @click="Save" class="btn btn-block btn-success">
	                            Save
	                    </button>
	                    <button @click="Discard" class="btn btn-block btn-danger">
	                            Discard
	                    </button>
                    </div>
                </div>
    			</div>

    			</div>
    			
    		</div>
    	</div>
    </div>

	</div>
</template>

<script>
import axios from 'axios'

	export default {
		data() {
			return {
				id: {

				},
				name: null,
				lname: null,
				email: null,
				avatar: null,
				token: null,
				status: null
			}
		},
		created() {
			if (process.browser) {
				var token = localStorage.getItem('token');
				this.token = token;
				if (token != null) {
					axios.post('/api/getuser/', {
						token: token
					})
					.then(response => this.id = response.data.ID)
				} else {
					this.$router.push("/auth/login")
				}
				
			}
		},
		methods: {
			Save() {
				axios.post('/api/edituser/', {
					token: this.token,
					name: this.id.name,
					lname: this.id.lname,
					email: this.id.email,
					avatar: this.id.avatar
				})
				.then(response => this.status = response.data)
			},
			Discard() {
				axios.post('/api/getuser/', {
					token: this.token
				})
				.then(response => this.id = response.data.ID)
			}
		}
	};
</script>

<style>

.font-Info {
	font-family: 'Brush Script MT';
	font-style: italic;
}	

</style>