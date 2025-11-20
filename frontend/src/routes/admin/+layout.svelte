<script lang="ts">
	import '../../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { openModal } from '$lib/stores/OpenModal.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';
	import { fetchActiveUser } from '$lib/api/api';
	import HeaderUserTabs from '$lib/components/Header/HeaderUserTabs.svelte';
	import HeaderAdminTabs from '$lib/components/Header/HeaderAdminTabs.svelte';

	let { children, data } = $props();
	function reroute(href: string) {
		openModal.state = false;
		window.location.href = href;
	}

	let isLoading = $state(true);

	onMount(async () => {
		const img = new Image();
		const user = await fetchActiveUser();
		isLoading = false;

		img.src = '/assets/pastel1.jpg';
		img.onload = function () {
			document.body.style.backgroundImage = 'url(' + img.src + ')';
			document.body.style.backgroundSize = 'cover';
			document.body.style.backgroundPosition = 'center';
			document.body.style.backgroundAttachment = 'fixed';
		};
	});
</script>

{#if openModal.state}
	<Modal {reroute} />
{/if}

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if isLoading}
	<div class="flex h-screen items-center justify-center">
		<div class="m-auto">
			<div
				class="loader h-64 w-64 rounded-full border-8 border-t-8 border-gray-200 ease-linear"
			></div>
		</div>
	</div>
{:else}
	<HeaderAdminTabs />
	{@render children()}
{/if}
