<script lang="ts">
	import { slide } from 'svelte/transition';
	import { openModal } from '$lib/stores/OpenModal.svelte';
	import { userRole } from '$lib/stores/UserRole.svelte';

	let { reroute = (href: string) => {} } = $props();

	let navItems = $state([] as { label: string; href: string }[]);

	// Функция для обновления навигации
	function updateNavigation(role: string) {
		if (role === 'admin') {
			navItems = [
				{ label: 'В НАЧАЛО', href: '#begin' },
				{ label: 'ПОЛЬЗОВАТЕЛИ', href: '/admin/users' },
				{ label: 'МАСТЕРА', href: '/admin/masters' },
				{ label: 'МАСТЕР-КЛАСС', href: '/admin/workshop' },
				{ label: 'ВЫХОД', href: '/logout' }
			];
		} else if (role === 'user') {
			navItems = [
				{ label: 'В НАЧАЛО', href: '#begin' },
				{ label: 'ТЕХНИКИ', href: '#services' },
				{ label: 'НАША РАБОТА', href: '#masters' },
				{ label: 'РАСПИСАНИЕ', href: '/schedule' },
				{ label: 'ПРОФИЛЬ', href: '/profile' },
				{ label: 'ЗАКАЗЫ', href: '/orders' },
				{ label: 'ВЫХОД', href: '/logout' }
			];
		} else {
			navItems = [
				{ label: 'В НАЧАЛО', href: '#begin' },
				{ label: 'ТЕХНИКИ', href: '#services' },
				{ label: 'НАША РАБОТА', href: '#masters' },
				{ label: 'ВХОД', href: '/login' }
			];
		}
	}

	// Вызываем при изменении роли
	$effect(() => {
		updateNavigation(userRole.role);
	});
</script>

<div
	class="fixed top-0 right-0 z-50 flex h-screen w-screen flex-col gap-8 border-b bg-white p-5 px-8 text-nowrap md:hidden"
	transition:slide={{ axis: 'x' }}
>
	<div class="flex items-center justify-between gap-4 border-b pb-2">
		<div class="pd-10 my-2 flex items-start text-xl md:text-2xl">
			<p class="font-semibold text-red-700">Мастерская искусства</p>
		</div>
		<button
			onclick={() => (openModal.state = false)}
			class="border-none text-red-700 outline-none"
			title="Cool"
		>
			<i class="fa-solid fa-xmark text-2xl"></i>
		</button>
	</div>
	<div class="flex flex-1 flex-col gap-4">
		{#each navItems as item}
			<button
				onclick={() => reroute(item.href)}
				class="group cursor-pointer border-none p-2 text-left duration-200 outline-none"
			>
				<p class="duration-200 group-hover:pl-2">{item.label}</p>
			</button>
		{/each}
	</div>
	<div class="flex flex-col items-center justify-center"></div>
</div>
