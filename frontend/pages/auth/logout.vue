<template>
	<div class="container mt-3 bg-white p-5">
		
		<div class="row">
			<div class="col d-flex justify-content-center">
				<b-alert show variant="success">
					<h5 class="alert-heading">Success</h5>
		              <hr>
		              <p class="mb-0">
		                Successfully Loged Out From Your Account
		              </p>
				</b-alert>
			</div>
		</div>

	</div>
</template>

<script>
	export default {
		created() {
			if (process.browser) {
				localStorage.removeItem('token')
			}
		}
	};
</script>