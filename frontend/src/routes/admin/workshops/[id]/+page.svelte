<script lang="ts">
	import SessionPageAdmin from '$lib/components/SessionPages/SessionPageAdmin.svelte';



	let { data } = $props();
</script>

<SessionPageAdmin {data}></SessionPageAdmin>
