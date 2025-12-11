<script lang="ts">
	import { PaymentMethod, Status, type OrderRelsDTO, type OrderSessionDTO, type PaymentOrderDTO } from "$lib/models";
	import { onMount } from "svelte";
	import SectionWraper from "../SectionWraper.svelte";
	import OrderCard from "./OrderCard.svelte";
	import { fetchOrders, fetchPayments, cancelOrder } from "$lib/api/api";
	import { goto } from "$app/navigation";
	import { fade, fly } from "svelte/transition";

	let loading = $state(false);
	let error: string | null = $state(null);
	let orders: OrderRelsDTO[] | null = $state([]);
	let selectedOrder: OrderRelsDTO | null = $state(null);

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
							<OrderCard {order} pay={()=>{goto(`/orders/${order.id}`)}} select={()=>{selectedOrder = order}}></OrderCard>
						{/each}
					</div>
				{/if}
			{/if}
		</div>
	</main>
</SectionWraper>


{#if selectedOrder}
	<div
		class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 transition-opacity duration-300 p-4"
		transition:fade
	>
		<div
			class="animate-fade-in relative w-full max-w-md rounded-lg bg-white p-6 shadow-xl"
			transition:fly={{ y: 100, duration: 300 }}
		>
			<button
				class="absolute top-2 right-2 text-gray-500 hover:text-gray-800"
				onclick={() => {
					selectedOrder = null;
				}}>✕</button
			>
			<div class="grid grid-cols-2 gap-4 md:gap-2">
                <h1 class="text-xl col-span-2">Вы уверены?</h1>
				<button
					class="block w-full shadow-md bg-amber-100 border-amber-50 text-center transition-colors"
					onclick={async ()=>{
						if (selectedOrder) await cancelOrderAction(selectedOrder.id);
                        selectedOrder = null;
                        }}
				>
					Да
				</button>
                <button
					class="block w-full shadow-md bg-amber-100 border-amber-50 text-center transition-colors"
					onclick={()=>{selectedOrder=null}}
				>
					Нет
				</button>
			</div>
		</div>
	</div>
{/if}
