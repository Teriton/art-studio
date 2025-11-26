<script lang="ts">
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import type { MasterDTO } from '$lib/models.ts';

	// Тестовые мастера (локальные данные, без API)
	let masters: MasterDTO[] = [
		{
			id: 1,
			first_name: 'Анна',
			last_name: 'Коваль',
			specialization: 'Живопись',
			expirience: 8,
			bio: 'Автор авторских этюдов и курсов для начинающих'
		} as unknown as MasterDTO,
		{
			id: 2,
			first_name: 'Пётр',
			last_name: 'Горбачёв',
			specialization: 'Керамика',
			expirience: 12,
			bio: 'Работает с керамикой и глазурью, проводит мастер-классы.'
		} as unknown as MasterDTO,
		{
			id: 3,
			first_name: 'Светлана',
			last_name: 'Лебедева',
			specialization: 'Текстиль',
			expirience: 5,
			bio: 'Специалист по батике и принтам на ткани.'
		} as unknown as MasterDTO
	];

	let loading = false;

	function formatName(m: MasterDTO) {
		return `${m.first_name ?? ''} ${m.last_name ?? ''}`.trim();
	}

	function editMaster(m: MasterDTO) {
		alert(`Редактировать мастера: ${formatName(m)} (id=${m.id})`);
	}

	function removeMaster(m: MasterDTO) {
		masters = masters.filter((x) => x.id !== m.id);
	}
</script>

{#if loading}
	<div class="flex h-[60vh] items-center justify-center">
		<div class="loader h-24 w-24 rounded-full border-8 border-t-8 border-gray-200"></div>
	</div>
{:else}
<SectionWraper>
    <div class="mx-auto w-full mt-16 p-6">
        
        <div class="overflow-x-auto rounded-lg bg-white/70 p-4 shadow">
            <div class="mb-6 flex items-center justify-between">
                <h2 class="text-2xl font-semibold">Мастера</h2>
                <div class="flex items-center gap-4">
                    <div class="text-gray-600">Всего: {masters.length}</div>
                    <button class="rounded bg-green-600 px-3 py-1 text-white hover:bg-green-700">Добавить</button>
                </div>
            </div>
            <table class="w-full table-auto">
					<thead>
						<tr class="text-left text-sm text-gray-600">
							<th class="px-3 py-2">ID</th>
							<th class="px-3 py-2">Имя</th>
							<th class="px-3 py-2">Специализация</th>
							<th class="px-3 py-2">Опыт (лет)</th>
							<th class="px-3 py-2">О мастере</th>
							<th class="px-3 py-2">Действия</th>
						</tr>
					</thead>
					<tbody>
						{#each masters as m (m.id)}
							<tr class="border-t">
								<td class="px-3 py-3 text-sm text-gray-700">{m.id}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{formatName(m)}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{m.specialization}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{m.expirience}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{m.bio}</td>
								<td class="px-3 py-3 text-sm text-gray-700">
									<div class="flex gap-2">
										<button
											class="rounded bg-blue-600 px-3 py-1 text-white hover:bg-blue-700"
											on:click={() => editMaster(m)}
										>
											Ред.
										</button>
										<button
											class="rounded bg-red-600 px-3 py-1 text-white hover:bg-red-700"
											on:click={() => removeMaster(m)}
										>
											Удалить
										</button>
									</div>
								</td>
							</tr>
						{/each}
						{#if masters.length === 0}
							<tr>
								<td colspan="6" class="px-3 py-6 text-center text-gray-500">Мастеров нет</td>
							</tr>
						{/if}
					</tbody>
				</table>
			</div>
		</div>
	</SectionWraper>
{/if}

<style>
	.loader {
		border-top-color: #ef4444;
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}
</style>

