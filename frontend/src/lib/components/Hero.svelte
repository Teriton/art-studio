<script lang="ts">
	import { onMount } from 'svelte';
	import SectionWraper from './SectionWraper.svelte';
	import type { WorkshopMasterDTO } from '$lib/models';
	import { fetchClosestWorkshop } from '$lib/api/api';
	import { animateTyping } from '$lib/animateTyping';

	let { workshop } = $props();

	// onMount(async () => {
	//     workshop = workshopState.workshop;
	//     $inspect(workshop);
	// });
</script>

<SectionWraper id="begin">
	<div
		class="relative inset-0 w-full overflow-hidden bg-[url('/assets/pastel1.jpg')] bg-cover bg-fixed bg-center"
	>
		<div class="absolute inset-0 bg-black/40"></div>
		<!-- Контент поверх фона -->
		<div class="h-10"></div>
		{#if workshop != undefined}
			<div
				class="relative z-10 flex flex-col items-center justify-center px-4 py-20 text-center md:mx-[150px] lg:mx-[300px]"
			>
				<h2 class="mb-4 text-2xl font-bold text-white md:text-3xl">
					Мастерская приветствует вас!<br />Открыта запись на наш новый МК.
				</h2>

				<div class="mb-6 text-sm text-gray-200 md:text-base">
					<p class="font-semibold">
						Продолжительность: <span class="font-semibold text-white">{workshop.duration} мин</span>
					</p>
					<p class="font-semibold">
						Сложность: <span class="font-semibold text-white">{workshop.dificulty}</span>
					</p>
				</div>

				<h3 class="mb-4 text-3xl font-bold text-white hover:cursor-pointer md:text-4xl">
					{workshop.title}
				</h3>
				<div class="text-lg font-semibold text-white">
					<div class="mb-4 flex items-center justify-center gap-2">
						<p>&nbsp;</p>
						<p use:animateTyping={[workshop.status]}></p>
						<p>&nbsp;</p>
					</div>
					<p><span class="text-green-300">{workshop.fee.toFixed(2)} руб.</span></p>
				</div>
			</div>
		{/if}
	</div>
</SectionWraper>
