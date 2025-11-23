<script lang="ts">
	import { PaymentMethod, Status, type OrderSessionDTO, type PaymentOrderDTO } from "$lib/models";
	import { onMount } from "svelte";
	import SectionWraper from "../SectionWraper.svelte";
	import OrderCard from "./OrderCard.svelte";
	import { fetchOrders, fetchPayments, cancelOrder } from "$lib/api/api";
	import { goto } from "$app/navigation";

	let loading = $state(false);
	let error: string | null = $state(null);
	let orders: OrderSessionDTO[] | null = $state([]);
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

    // const mockPaymentOrderDTO: PaymentOrderDTO = {
	// 	id: 101,
	// 	user_id: 42,
	// 	order_id: 205,
	// 	status: Status.active,
	// 	fee: 2500.0,
	// 	payment_method: PaymentMethod.card,
	// 	order: {
	// 		id: 205,
	// 		user_id: 42,
	// 		schedule_id: 33,
	// 		date: "2025-11-24T14:30:00Z",
	// 		status: Status.active,
	// 		session: {
	// 			id: 33,
	// 			workshop_id: 5,
	// 			date: "2025-11-24T14:30:00Z",
	// 			location: "ул. Ленина, 15",
	// 			numberOfSeats: 12,
	// 			workshop: {
	// 				"master_id": 1,
	// 				"technique_id": 1,
	// 				"title": "Perfaracia",
	// 				"dificulty": "Bolno",
	// 				"duration": 120,
	// 				"fee": 120,
	// 				"status": Status.active,
	// 				"id": 1
	// 			}
	// 		}
	// 	}
    // };

	// let payments: PaymentOrderDTO[] = [];
	// payments.push(mockPaymentOrderDTO)

	

</script>

<SectionWraper>
	<main class="mx-auto mt-10 w-full max-w-5xl px-6 py-12">
		<div class="flex flex-col rounded-xl bg-white/80 p-6 shadow-md backdrop-blur-md">
			<h1 class="md:text-1xl mx-4ss text-3xl font-semibold text-black">
				Заказы
			</h1>
			<hr class="my-4"/>
			{#if !loading}
				<div class="flex flex-col gap-6">
					{#each orders as order}
						<OrderCard {order} pay={()=>{}} cancel={async ()=>{await cancelOrderAction(order.id)}}></OrderCard>
					{/each}
				</div>
			{/if}
		</div>
	</main>
</SectionWraper>