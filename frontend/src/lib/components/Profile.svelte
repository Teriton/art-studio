<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import type { UserDTO } from '$lib/models';
	import { fetchActiveUser, updateUserInfo } from '$lib/api/api';

	let user: UserDTO | null = $state(null);
	let loading = $state(true);
	let error: string | null = $state(null);
	let editing = $state(false);

	// form fields
	let first_name = $state('');
	let last_name = $state('');
	let email = $state('');
	let phone_number = $state('');

	onMount(async () => {
		loading = true;
		error = null;
		try {
			user = await fetchActiveUser();
			if (user === null) {
				// not logged in, redirect to login
				goto('/login');
				return;
			}
			first_name = user?.first_name ?? '';
			last_name = user?.last_name ?? '';
			email = user?.email ?? '';
			phone_number = user?.phone_number ?? '';
		} catch (err) {
			console.error(err);
			error = String(err);
		} finally {
			loading = false;
		}
	});

	function initials(u: UserDTO | null) {
		if (!u) return '??';
		return ((u.first_name[0] ?? '') + (u.last_name[0] ?? '')).toUpperCase() || 'U';
	}

	async function save() {
		// optimistic local save; backend update endpoint may be missing in this repo.
		editing = false;
		if (!user) return;
		user.first_name = first_name;
		user.last_name = last_name;
		user.email = email;
		user.phone_number = phone_number;
		await updateUserInfo(user);
	}

	function logout() {
		// simple client redirect to logout route if available
		goto('/logout');
	}
</script>

<svelte:head>
	<title>Профиль — Мастерская искусства</title>
</svelte:head>

<SectionWraper>
	<main class="mx-auto mt-10 max-w-5xl px-6 py-12">
		<div class="grid grid-cols-1 gap-8 lg:grid-cols-3">
			<!-- profile card -->
			<section class="col-span-1 rounded-xl bg-white/80 p-6 shadow-md backdrop-blur-md">
				{#if loading}
					<div class="animate-pulse">
						<div class="mb-4 h-32 w-32 rounded-full bg-gray-200"></div>
						<div class="mb-2 h-4 w-3/4 rounded bg-gray-200"></div>
						<div class="h-4 w-1/2 rounded bg-gray-200"></div>
					</div>
				{:else if error}
					<div class="text-red-600">{error}</div>
				{:else}
					<div class="flex flex-col items-center text-center">
						<div
							class="mb-4 flex h-28 w-28 items-center justify-center rounded-full bg-red-100 text-2xl font-bold text-red-700"
						>
							{initials(user)}
						</div>
						<h2 class="text-xl font-semibold text-gray-800">
							{user?.first_name}
							{user?.last_name}
						</h2>
						<p class="text-sm text-gray-500">@{user?.login}</p>
						<p class="mt-3 text-sm text-gray-600">{user?.email}</p>
						<p class="mt-1 text-sm text-gray-600">{user?.phone_number}</p>

						<div class="mt-6 flex w-full gap-3">
							<button
								class="flex-1 rounded bg-red-700 py-2 text-white hover:bg-red-600"
								onclick={() => (editing = !editing)}
							>
								{editing ? 'Отмена' : 'Редактировать'}
							</button>
							<button class="flex-1 rounded bg-gray-200 py-2 text-gray-800" onclick={logout}>
								Выйти
							</button>
						</div>
					</div>
				{/if}
			</section>

			<!-- main content -->
			<section class="col-span-2 rounded-xl bg-white/80 p-6 shadow-md backdrop-blur-md">
				<div class="mb-6 flex items-center justify-between">
					<h3 class="text-lg font-semibold text-gray-800">Мой профиль</h3>
				</div>

				{#if editing}
					<form class="space-y-4" onsubmit={save}>
						<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
							<input class="rounded border p-3" bind:value={first_name} placeholder="Имя" />
							<input class="rounded border p-3" bind:value={last_name} placeholder="Фамилия" />
						</div>
						<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
							<input class="rounded border p-3" bind:value={email} placeholder="Email" />
							<input class="rounded border p-3" bind:value={phone_number} placeholder="Телефон" />
						</div>

						<div class="flex gap-3">
							<button type="submit" class="rounded bg-red-700 px-4 py-2 text-white hover:bg-red-600"
								>Сохранить</button
							>
							<button
								type="button"
								class="rounded bg-gray-200 px-4 py-2"
								onclick={() => (editing = false)}>Отмена</button
							>
						</div>
					</form>
				{:else}
					<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
						<div>
							<h4 class="text-sm text-gray-500">Имя</h4>
							<p class="text-base text-gray-800">{user?.first_name}</p>
						</div>
						<div>
							<h4 class="text-sm text-gray-500">Фамилия</h4>
							<p class="text-base text-gray-800">{user?.last_name}</p>
						</div>
						<div>
							<h4 class="text-sm text-gray-500">Email</h4>
							<p class="text-base text-gray-800">{user?.email}</p>
						</div>
						<div>
							<h4 class="text-sm text-gray-500">Телефон</h4>
							<p class="text-base text-gray-800">{user?.phone_number}</p>
						</div>
					</div>
				{/if}

				<hr class="my-6" />

				<div class="grid grid-cols-1 gap-6 md:grid-cols-2">
					<div class="rounded border p-4">
						<h5 class="mb-2 font-semibold text-gray-800">Расписание</h5>
						<p class="text-sm text-gray-600">Перейти к расписанию.</p>
						<div class="mt-4">
							<a class="text-red-700 hover:underline" href="/schedule">Посмотреть</a>
						</div>
					</div>

					<div class="rounded border p-4">
						<h5 class="mb-2 font-semibold text-gray-800">Мои заказы</h5>
						<p class="text-sm text-gray-600">Статус и история ваших заказов.</p>
						<div class="mt-4">
							<a class="text-red-700 hover:underline" href="/orders">Посмотреть заказы</a>
						</div>
					</div>
				</div>
			</section>
		</div>
	</main>
</SectionWraper>

<style>
	/* small helpers to keep visuals consistent with site */
	main {
		min-height: calc(100vh - 4rem);
	}
</style>
