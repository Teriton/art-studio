<script lang="ts">
	import '../../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import Header from '$lib/components/Header/Header.svelte';
	import { openModal } from '$lib/stores/OpenModal.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';
	import { userRole } from '$lib/stores/UserRole.svelte';
	import { fetchActiveUser } from '$lib/api/api';
	import { page } from '$app/state';

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

		if (user) {
			userRole.role = user.admin ? 'admin' : 'user';
		} else {
			userRole.role = 'guest';
		}

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
	<Header />
	{@render children()}
{/if}
