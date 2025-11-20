<script lang="ts">
	import SignUpUser from '$lib/components/LoginPages/SignUpUser.svelte';
	import type { ActionData, PageProps } from './$types';

	let { form }: PageProps = $props();

	$effect(() => {
		if (form?.success) {
			window.location.href = '/login';
		}
	});
</script>

<div>
	<SignUpUser></SignUpUser>
</div>
