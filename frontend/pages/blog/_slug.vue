<template>
	<div class="container bg-white mt-3 p-4 rounded">
		<div class="text-center mt-0 pb-2">
          
            
			<div class="">
				<img :src="post.thumbnail" alt="test" style="width: 100%" class="img-thumbnail img-responsive">
				<h2 class="text-center mt-3 font-weight-bold"> {{post.title}} </h2>
				<h5 class="text-center text-muted mt-5 mb-5"> {{post.description}} </h5>
				<hr class="badge-light">
				<div class="text-left">
					{{post.body}}
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
				media: '/media/',
				post: {

				}
			}
		},
		created() {
			axios
				.get('/api/post/' + this.$route.params.slug)
				.then(response => this.post = response.data.post)
				.then(function resp() {
					this.post.body = this.post.body.replace("\r", '<br>')
				})

		},
		mounted() {

		}
	};
</script>