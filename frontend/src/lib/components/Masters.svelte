<script lang="ts">
	import type { MasterDTO } from '$lib/models';
	import { onMount } from 'svelte';
	import SectionWraper from './SectionWraper.svelte';
	import { fetchMasters } from '$lib/api/api';

	let { masters } = $props();

	// const masters = [
	//   {
	//     name: 'Анна Кузнецова',
	//     skills: 'Акварель и графику',
	//     experience: '6 лет',
	//     description: 'Специализируется на создании живописных и графических работ в технике акварели.',
	//     img: 'https://tse3.mm.bing.net/th/id/OIP.TaiypjChKJsZJOwD7D-jygHaED?rs=1&pid=ImgDetMain&o=7&rm=3'
	//   },
	//   {
	//     name: 'Арина Ковалева',
	//     skills: 'Декупаж, декорирование предметов интерьера',
	//     experience: '6 лет',
	//     description: 'Опытный мастер по декупажу, создаёт уникальные предметы интерьера с использованием различных техник украшения.',
	//     img: 'https://tse3.mm.bing.net/th/id/OIP.TaiypjChKJsZJOwD7D-jygHaED?rs=1&pid=ImgDetMain&o=7&rm=3'
	//   },
	//   {
	//     name: 'Дмитрий Соколов',
	//     skills: 'Текстурные пасты, скульптура',
	//     experience: '10 лет',
	//     description: 'Мастер по созданию объемных текстур и скульптурных работ с использованием различных материалов.',
	//     img: 'https://tse3.mm.bing.net/th/id/OIP.TaiypjChKJsZJOwD7D-jygHaED?rs=1&pid=ImgDetMain&o=7&rm=3'
	//   },
	//   {
	//     name: 'Екатерина Лебедева',
	//     skills: 'Изделия из эпоксидной смолы',
	//     experience: '7 лет',
	//     description: 'Создаёт уникальные изделия и украшения с использованием прозрачной эпоксидной смолы.',
	//     img: 'https://tse3.mm.bing.net/th/id/OIP.TaiypjChKJsZJOwD7D-jygHaED?rs=1&pid=ImgDetMain&o=7&rm=3'
	//   },
	//   {
	//     name: 'Екатерина Лебедева',
	//     skills: 'Изделия из эпоксидной смолы',
	//     experience: '7 лет',
	//     description: 'Создаёт уникальные изделия и украшения с использованием прозрачной эпоксидной смолы.',
	//     img: 'https://tse3.mm.bing.net/th/id/OIP.TaiypjChKJsZJOwD7D-jygHaED?rs=1&pid=ImgDetMain&o=7&rm=3'
	//   }
	// ];
</script>

<SectionWraper id="masters">
	<div class="mt-14 text-center">
		<h3 class="mx-auto text-3xl font-bold text-white">Наши мастера</h3>
		<div class="mx-auto mt-2 h-0.5 w-24 bg-red-500 transition-all duration-300"></div>
	</div>
	<div class="container mb-20 pb-2">
		<div class="scrollbar-custom w-screen overflow-x-auto py-10">
			<div class="flex min-w-max gap-6 px-2">
				{#each masters as master}
					<div
						class="max-w-80 min-w-[250px] rounded-xl bg-linear-to-br from-pink-100 to-yellow-100 shadow-md transition-transform duration-300 hover:scale-105"
					>
						<img
							src="https://tse3.mm.bing.net/th/id/OIP.TaiypjChKJsZJOwD7D-jygHaED?rs=1&pid=ImgDetMain&o=7&rm=3"
							alt={master.first_name + ' ' + master.last_name}
							class="h-60 w-full rounded-lg object-cover"
						/>
						<div class="p-4">
							<h3 class="mb-2 text-xl font-semibold text-gray-900">
								{master.first_name + ' ' + master.last_name}
							</h3>
							<p class="mb-1 text-sm text-gray-900">Опыт: {master.expirience}</p>
							<p class="mb-1 text-red-800">{master.specialization}</p>
							<p class="text-balck mb-1">{master.bio}</p>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</SectionWraper>
