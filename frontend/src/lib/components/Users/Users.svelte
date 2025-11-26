
<script lang="ts">
	import SectionWraper from '$lib/components/SectionWraper.svelte';
	import type { UserDTO } from '$lib/models.ts';
	import { onMount } from 'svelte';
    import {delteUserById} from "$lib/api/api"
    
    let ws: WebSocket | null = $state(null);
    let message = $state("");
    let messages: string[] = $state([]);
    let users: UserDTO[] | null = $state(null);
    let loading = false;
    let error: string | null = $state(null);

    onMount(()=>{
        ws = new WebSocket("ws://127.0.0.1:8000/admin/users");
        ws.onmessage = (event) => {
            console.log(event.data)
            users = JSON.parse(event.data) as UserDTO[];
        };

        return () => {
            ws?.close();
        };
    });


	function formatName(u: UserDTO) {
		return `${u.first_name ?? ''} ${u.last_name ?? ''}`.trim();
	}

	async function removeUser(u: UserDTO) {
		const res = await delteUserById(u.id)
        if (!res) error = "Error while deleting";
	}
</script>

{#if loading}
	<div class="flex h-[60vh] items-center justify-center">
		<div class="loader h-24 w-24 rounded-full border-8 border-t-8 border-gray-200"></div>
	</div>
{:else}
	<SectionWraper>
		<div class="mx-auto w-full mt-16 p-6">
			{#if error || users ==null}
				<div class="rounded bg-red-100 p-4 text-red-700">{error}</div>
			{:else}
				<div class="overflow-x-auto rounded-lg bg-white/70 p-4 shadow">
                    <div class="font-semibold mx-2 mb-4 text-gray-600">Всего пользователей: {users != null?  users.length : 0}</div>
					<table class="w-full table-auto">
						<thead>
							<tr class="text-left text-sm text-gray-600">
								<th class="px-3 py-2">ID</th>
								<th class="px-3 py-2">Имя</th>
								<th class="px-3 py-2">Email</th>
								<th class="px-3 py-2">Телефон</th>
								<th class="px-3 py-2">Логин</th>
								<th class="px-3 py-2">Админ</th>
								<th class="px-3 py-2">Действия</th>
							</tr>
						</thead>
						<tbody>
							{#each users as u }
								<tr class="border-t">
									<td class="px-3 py-3 text-sm text-gray-700">{u.id}</td>
									<td class="px-3 py-3 text-sm text-gray-700">{formatName(u)}</td>
									<td class="px-3 py-3 text-sm text-gray-700">{u.email}</td>
									<td class="px-3 py-3 text-sm text-gray-700">{u.phone_number}</td>
									<td class="px-3 py-3 text-sm text-gray-700">{u.login}</td>
									<td class="px-3 py-3 text-sm text-gray-700">{u.admin ? 'Да' : 'Нет'}</td>
									<td class="px-3 py-3 text-sm text-gray-700">
										<div class="flex gap-2">
											<button
												class="rounded bg-red-600 px-3 py-1 text-white hover:bg-red-700"
												onclick={async () => await removeUser(u)}
												title="Удалить пользователя"
											>
												Удалить
											</button>
										</div>
									</td>
								</tr>
							{/each}
							{#if users.length === 0}
								<tr>
									<td colspan="7" class="px-3 py-6 text-center text-gray-500">Пользователей нет</td>
								</tr>
							{/if}
						</tbody>
					</table>
				</div>
			{/if}
		</div>
	</SectionWraper>
{/if}

<style>
	/* keep loader style consistent with other pages */
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
