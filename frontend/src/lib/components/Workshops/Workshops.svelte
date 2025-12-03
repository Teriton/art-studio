<script lang="ts">
	import { goto } from '$app/navigation';
	import { addWorkshopAdmin, delteWorkshopById, fetchMastersAdmin, fetchTechniquesAdmin, fetchWorkshopsAdmin } from '$lib/api/api';
    import SectionWraper from '$lib/components/SectionWraper.svelte';
    import { Status, type MasterDTO, type TechniqueDTO, type WorkshopAddDTO, type WorkshopDTO, type WorkshopRelDTO } from '$lib/models';
	import { onMount } from 'svelte';
	import { fade, fly } from 'svelte/transition';
    
    let workshops: WorkshopRelDTO[] = $state([]);
    let loading = $state(true);
	let addWorkshopForm: WorkshopAddDTO | null = $state(null);
	let selectedMaster: MasterDTO | null = $state(null);
	let selectedTechnique: TechniqueDTO | null = $state(null);
	let masters: MasterDTO[] | null = $state([]);
	let techniques: TechniqueDTO[] | null = $state([]);
	
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

	async function addWorkshopModal() {
		addWorkshopForm = {
			master_id: -1,
			technique_id: -1,
			title: "",
			dificulty: "",
			duration: 0,
			fee: 0,
			status: Status.unactive

		};

		masters = await fetchMastersAdmin()
		techniques = await fetchTechniquesAdmin()
	}

	async function addWorkshop() {
		if (!selectedMaster) {
			alert("Мастер не выбран!");
			return;
		}

		if (!selectedTechnique) {
			alert("Техника не выбрана!");
			return;
		}
		
		if (addWorkshopForm) {
			addWorkshopForm.master_id = selectedMaster.id;
			addWorkshopForm.technique_id = selectedTechnique.id;
			if (!(await addWorkshopAdmin(addWorkshopForm))) {
				loading = true;
			}
		}
		await fetchData()
		addWorkshopForm = null;
		selectedMaster = null;
		selectedTechnique = null;
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
                    <button class="rounded bg-green-600 px-3 py-1 text-white hover:bg-green-700"
							onclick={addWorkshopModal}
					>Добавить</button>
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

{#if addWorkshopForm}
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
					addWorkshopForm = null
				}}>✕</button
			>
			<h2 class="mb-2 text-2xl font-light">Окно добавления мастера</h2>
			<div class="flex flex-col gap-2">
				<div>
					<p class="text-gray-700 font-light">Название</p>
					<input
						bind:value={addWorkshopForm.title}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					/>
				</div>
				<div>
					<p class="text-gray-700 font-light">Сложность</p>
					<input
						bind:value={addWorkshopForm.dificulty}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					/>
				</div>
				<div>
					<p class="text-gray-700 font-light">Продолжительность</p>
					<input
						bind:value={addWorkshopForm.duration}
						type="number"
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
						/>
				</div>
				<div>
					<p class="text-gray-700 font-light">Стоимость</p>
					<input
						bind:value={addWorkshopForm.fee}
						type="number"
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
						/>
				</div>
				<div>
					<p class="text-gray-700 font-light">Мастер</p>
					<select name="masters" bind:value={selectedMaster}
							class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					>
						{#each masters as master}
							<option value={master}>{master.first_name} {master.last_name}</option>
						{/each}
					</select>
				</div>
				<div>
					<p class="text-gray-700 font-light">Техника</p>
					<select name="techniques" bind:value={selectedTechnique}
							class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					>
						{#each techniques as technique}
							<option value={technique}>{technique.name}</option>
						{/each}
					</select>
				</div>
				<button
					class="w-full mt-2 bg-gray-200/80"
					onclick={addWorkshop}
				>
					Добавить
				</button>
			</div>
		</div>
	</div>
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

