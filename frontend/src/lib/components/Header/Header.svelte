<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { openModal } from '$lib/stores/OpenModal.svelte';
	import { userRole } from '$lib/stores/UserRole.svelte';

	let navItems = $state([] as { label: string; href: string }[]);

	// Функция для обновления навигации
	function updateNavigation(role: string) {
		if (role === 'admin') {
			navItems = [
				{ label: 'В НАЧАЛО', href: '#begin' },
				{ label: 'ПОЛЬЗОВАТЕЛИ', href: '/admin/users' },
				{ label: 'МАСТЕРА', href: '/admin/masters' },
				{ label: 'МАСТЕР-КЛАСС', href: '/admin/workshops' },
				{ label: 'ПРОФИЛЬ', href: '/admin/profile' },
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

	// scrollY from window
	let y = $state(0);
	let scrolled = $derived(y > 0);

	// active section hash like '#begin'
	let active = $state('#begin');

	let observer: IntersectionObserver | null = null;

	onMount(() => {
		// Найти элементы только для тех ссылок, которые являются якорями (#id).
		// Не пытаться делать querySelector для route-путей типа '/registration/admin'.
		const sections = navItems
			.map((i) =>
				typeof i.href === 'string' && i.href.startsWith('#')
					? (document.querySelector(i.href) as HTMLElement | null)
					: null
			)
			.filter(Boolean) as HTMLElement[];

		if (sections.length) {
			observer = new IntersectionObserver(
				(entries) => {
					// выбирать ту секцию, которая видима ближе к центру окна
					entries.forEach((entry) => {
						if (entry.isIntersecting) {
							active = `#${entry.target.id}`;
						}
					});
				},
				{
					root: null,
					// центр окна: когда элемент пересекает середину экрана — считаем его активным
					rootMargin: '-40% 0px -40% 0px',
					threshold: 0
				}
			);

			sections.forEach((s) => observer!.observe(s));
		}
	});

	onDestroy(() => {
		observer?.disconnect();
		observer = null;
	});
</script>

<div class="fixed top-0 left-0 z-20 flex w-full flex-col">
	<div class={'flex justify-around duration-200 ' + (scrolled ? 'bg-white' : 'bg-transparent')}>
		<div
			class={'z-1 mx-5 flex w-full max-w-[1400px] items-center justify-between p-4 duration-200' +
				(scrolled ? 'py-4' : 'py-6')}
		>
			<div class="pd-10 my-2 flex items-start text-xl md:text-2xl">
				<p class={'font-semibold ' + (scrolled ? 'text-red-700' : 'text-white')}>
					Мастерская искусства
				</p>
			</div>
			<button
				type="button"
				onclick={() => (openModal.state = true)}
				class="grid place-items-center rounded bg-transparent hover:bg-transparent focus:outline-none focus-visible:ring-2 focus-visible:ring-red-400/40 md:hidden"
				title="menu"
				aria-label="Открыть меню"
			>
				<i class={'fa-solid fa-bars ' + (scrolled ? 'text-red-700' : 'text-white')}></i>
			</button>
			<nav
				class="hidden items-center gap-4 pt-2 text-sm md:flex lg:gap-6 lg:text-base"
				aria-label="Главная навигация"
			>
				{#each navItems as { label, href }}
					<a
						{href}
						class="group relative inline-block pb-1 focus:outline-none"
						aria-current={active === href ? 'true' : 'false'}
					>
						<span class={'font-semibold ' + (scrolled ? 'text-red-700' : 'text-white')}>
							<span class="font-bold">{label}</span>
						</span>

						<span
							class={'absolute bottom-0 left-0 h-0.5 transition-all duration-300 ' +
								(active === href ? 'w-full ' : 'w-0 group-hover:w-full ') +
								(scrolled ? 'bg-red-700' : 'bg-white')}
						></span>
					</a>
				{/each}
			</nav>
		</div>
	</div>
</div>

<svelte:window bind:scrollY={y} />
