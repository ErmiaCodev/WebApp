<template>
	<div>
		


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