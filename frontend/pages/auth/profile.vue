<template>
	<div class="container">
		 <div class="row d-flex justify-content-center">
    	<div class="col-md-10 mt-5 pt-5">
    		<div class="row z-depth-3">
    			<div class="col-sm-4 bg-info rounded">
    				<div class="card-block text-center text-white pt-3">
    					<img src="/media/ca.jpg" alt="Profile" class="img-thumbnail rounded-circle">
    					<h2 class="font-weight-bold mt-4 text-capitalize"> 
                                
                         </h2>
    					<p></p>

    				</div>
    			</div>
    			<div class="col-sm-8 bg-white rounded-right">
    				<h3 class="mt-3 font-Info text-center text-capitalize"> {{id.username}}'s Profile </h3>
    				<hr class="badge-primary mt-0 w-25">
    				
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Name:</p>
    						<h6 class="text-muted"> {{id.name}} </h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">LastName:</p>
    						<h6 class="text-muted"> {{id.lname}} </h6>
    					</div>
    				</div>
    				<hr class="badge-light mt-0">
                    
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Email:</p>
    						<h6 class="text-muted"> {{id.email}} </h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">AvatarName:</p>
    						<h6 class="text-muted"> {{id.avatar}} </h6>
    					</div>
    				</div>
    				<hr class="badge-light mt-0">

                    <br>
                    <br>
                <div class="row mb-3">
                    <div class="col-sm-12">
                    	<NuxtLink to="/auth/logout">
                    		<button class="btn btn-block btn-danger">
	                            logout
	                        </button>
                    	</NuxtLink>
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

				}
			}
		},
		created() {
			if (process.browser) {
				var token = localStorage.getItem('token');
				if (token != null) {
					axios
					.post('/api/getuser/', {
						token: token
					})
					.then(response => this.id = response.data.ID)
				} else {
					this.$router.push("/auth/login")
				}
				
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