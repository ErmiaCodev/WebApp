<template>
	<div class="bg-white">
		<header style="height: 100vh; min-height: 500px; background-image: url('https://ubuntuhandbook.org/wp-content/uploads/2016/09/Yakkety_Yak_Wallpaper.jpg');background-size: cover; background-position: center; background-repeat: no-repeat;">
		  <div class="container h-100">
		    <div class="row h-100 align-items-center">
		      <div class="col-12 text-center">
		        <h1 class="font-weight-light text-white mb-2">Cat: {{cat}} </h1>
		        <div class="m-5">
		        	<b-form-select v-model="cat" :options="options"></b-form-select>	        	
		        </div>
		      </div>
		    </div>
		  </div>
		</header>
		<div class="container">
			<div class="p-4 bg-white rounded m-3">
				<div>
					<hr >

					<div v-for="post in Categorized">
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
	</div>
</template>

<script>
import axios from 'axios'
	export default {
		data() {
			return {
				options: [
					{'value': 'GnuLinux', 'text': 'Gnu Linux'},
					{'value': 'WebSec', 'text': 'Web Security'},
					{'value': 'WebDevel', 'text': 'Web Development'},

				],
				cat: null,
				posts: []
			}
		},
		mounted() {
			axios
				.get('/api/posts/')
				.then(response => { this.posts = response.data.posts })
		},
		computed: {
			Categorized() {
				if (this.cat == null) {
					return this.posts	
				} else {
					return this.posts.filter(post => post.cat == this.cat)
				}
				
			}
		}
	};
</script>