<template>
	<div class="container-fluid p-5 bg-white">
		<div class="container">
			<h1 class="text-center"> Blog </h1>

			<div>
				<br>

				<div v-for="post in posts">
					<NuxtLink :to="/blog/ + post.slug" class="text-info">
						<h2> {{post.title}} </h2>
						<p class="text-truncate text-info mb-0 pb-0"> {{post.description}} </p>
					</NuxtLink>
					<span class="text-muted"> By <i>{{post.author}}</i> </span>
					<hr class="badge-light" >
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
				posts: null
			}
		},
		created() {
			axios
				.get('/api/posts/')
				.then(response => {this.posts = response.data.posts})
		}
	};
</script>

<style>
	a:hover {
		text-decoration: none !important;
	}
</style>
