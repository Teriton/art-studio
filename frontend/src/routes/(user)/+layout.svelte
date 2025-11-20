<script lang="ts">
	import '../../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { openModal } from '$lib/stores/OpenModal.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';
	import { fetchActiveUser } from '$lib/api/api';
	import HeaderUserTabs from '$lib/components/Header/HeaderUserTabs.svelte';
	import { goto } from '$app/navigation';
	import type { UserDTO } from '$lib/models';

	let { children } = $props();
	function reroute(href: string) {
		openModal.state = false;
		window.location.href = href;
	}

	let isLoading = $state(true);
	let user: UserDTO | null = null;

	onMount(async () => {
		const img = new Image();
		isLoading = false;

		img.src = '/assets/info_back.jpg';
		img.onload = function () {
			document.body.style.backgroundImage = 'url(' + img.src + ')';
			document.body.style.backgroundSize = 'cover';
			document.body.style.backgroundPosition = 'center';
			document.body.style.backgroundAttachment = 'fixed';
		};
		return { user: user };
	});
	export function load() {
		return { user: user };
	}
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
	<HeaderUserTabs />
	{@render children()}
{/if}
