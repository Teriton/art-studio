<script lang="ts">
	import { goto } from '$app/navigation';
	import { delteWorkshopById, fetchWorkshopsAdmin } from '$lib/api/api';
    import SectionWraper from '$lib/components/SectionWraper.svelte';
    import { Status, type WorkshopDTO, type WorkshopRelDTO } from '$lib/models';
	import { onMount } from 'svelte';
    
    let workshops: WorkshopRelDTO[] = $state([]);
    let loading = $state(false);
	
    async function fetchData() {
		const workshopsNull = await fetchWorkshopsAdmin()
		workshops =  workshopsNull ? workshopsNull: [];
		if (!workshopsNull) goto("/");
	}

    async function removeMaster(w: WorkshopRelDTO) {
		workshops = workshops.filter((x) => x.id !== w.id);
		const res = await delteWorkshopById(w.id);
		if (!res) loading = true;
	}

    onMount(async ()=> {await fetchData(); loading=false;});


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
                <h2 class="text-2xl font-semibold">Мастерклассы</h2>
                <div class="flex items-center gap-4">
                    <div class="text-gray-600">Всего: {workshops.length}</div>
                    <button class="rounded bg-green-600 px-3 py-1 text-white hover:bg-green-700">Добавить</button>
                </div>
            </div>
            <table class="w-full table-auto">
					<thead>
						<tr class="text-left text-sm text-gray-600">
							<th class="px-3 py-2">ID</th>
							<th class="px-3 py-2">Название</th>
							<th class="px-3 py-2">Сложность</th>
							<th class="px-3 py-2">Продолжительность, мин.</th>
							<th class="px-3 py-2">Стоимость, руб.</th>
                            <th class="px-3 py-2">Статус</th>
							<th class="px-3 py-2">Действия</th>
						</tr>
					</thead>
					<tbody>
						{#each workshops as w (w.id)}
							<tr class="border-t">
								<td class="px-3 py-3 text-sm text-gray-700">{w.id}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{w.title}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{w.dificulty}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{w.duration}</td>
								<td class="px-3 py-3 text-sm text-gray-700">{w.fee}</td>
                                <td class="px-3 py-3 text-sm text-gray-700">{w.status}</td>
								<td class="px-3 py-3 text-sm text-gray-700">
									<div class="flex gap-2">
										<button
											class="rounded bg-blue-600 px-3 py-1 text-white hover:bg-blue-700"
											onclick={() => {}}
										>
											Подробнее
										</button>
										<button
											class="rounded bg-red-600 px-3 py-1 text-white hover:bg-red-700"
											onclick={async () => { await removeMaster(w)}}
										>
											Удалить
										</button>
									</div>
								</td>
							</tr>
						{/each}
						{#if workshops.length === 0}
							<tr>
								<td colspan="6" class="px-3 py-6 text-center text-gray-500">Мастерклассов нет</td>
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

