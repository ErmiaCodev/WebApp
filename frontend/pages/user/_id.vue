<template>
	<div>
		<div class="container mt-2">
		<!-- <div v-if="status" class="bg-white">
    			<div v-if="status == 200" class="alert alert-success">
    				Saved				
    			</div>
    	</div> -->
		 <div class="row d-flex justify-content-center">
		 	
    		<div class="col-md-10 mt-2 pt-5">

    		<div class="row z-depth-3">
    			<div class="col-sm-4 bg-info rounded">
    				<div class="card-block text-center text-white pt-3">
    					<img src="/media/ca.jpg" alt="Profile" class="img-thumbnail rounded-circle">
    					<h2 class="font-weight-bold mt-4 text-capitalize"> 
                             {{prof.name}}  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
  <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
</svg>
                         </h2>
    					<p>
    						See UR Friend's Profile
    					</p>

    				</div>
    			</div>
    			<div class="col-sm-8 bg-white rounded-right">
    				<h3 class="mt-3 font-Info text-center text-capitalize"> {{prof.username}}'s Profile </h3>
    				<hr class="badge-primary mt-0 w-25">
    				
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Name:</p>
    						<h6 class="text-muted">
    							{{prof.name}}
    						</h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">LastName:</p>
    						<h6 class="text-muted">
    							{{prof.lname}}
    						</h6>
    					</div>
    				</div>
    				<hr class="badge-light mt-0">
                    
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Email:</p>
    						<h6 class="text-info">
    							<b><i>Hide Due Privacy</i></b>
    						</h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">AvatarName:</p>
    						<h6 class="text-muted">
    							{{prof.avatar}}
    						</h6>
    					</div>
    				</div>
    				<hr class="badge-light mt-0">


                <div class="row mb-3 mt-2">
                    <div class="col-sm-12">
	                    <button class="btn btn-block btn-danger">
	                		Message
	                    </button>
                    </div>
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
				prof: {
				}
			}
		},
		created() {
			axios.get('/api/getuser/' + this.$route.params.id)
			.then(response => this.prof = response.data)
		}
	};
</script>
