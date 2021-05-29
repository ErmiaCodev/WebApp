<template>
	<div class="container">
		<div class="row">
	    	<div class="col d-flex justify-content-center">
	    		<b-card
			      style="width: 30rem;"
			      class="mb-2"
			    >
	    			<b-card-text>
	    			</b-card-text>
	    		</b-card>
			</div>
		</div>

	</div>
</template>

<script>
import axios from 'axios'

	export default {
		mounted() {
			if (process.browser) {
				var token = localStorage.getItem('token') 
			}
			
		}
	};
</script>