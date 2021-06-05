<template>
	<div class="">
		<header class="masthead" :style="part1 + post.thumbnail + part2">
            <div class="container position-relative px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="post-heading">
                            <h1> {{post.title}} </h1>
                            <h2 class="subheading"> {{post.description}} </h2>
                            <span class="meta">
                                Posted by
                                <a href="#!" v-text="post.author" />
                                on August 24, 2021
                            </span>
                        </div>
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
import axios from 'axios';

	export default {
		data() {
			return {
				media: '/media/',
				part1: "background-image: url('",
				part2: "')",
				post: {

				},
				test: '/media/ca.jpg'
			}
		},
		mounted() {
			axios
				.get('/api/post/' + this.$route.params.slug)
				.then(response => this.post = response.data.post)
		},
	};
</script>

<style>
header.masthead {
  position: relative;
  margin-bottom: 3rem;
  padding-top: calc(8rem + 57px);
  padding-bottom: 8rem;
  background: no-repeat center center;
  background-color: #6c757d;
  background-size: cover;
  background-attachment: scroll;
}
header.masthead:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #212529;
  opacity: 0.5;
}
header.masthead .page-heading,
header.masthead .post-heading,
header.masthead .site-heading {
  color: #fff;
}
header.masthead .page-heading,
header.masthead .site-heading {
  text-align: center;
}
header.masthead .page-heading h1, header.masthead .page-heading .h1,
header.masthead .site-heading h1,
header.masthead .site-heading .h1 {
  font-size: 3rem;
}
header.masthead .page-heading .subheading,
header.masthead .site-heading .subheading {
  font-size: 1.5rem;
  font-weight: 300;
  line-height: 1.1;
  display: block;
  margin-top: 0.625rem;
  font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
header.masthead .post-heading h1, header.masthead .post-heading .h1 {
  font-size: 2.25rem;
}
header.masthead .post-heading .meta,
header.masthead .post-heading .subheading {
  line-height: 1.1;
  display: block;
}
header.masthead .post-heading .subheading {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0.75rem 0 2rem;
  font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
header.masthead .post-heading .meta {
  font-size: 1.25rem;
  font-weight: 300;
  font-style: italic;
  font-family: "Lora", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
header.masthead .post-heading .meta a {
  color: #fff;
}
@media (min-width: 992px) {
  header.masthead {
    padding-top: 12.5rem;
    padding-bottom: 12.5rem;
  }
  header.masthead .page-heading h1, header.masthead .page-heading .h1,
header.masthead .site-heading h1,
header.masthead .site-heading .h1 {
    font-size: 5rem;
  }
  header.masthead .post-heading h1, header.masthead .post-heading .h1 {
    font-size: 3.5rem;
  }
  header.masthead .post-heading .subheading {
    font-size: 1.875rem;
  }
}
</style>