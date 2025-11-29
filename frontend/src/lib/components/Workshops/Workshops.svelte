<script lang="ts">
    import SectionWraper from '$lib/components/SectionWraper.svelte';
    import { Status, type WorkshopDTO } from '$lib/models';

	// Тестовые мастера (локальные данные, без API)
    const workshops: WorkshopDTO[] = [
    {
        id: 1,
        master_id: 101,
        technique_id: 201,
        title: "Основы акварели",
        dificulty: "Новичок",
        duration: 120,
        fee: 2500,
        status: Status.active
    },
    {
        id: 2,
        master_id: 102,
        technique_id: 202,
        title: "Роспись по керамике",
        dificulty: "Средний",
        duration: 180,
        fee: 3500,
        status: Status.active
    },
    {
        id: 3,
        master_id: 103,
        technique_id: 203,
        title: "Лепка из полимерной глины",
        dificulty: "Новичок",
        duration: 90,
        fee: 2000,
        status: Status.active
    },
    {
        id: 4,
        master_id: 104,
        technique_id: 204,
        title: "Вышивка золотым шитьём",
        dificulty: "Эксперт",
        duration: 240,
        fee: 5000,
        status: Status.canceled
    },
    {
        id: 5,
        master_id: 105,
        technique_id: 205,
        title: "Граттаж: рисуем скретч-артом",
        dificulty: "Новичок",
        duration: 60,
        fee: 1500,
        status: Status.unactive
    },
    {
        id: 6,
        master_id: 106,
        technique_id: 206,
        title: "Моделирование из бумаги (киригами)",
        dificulty: "Средний",
        duration: 150,
        fee: 2800,
        status: Status.active
    },
    {
        id: 7,
        master_id: 107,
        technique_id: 207,
        title: "Точечная роспись (дот-арт)",
        dificulty: "Средний",
        duration: 120,
        fee: 2200,
        status: Status.canceled
    },
    {
        id: 8,
        master_id: 108,
        technique_id: 208,
        title: "Витражная роспись на стекле",
        dificulty: "Эксперт",
        duration: 200,
        fee: 4200,
        status: Status.active
    },
    {
        id: 9,
        master_id: 109,
        technique_id: 209,
        title: "Скетчинг в городской среде",
        dificulty: "Средний",
        duration: 180,
        fee: 3000,
        status: Status.active
    },
    {
        id: 10,
        master_id: 110,
        technique_id: 210,
        title: "Макраме для начинающих",
        dificulty: "Новичок",
        duration: 100,
        fee: 1800,
        status: Status.active
    }
    ];

    let loading = false;

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
											onclick={() => {}}
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

