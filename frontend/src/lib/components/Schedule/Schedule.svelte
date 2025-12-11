<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import type { WorkshopRelDTO } from '$lib/models';
	import { fetchWorkshops } from '$lib/api/api';
	import { fly, fade } from 'svelte/transition';
	import ScheduleCard from './ScheduleCard.svelte';

	let loading = $state(false);
	let error: string | null = $state(null);
	let workshops: WorkshopRelDTO[] | null = $state([]);
	let selectedWorkshop: WorkshopRelDTO | null = $state(null);
	// Имитация загрузки данных
	onMount(async () => {
		loading = true;
		error = null;
		try {
			// Здесь должен быть реальный вызов API, например:
			workshops = await fetchWorkshops();
			if (workshops === null) {
				goto('/login');
				return;
			}
			// Для демонстрации используем заглушк
		} catch (err) {
			console.error(err);
			error = String(err);
		} finally {
			loading = false;
		}
	});

	function formatDateTime(date: Date): string {
		const day = String(date.getDate()).padStart(2, '0');
		const month = String(date.getMonth() + 1).padStart(2, '0');
		const year = date.getFullYear();
		const hours = String(date.getHours()).padStart(2, '0');
		const minutes = String(date.getMinutes()).padStart(2, '0');
		return `${day}.${month}.${year} (${hours}:${minutes}`;
	}

	function formatEndTime(endDate: Date): string {
		const hours = String(endDate.getHours()).padStart(2, '0');
		const minutes = String(endDate.getMinutes()).padStart(2, '0');
		return `${hours}:${minutes})`;
	}

	async function orderPage(workshopId: number | null) {
		if (workshopId === null) goto('/');
		goto(`/schedule/${workshopId}`);
	}

	function openModal(workshop: WorkshopRelDTO) {
		selectedWorkshop = workshop;
	}
</script>

<svelte:head>
	<title>Расписание — Мастерская искусства</title>
</svelte:head>

<SectionWraper>
	<main class="mx-auto mt-10 w-full max-w-5xl px-6 py-12">
		<div class="flex flex-col rounded-xl bg-white/80 p-6 shadow-md backdrop-blur-md">
			<h1 class="md:text-1xl mx-4ss text-3xl font-semibold text-black">
				Расписание
			</h1>
			<hr class="my-4"/>

			{#if loading}
				<div class="animate-pulse">
					<div class="mb-4 h-10 rounded bg-red-800"></div>
					<div class="mb-4 h-10 rounded bg-red-800"></div>
				</div>
			{:else if error}
				<div class="rounded bg-red-900 p-4 text-red-300">Ошибка загрузки расписания: {error}</div>
			{:else if workshops === null || workshops.length === 0}
				<div class="py-8 text-center text-gray-400">Нет доступных мастерских.</div>
			{:else}
				<div class="flex flex-col gap-6">
				{#each workshops as workshop}
					<ScheduleCard {workshop} select={async ()=>{await openModal(workshop)}} orderPage={async ()=>{await orderPage(workshop.id)}}></ScheduleCard>
				{/each}
				</div>
			{/if}
		</div>
	</main>
</SectionWraper>

{#if selectedWorkshop}
	<div
		class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 transition-opacity duration-300"
		transition:fade
	>
		<div
			class="animate-fade-in relative w-full max-w-2xl rounded-lg bg-white p-8 shadow-xl max-h-[90vh] overflow-y-auto"
			transition:fly={{ y: 100, duration: 300 }}
		>
			<button
				class="absolute top-4 right-4 text-gray-500 hover:text-gray-800 text-2xl"
				onclick={() => {
					selectedWorkshop = null;
				}}>✕</button
			>
			<div class="flex flex-col gap-4">
				<h2 class="text-3xl font-bold text-gray-800">{selectedWorkshop.title}</h2>
				
				<!-- Описание -->
				<div class="bg-gray-50 p-4 rounded-lg">
					<p class="text-gray-700 leading-relaxed">
						{selectedWorkshop.description}
					</p>
				</div>

				<!-- Сетка параметров -->
				<div class="grid grid-cols-2 gap-4">
					<div class="bg-red-50 p-4 rounded-lg">
						<p class="text-sm text-gray-600 font-semibold">Продолжительность</p>
						<p class="text-lg font-bold text-gray-800">{selectedWorkshop.duration} мин</p>
					</div>
					<div class="bg-amber-50 p-4 rounded-lg">
						<p class="text-sm text-gray-600 font-semibold">Стоимость</p>
						<p class="text-lg font-bold text-red-600">{selectedWorkshop.fee} ₽</p>
					</div>
					<div class="bg-blue-50 p-4 rounded-lg">
						<p class="text-sm text-gray-600 font-semibold">Сложность</p>
						<p class="text-lg font-bold text-gray-800">{selectedWorkshop.dificulty}</p>
					</div>
					<div class="bg-green-50 p-4 rounded-lg">
						<p class="text-sm text-gray-600 font-semibold">Статус</p>
						<p class="text-lg font-bold text-gray-800">{selectedWorkshop.status}</p>
					</div>
				</div>

				<!-- Информация о мастере -->
				<div class="bg-purple-50 p-4 rounded-lg">
					<h3 class="font-semibold text-gray-800 mb-2">Преподаватель</h3>
					<p class="text-lg font-bold text-gray-800">
						{selectedWorkshop.master.first_name} {selectedWorkshop.master.last_name}
					</p>
					<p class="text-sm text-gray-600 mt-1">{selectedWorkshop.master.specialization}</p>
					{#if selectedWorkshop.master.expirience}
						<p class="text-sm text-gray-600 mt-1">Опыт: {selectedWorkshop.master.expirience} лет</p>
					{/if}
				</div>

				<!-- Информация о технике -->
				<div class="bg-indigo-50 p-4 rounded-lg">
					<h3 class="font-semibold text-gray-800 mb-2">Техника</h3>
					<p class="text-lg font-bold text-gray-800">{selectedWorkshop.technique.name}</p>
				</div>

				<!-- Кнопки действия -->
				<div class="flex gap-3 mt-6">
					<button
						class="flex-1 bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-4 rounded-lg transition-colors"
						onclick={() => orderPage(selectedWorkshop === null ? null : selectedWorkshop.id)}
					>
						Забронировать
					</button>
					<button
						class="flex-1 bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-3 px-4 rounded-lg transition-colors"
						onclick={() => {
							selectedWorkshop = null;
						}}
					>
						Закрыть
					</button>
				</div>
			</div>
		</div>
	</div>
{/if}

<style>
	/* Убедитесь, что основной фон не перекрывает контент */
	main {
		min-height: calc(100vh - 4rem);
	}
</style>
