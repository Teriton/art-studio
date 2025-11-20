<script lang="ts">
	import { goto } from '$app/navigation';
	import { fetchNumberOfSeatsAvalable, bookSessionPost } from '$lib/api/api.js';
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import type { ScheduleDTO, Seats } from '$lib/models.js';
	import {fade, fly} from "svelte/transition";


	let { data } = $props();
	let selectedSession: ScheduleDTO | null = $state(null);
	let logedin = $state(false);
	let seats:Seats = $state({
		allSeats: 0,
		occupiedSeats:	0,
	});

	async function selectSession(session:ScheduleDTO) {
		selectedSession = session
		seats = await fetchNumberOfSeatsAvalable(session.id)
	}

	async function bookSession() {
		if (selectedSession === null) return;
		const res = await bookSessionPost(selectedSession.id)
		if (res === null) goto("/login");
		else goto("/orders")
	}
</script>

<SectionWraper>
	<main class="mx-auto mt-10 w-full max-w-5xl px-6 py-12">
		<div class="flex flex-col rounded-xl bg-white/80 p-6 shadow-md backdrop-blur-md">
			{#if !data.error}
				<h1 class="md:text-1xl mx-4 mb-6 text-3xl font-semibold text-black md:mb-0">
					{data.workshop?.title}
				</h1>
				<div class="m-4 grid grid-cols-2 items-center gap-10 md:grid-cols-3">
					<div>
						<h4 class="text-sm text-gray-500">Мастер</h4>
						<p class="text-base text-gray-800">
							{data.workshop?.master.first_name + ' ' + data.workshop?.master.last_name}
						</p>
					</div>
					<div>
						<h4 class="text-sm text-gray-500">Техника</h4>
						<p class="text-grasy-800 text-base">{data.workshop?.technique.name}</p>
					</div>
					<div>
						<h4 class="text-sm text-gray-500">Сложность</h4>
						<p class="text-base text-gray-800">{data.workshop?.dificulty}</p>
					</div>
					<div>
						<h4 class="text-sm text-gray-500">Продолжительность</h4>
						<p class="text-base text-gray-800">{data.workshop?.duration} мин.</p>
					</div>
					<div>
						<h4 class="text-sm text-gray-500">Цена</h4>
						<p class="text-base text-gray-800">{data.workshop?.fee} руб.</p>
					</div>
					<div>
						<h4 class="text-sm text-gray-500">Статус</h4>
						<p class="text-base text-gray-800">{data.workshop?.status}</p>
					</div>
				</div>
				<h2 class="mx-4 my-6 mb-10 text-2xl font-semibold text-black md:my-4 md:mb-0 md:text-xl">
					Необходимые материалы
				</h2>
				<div class="m-4 grid grid-cols-2 items-center gap-10 md:grid-cols-3">
					{#each data.workshop?.sets_of_material as set_of_material}
						<div>
							<h4 class="text-sm text-gray-500">{set_of_material.material.name}</h4>
							<p class="text-base text-gray-800">
								{set_of_material.quantity + ' ' + set_of_material.unit}
							</p>
						</div>
					{/each}
				</div>
				<hr/>
				<div class="flex flex-col gap-2">
					<h2 class="mx-4 my-6 text-2xl font-semibold text-black md:my-3 md:mb-0 md:text-xl">
						Расписание сессий
					</h2>
					<div class="flex flex-col gap-3 rounded-3xl bg-gray-400/40 p-4 shadow-xl">
						{#each data.sessions as sessionDate}
							<h2 class="mx-4 text-2xl font-semibold text-black md:text-xl">{sessionDate[0]}</h2>
							<div class="mx-4 flex gap-4">
								{#each sessionDate[1] as session}
									<button class=" rounded-2xl bg-red-400 p-2 px-4 duration-200 hover:cursor-pointer hover:bg-red-300"
											onclick={() => selectSession(session)}
									>
										<div
										>
											<p>{new Date(session.date).toISOString().split('T')[1].slice(0, 5)}</p>
										</div>
									</button>
								{/each}
							</div>
						{/each}
					</div>
				</div>
			{:else}
				<h1 class="md:text-1xl fosnt-semibold mx-4 mb-6 text-3xl text-black md:mb-0">
					Error {data.error}
				</h1>
			{/if}
		</div>
	</main>
</SectionWraper>

{#if selectedSession}
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
					selectedSession = null;
				}}>✕</button
			>
			<div class="flex flex-col gap-4 md:gap-2">
				<h2 class="mb-2 text-2xl font-bold">Основная информация</h2>
				<p class="text-gray-700">
					<span class=" text-black">Место проведения:</span>
					{selectedSession.location} 
				</p>
				<p class="text-gray-700">
					<span class=" text-black">Время:</span>
					{selectedSession.date}
				</p>
				<p class="text-gray-700">
					<span class=" text-black">Колличество мест:</span>
					{seats.allSeats}/{seats.occupiedSeats}
				</p>
				<button
					onclick={async () => await bookSession()}
					class="block w-full border-amber-50 text-center transition-colors"
				>
					Забронировать
				</button>
			</div>
		</div>
	</div>
{/if}
