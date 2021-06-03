<template>
	<div class="bg-white">
		<header style="height: 100vh; min-height: 5; background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/static/assets/img/home.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;">
		  <div class="container h-100">
		    <div class="row h-100 align-items-center">
		      <div class="col-12 text-center">
		        <h1 class="title font-weight-light text-white mb-2"> Geeky Blog </h1>
		        <h6 class="text-white"> <NuxtLink to="/blog/cat"> <span class="text-white"> Categorize  </span> </NuxtLink> - <NuxtLink to="/blog/cat"> <span class="text-white"> Search  </span> </NuxtLink> </h6>
		      </div>
		    </div>
		  </div>
		</header>
		<div class="container mt-3">
			<br>
			<div>
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
		mounted() {
			axios.get('/api/posts')
				.then(response => this.posts = response.data.posts)
		}
	};
</script>

<style>
	a:hover {
		text-decoration: none !important;
	}
</style>
