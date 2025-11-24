<script lang="ts">
	import { PaymentMethod, Status, type OrderRelsDTO, type OrderSessionDTO, type PaymentOrderDTO } from "$lib/models";
	import { onMount } from "svelte";
	import SectionWraper from "../SectionWraper.svelte";
	import OrderCard from "./OrderCard.svelte";
	import { fetchOrders, fetchPayments, cancelOrder } from "$lib/api/api";
	import { goto } from "$app/navigation";

	let loading = $state(false);
	let error: string | null = $state(null);
	let orders: OrderRelsDTO[] | null = $state([]);
	// let selectedWorkshop: WorkshopRelDTO | null = $state(null);

	async function fetchData() {
		loading = true;
		error = null;
		try {
			// Здесь должен быть реальный вызов API, например:
			orders = await fetchOrders();
			if (orders === null) {
				goto('/login');
				return;
			}
			// Для демонстрации используем заглушк
		} catch (err) {
			console.error(err);
			error = String(err);
		} finally {
			loading = false;
		}
  	}

	onMount(async () => {
		await fetchData();
	});

	async function cancelOrderAction(order_id: number) {
		// if (selectedSession === null) return;
		const res = await cancelOrder(order_id)
		if (res === null) goto("/login");
		else await fetchData();
	}
</script>

<SectionWraper>
	<main class="mx-auto mt-10 w-full max-w-5xl px-6 py-12">
		<div class="flex flex-col rounded-xl bg-white/80 p-6 shadow-md backdrop-blur-md">
			<h1 class="md:text-1xl mx-4ss text-3xl font-semibold text-black">
				Заказы
			</h1>
			<hr class="my-4"/>
			{#if !loading}
				{#if orders?.length == 0}
					<h3 class="text-xl">У вас пока нет заказов</h3>
				{:else}
					<div class="flex flex-col gap-6">
						{#each orders as order}
							<OrderCard {order} pay={()=>{}} cancel={async ()=>{await cancelOrderAction(order.id)}}></OrderCard>
						{/each}
					</div>
				{/if}
			{/if}
		</div>
	</main>
</SectionWraper>


