<script>
	import { logoutUser } from '$lib/api/api';
	import { onMount } from 'svelte';

	onMount(async () => {
		await logoutUser();
		location.href = '/';
	});
</script>

<div></div>
