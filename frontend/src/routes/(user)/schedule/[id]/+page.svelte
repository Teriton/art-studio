<script lang="ts">
	import SessionPage from '$lib/components/SessionPages/SessionPage.svelte';


	let { data } = $props();
</script>

<SessionPage {data}></SessionPage>

