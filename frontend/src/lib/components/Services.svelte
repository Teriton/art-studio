<script lang="ts">
	import SectionWraper from './SectionWraper.svelte';
	import { fly, fade } from 'svelte/transition';

	interface Technique {
		name: string;
		image: string;
		description: string;
	}

	let selectedTechnique: Technique | null = null;
	const techniques: Technique[] = [
		{
			name: 'Акварель',
			image: 'img/watercolor.jpg',
			description: 'Техника живописи с использованием водорастворимых красок.'
		},
		{
			name: 'Спиртовые чернила',
			image: 'img/alcoholink.jpg',
			description: 'Техника создания ярких абстрактных изображений с помощью спиртовых чернил.'
		},
		{
			name: 'Декупаж',
			image: 'img/decoupage.jpg',
			description: 'Техника украшения предметов вырезанными изображениями и их закрепления лаком.'
		},
		{
			name: 'Эпоксидная смола',
			image: 'img/epoxyresin.jpg',
			description:
				'Техника создания изделий и украшений с использованием прозрачной эпоксидной смолы.'
		},
		{
			name: 'Керамика',
			image: 'img/ceramics.jpg',
			description: 'Техника создания изделий из глины с последующим обжигом и глазурованием.'
		},
		{
			name: 'Текстурная паста',
			image: 'img/texture.jpg',
			description: 'Техника создания объемных текстур на поверхности с помощью специальных паст.'
		},
		{
			name: 'Мозаика',
			image: 'img/mosaic.jpg',
			description:
				'Техника создания изображений или узоров из мелких кусочков стекла, камня или керамики.'
		},
		{
			name: 'Эбру',
			image: 'img/ebru.jpg',
			description: 'Техника рисования на воде с использованием специальных красок.'
		}
	];

	function openModal(technique: Technique) {
		selectedTechnique = technique;
	}
</script>

<SectionWraper id="services">
	<div class="relative">
		<div class="absolute inset-0 bg-red-700/40"></div>
		<div class="absolute inset-0 bg-black/40"></div>
		<section id="service" class="relative z-10 py-16">
			<div class="container mx-auto px-4">
				<div class="mb-12 text-center">
					<h3 class="text-3xl font-bold text-white">Техники</h3>
					<div class="mx-auto mt-2 h-0.5 w-24 bg-red-500 transition-all duration-300"></div>
				</div>

				<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
					{#each techniques as { name, image, description }}
						<div
							role="button"
							tabindex="0"
							onkeydown={(e) => e.key === 'Enter' && openModal({ name, image, description })}
							onclick={() => openModal({ name, image, description })}
							class="relative h-[300px] transform cursor-pointer overflow-hidden rounded-lg bg-cover bg-center shadow-lg transition-transform duration-300 hover:scale-105"
							style={`background-image: url('${image}')`}
						>
							<div class="absolute inset-0 bg-black/10"></div>
							<div class="absolute bottom-4 left-4">
								<h2 class="text-xl font-bold text-white drop-shadow-md">{name}</h2>
							</div>
						</div>
					{/each}
				</div>
			</div>
		</section>
	</div>
</SectionWraper>

{#if selectedTechnique}
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
					selectedTechnique = null;
				}}>✕</button
			>
			<h2 class="mb-2 text-2xl font-bold">{selectedTechnique.name}</h2>
			<p class="text-gray-700">{selectedTechnique.description}</p>
		</div>
	</div>
{/if}
