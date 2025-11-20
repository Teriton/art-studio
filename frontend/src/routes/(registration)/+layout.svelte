<script lang="ts">
	import '../../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import { onMount } from 'svelte';

	let { children } = $props();
	onMount(() => {
		const img = new Image();
		img.src = '/assets/reg_back.jpg';
		img.onload = function () {
			document.body.style.backgroundImage = 'url(' + img.src + ')';
			document.body.style.backgroundSize = 'cover';
			document.body.style.backgroundPosition = 'center';
			document.body.style.backgroundAttachment = 'fixed';
		};
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<SectionWraper>
	<div class="flex h-screen items-center justify-center">
		<div class="m-auto">
			{@render children()}
		</div>
	</div>
</SectionWraper>
