<script lang="ts">
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import type { MasterAddDTO, MasterDTO } from '$lib/models.ts';
	import { fetchMastersAdmin, delteMasterById, updateMasterById, addMasterAdmin } from "$lib/api/api";
	import { onMount } from 'svelte';
	import { fade, fly } from 'svelte/transition';
	import { goto } from '$app/navigation';

	let loading = $state(true);
	let addMasterForm: MasterAddDTO | null = $state(null)

	let masters: MasterDTO[] = $state([]);
	let selectedMasterBuf: MasterDTO | null = $state(null);
	let selectedMaster: MasterDTO | null = $state(null);

	async function fetchData() {
		const mastersNull = await fetchMastersAdmin()
		masters =  mastersNull ? mastersNull: [];
		if (!mastersNull) goto("/");
	}

	onMount(async ()=> {await fetchData(); loading=false;});

	async function removeMaster(m: MasterDTO) {
		masters = masters.filter((x) => x.id !== m.id);
		const res = await delteMasterById(m.id);
		if (!res) loading = true;
	}

	function addMasterModal() {
		addMasterForm = {
			first_name: "",
			last_name: "",
			specialization: "",
			expirience: 0,
			bio: ""
		};
	}

	function formatName(m: MasterDTO) {
		return `${m.first_name ?? ''} ${m.last_name ?? ''}`.trim();
	}
	async function save() {
		if (selectedMaster) {
			const { id, ...masterData } = selectedMaster;
			if (!(await updateMasterById(selectedMaster.id,masterData))) {
				loading = true;
			}
		}
		selectedMaster = null;
	}
	async function addMaster() {
		if (addMasterForm) {
			if (!(await addMasterAdmin(addMasterForm))) {
				loading = true;
			}
		}
		await fetchData()
		addMasterForm = null;
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
                    <button class="rounded bg-green-600 px-3 py-1 text-white hover:bg-green-700"
							onclick={addMasterModal}
					
					>Добавить</button>
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
											onclick={()=>{selectedMaster = m; selectedMasterBuf = {...m}}}
										>
											Ред.
										</button>
										<button
											class="rounded bg-red-600 px-3 py-1 text-white hover:bg-red-700"
											onclick={() => removeMaster(m)}
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

{#if selectedMaster}
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
					if (selectedMaster)	Object.assign(selectedMaster, selectedMasterBuf);
					selectedMaster = null
				}}>✕</button
			>
			<h2 class="mb-2 text-2xl font-light">Окно редактирования</h2>
			<div class="flex flex-col gap-2">
				<div class="grid grid-cols-2 gap-4">
					<div>
						<p class="text-gray-700 font-light">Имя</p>
						<input
							bind:value={selectedMaster.first_name}
							class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
						/>
					</div>
					<div>
						<p class="text-gray-700 font-light">Фамилия</p>
						<input
							bind:value={selectedMaster.last_name}
							class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
							/>
					</div>
				</div>
				<div>
					<p class="text-gray-700 font-light">Специализация</p>
					<input
						bind:value={selectedMaster.specialization}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					/>
				</div>
				<div>
					<p class="text-gray-700 font-light">Опыт (лет)</p>
					<input
						type="number"
						bind:value={selectedMaster.expirience}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					/>
				</div>
				<div>
					<p class="text-gray-700 font-light">О мастере</p>
					<textarea
						bind:value={selectedMaster.bio}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none">
					</textarea>
				</div>
				<button
					onclick={save}
					class="w-full mt-2 bg-gray-200/80"
				>
					Сохранить
				</button>
			</div>
		</div>
	</div>
{/if}


{#if addMasterForm}
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
					addMasterForm = null
				}}>✕</button
			>
			<h2 class="mb-2 text-2xl font-light">Окно добавления мастера</h2>
			<div class="flex flex-col gap-2">
				<div class="grid grid-cols-2 gap-4">
					<div>
						<p class="text-gray-700 font-light">Имя</p>
						<input
							bind:value={addMasterForm.first_name}
							class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
						/>
					</div>
					<div>
						<p class="text-gray-700 font-light">Фамилия</p>
						<input
							bind:value={addMasterForm.last_name}
							class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
							/>
					</div>
				</div>
				<div>
					<p class="text-gray-700 font-light">Специализация</p>
					<input
						bind:value={addMasterForm.specialization}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					/>
				</div>
				<div>
					<p class="text-gray-700 font-light">Опыт (лет)</p>
					<input
						type="number"
						bind:value={addMasterForm.expirience}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
					/>
				</div>
				<div>
					<p class="text-gray-700 font-light">О мастере</p>
					<textarea
						bind:value={addMasterForm.bio}
						class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none">
					</textarea>
				</div>
				<button
					class="w-full mt-2 bg-gray-200/80"
					onclick={addMaster}
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

