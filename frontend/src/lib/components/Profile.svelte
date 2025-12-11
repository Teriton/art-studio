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

	// errors
	let errors = $state({
		email: '',
		phone_number: '',
		first_name: '',
		last_name: ''
	});

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

	function validateEmail(emailValue: string): boolean {
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		return emailRegex.test(emailValue);
	}

	function validatePhone(phoneValue: string): boolean {
		const phoneRegex = /^[\d\s\-\+\(\)]+$/;
		return phoneRegex.test(phoneValue) && phoneValue.replace(/\D/g, '').length >= 10;
	}

	function validateForm(): boolean {
		let valid = true;
		errors = { email: '', phone_number: '', first_name: '', last_name: '' };

		if (!first_name.trim()) {
			errors.first_name = 'Укажите имя';
			valid = false;
		}

		if (!last_name.trim()) {
			errors.last_name = 'Укажите фамилию';
			valid = false;
		}

		if (!email.trim()) {
			errors.email = 'Укажите email';
			valid = false;
		} else if (email && !validateEmail(email)) {
			errors.email = 'Некорректный формат email';
			valid = false;
		}

		if (!phone_number.trim()) {
			errors.phone_number = 'Укажите телефон';
			valid = false;
		} else if (phone_number && !validatePhone(phone_number)) {
			errors.phone_number = 'Телефон должен содержать минимум 10 цифр';
			valid = false;
		}

		return valid;
	}

	async function save() {
		if (!validateForm()) return;
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
					<form class="space-y-4" onsubmit={(e) => { e.preventDefault(); save(); }}>
						<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
							<div>
								<input
									class={`w-full rounded border p-3 ${errors.first_name ? 'border-red-500' : ''}`}
									bind:value={first_name}
									placeholder="Имя"
									oninput={() => (errors.first_name = '')}
								/>
								{#if errors.first_name}
									<p class="mt-1 text-sm text-red-500">{errors.first_name}</p>
								{/if}
							</div>
							<div>
								<input
									class={`w-full rounded border p-3 ${errors.last_name ? 'border-red-500' : ''}`}
									bind:value={last_name}
									placeholder="Фамилия"
									oninput={() => (errors.last_name = '')}
								/>
								{#if errors.last_name}
									<p class="mt-1 text-sm text-red-500">{errors.last_name}</p>
								{/if}
							</div>
						</div>
						<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
							<div>
								<input
									class={`w-full rounded border p-3 ${errors.email ? 'border-red-500' : ''}`}
									bind:value={email}
									placeholder="Email"
									oninput={() => (errors.email = '')}
								/>
								{#if errors.email}
									<p class="mt-1 text-sm text-red-500">{errors.email}</p>
								{/if}
							</div>
							<div>
								<input
									class={`w-full rounded border p-3 ${errors.phone_number ? 'border-red-500' : ''}`}
									bind:value={phone_number}
									placeholder="Телефон"
									oninput={() => (errors.phone_number = '')}
								/>
								{#if errors.phone_number}
									<p class="mt-1 text-sm text-red-500">{errors.phone_number}</p>
								{/if}
							</div>
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
