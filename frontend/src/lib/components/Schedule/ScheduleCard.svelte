<script lang="ts">
	import { PaymentMethod, Status, PaymentStatus, type OrderRelsDTO, type OrderSessionDTO, type PaymentOrderDTO, type WorkshopRelDTO } from "$lib/models";
	import { fade, fly } from "svelte/transition";

    let modal: boolean = $state(false);
	let { workshop, select, orderPage }: {
        workshop: WorkshopRelDTO,
		select: () => void,
		orderPage: () => void,
    } = $props();

</script>
<div class="gap-4 rounded-3xl bg-gray-400/40 p-4 shadow-xl">
    <h2 class=" font-semibold text-2xl ml-4 md:text-md">{workshop.title}</h2>
    <hr/>
    <div class="flex flex-col md:flex-row md:justify-between md:items-center mt-4 md:p-0">
        <div class="grid grid-flow-col mb-6 md:mb-0 grid-rows-1 md:grid-rows-2">
            <div>
                <p class="text-gray-700 font-light text-xl md:text-base">Мастер</p>
                <p class=" font-mediums text-2xl md:text-base ">{workshop.master.first_name + workshop.master.last_name}</p>
            </div>
            <div>
                <p class="text-gray-700 font-light text-xl md:text-base">Техника</p>
                <p class=" font-mediums text-2xl md:text-base">{workshop.technique.name}</p>
            </div>
        </div>
        <div class=" grid grid-cols-2 gap-4 md:mx-10 md:content-around md:h-full">
            <div class="flex flex-col justify-centerpx-10 py-3 p-2 md:px-10 md:p-2">
                <p class="text-gray-700 font-light text-xl md:text-base">Статус:</p>
                <p class="font-mediums text-2xl md:text-base"> {workshop.status}</p>
            </div>
            <div class="flex flex-col justify-centerpx-10 py-3 p-2 md:px-10 md:p-2">
                <p class="text-gray-700 font-light text-xl md:text-base">Сумма:</p>
                <p class="font-mediums text-2xl md:text-base"> {workshop.fee} руб.</p>
            </div>
            <div class="flex flex-col justify-centerpx-10 py-3 p-2 md:px-10 md:p-2">
                <p class="text-gray-700 font-light text-xl md:text-base">Сложность: </p>
                <p class="font-mediums text-2xl md:text-base"> {workshop.dificulty}</p>
            </div>
            <div class="flex flex-col justify-centerpx-10 py-3 p-2 md:px-10 md:p-2">
                <p class="text-gray-700 font-light text-xl md:text-base">Продолжительность:</p>
                <p class="font-mediums text-2xl md:text-base">{workshop.duration} мин.</p>
            </div>
        </div>
        <div class="flex gap-3 justify-centersss text-2xl md:text-xl font-light items-center mt-6 md:flex-col">
            <button class=" bg-red-600/30 h-15 md:w-full shadow-xl flex-1" onclick={select}>Детали</button>
            <button class=" bg-red-600/30 h-15 md:w-full  flex-1 " onclick={orderPage}>Забронировать</button>
        </div>
    </div>
</div>