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
			class="animate-fade-in relative w-full max-w-md rounded-lg bg-white p-6 shadow-xl"
			transition:fly={{ y: 100, duration: 300 }}
		>
			<button
				class="absolute top-2 right-2 text-gray-500 hover:text-gray-800"
				onclick={() => {
					selectedWorkshop = null;
				}}>✕</button
			>
			<div class="flex flex-col gap-4 md:gap-2">
				<h2 class="mb-2 text-2xl font-bold">{selectedWorkshop.title}</h2>
				<p class="text-gray-700">
					<span class=" text-black">Продолжительность:</span>
					{selectedWorkshop.duration} минут
				</p>
				<p class="text-gray-700">
					<span class=" text-black">Мастер:</span>
					{selectedWorkshop.master.first_name + ' ' + selectedWorkshop.master.last_name}
				</p>
				<p class="text-gray-700">
					<span class=" text-black">Сложность:</span>
					{selectedWorkshop.dificulty}
				</p>
				<p class="text-gray-700">
					<span class=" text-black">Стоимость:</span>
					{selectedWorkshop.fee}
				</p>
				<button
					class="block w-full border-amber-50 text-center transition-colors"
					onclick={() => orderPage(selectedWorkshop === null ? null : selectedWorkshop.id)}
				>
					Забронировать
				</button>
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
