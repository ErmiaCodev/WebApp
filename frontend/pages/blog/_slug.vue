<template>
	<div class="">
		<header :style="part1 + post.thumbnail + part2">
		  <div class="container h-100">
		    <div class="row h-100 align-items-center">
		      <div class="col-12 text-center">
		        <h1 class="title font-weight-light text-white mb-2">{{post.title}} </h1>
		        <h5 class="text-white"> {{post.description}} </h5>
		      </div>
		    </div>
		  </div>
		</header>	
		<div class="container">
			<div class="bg-white p-3 m-2">
				<h2 class="text-center">
					{{post.title}}
				</h2>
				<h5>
					{{post.body}}
				</h5>
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
				part1: "height: 100vh; min-height: 5; background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('",
				part2: "'); background-size: cover; background-position: center; background-repeat: no-repeat;",
				post: {

				},
				test: '/media/ca.jpg'
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