<script lang="ts">
	import { PaymentMethod, Status, PaymentStatus, type OrderRelsDTO, type OrderSessionDTO, type PaymentOrderDTO } from "$lib/models";
	import { fade, fly } from "svelte/transition";

    let modal: boolean = $state(false);
	let { order, pay, cancel } = $props<{
		order: OrderRelsDTO;
		pay: () => void;
		cancel: () => void;
	}>();

</script>

<div class="flex flex-col gap-4 rounded-3xl bg-gray-400/40 p-4 shadow-xl">
    <div class="grid grid-flow-col grid-rows-4 md:grid-rows-2">
            <h2 class=" font-semibold text-2xl">Заказ №{order.id}</h2>
            <h3 class=" font-mediums text-xl">Мастеркласс: {order.session.workshop.title}</h3>
            <p class=" flex items-center row-span-2 md:justify-center text-2xl font-light ">Дата: {order.date}</p>
    </div>
    <div class=" grid grid-cols-2 gap-4 ">
        <p class= "flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Статус: {order.status}</p>
        <p class="flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Сумма: {order.session.workshop.fee} </p>
        <p class="flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Место проведения: {order.session.location}</p>
        <p class="flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Продолжительность: {order.session.workshop.duration}</p>
    </div>
    <div class="flex gap-3 justify-centersss text-2xl md:text-xl font-light items-center mt-3">
        {#if order.payment.status == PaymentStatus.unpaid}
            <button class=" bg-green-600 h-20 md:h-auto flex-1" onclick={async ()=>{
                        await pay()
                        }}>Оплатить</button>
            <button class=" bg-red-600 h-20 md:h-auto text-white flex-1" onclick={()=>{modal = true}}>Отменить</button>
        {:else}
			<div class="flex flex-col md:flex-row rounded-xl p-3 border-2 border-green-600  md:h-auto flex-1">
				<h2 class="flex md:h-auto flex-1 items-center justify-center">Оплачено</h2>
				<h2 class="flex  md:h-auto flex-1 items-center justify-center">Способ оплаты: {order.payment.payment_method == PaymentMethod.card? "картой" : "на месте"}</h2>
			</div>
			{/if}
		</div>
</div>


{#if modal}
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
					modal = false;
				}}>✕</button
			>
			<div class="grid grid-cols-2 gap-4 md:gap-2">
                <h1 class="text-xl col-span-2">Вы уверены?</h1>
				<button
					class="block w-full shadow-md bg-amber-100 border-amber-50 text-center transition-colors"
					onclick={async ()=>{
                        await cancel()
                        modal = false;
                        }}
				>
					Да
				</button>
                <button
					class="block w-full shadow-md bg-amber-100 border-amber-50 text-center transition-colors"
					onclick={()=>{modal=false}}
				>
					Нет
				</button>
			</div>
		</div>
	</div>
{/if}
