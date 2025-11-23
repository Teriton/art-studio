<script lang="ts">
	import { PaymentMethod, Status, type PaymentOrderDTO } from "$lib/models";

    let {payment}: {payment:PaymentOrderDTO} = $props()

</script>

<div class="flex flex-col gap-4 rounded-3xl bg-gray-400/40 p-4 shadow-xl">
    <div class="grid grid-flow-col grid-rows-4 md:grid-rows-2">
            <h2 class=" font-semibold text-2xl">Заказ №{payment.id}</h2>
            <h3 class=" font-mediums text-xl">Мастеркласс: {payment.order.session.workshop.title}</h3>
            <p class=" flex items-center row-span-2 md:justify-center text-2xl font-light ">Дата: {payment.order.date}</p>
    </div>
    <div class=" grid grid-cols-2 gap-4 ">
        <p class= "flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Статус: {payment.status}</p>
        <p class="flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Сумма: {payment.fee}</p>
        <p class="flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Место проведения: {payment.order.session.location}</p>
        <p class="flex items-center justify-center bg-gray-600/40 py-3 p-2 shadow-xl rounded-3xl">Продолжительность: {payment.order.session.workshop.duration}</p>
    </div>
    <div class="flex gap-3 justify-centersss text-2xl md:text-xl font-light items-center mt-3">
        <button class=" bg-green-600 h-20 md:h-auto flex-1">Оплатить</button>
        <button class=" bg-red-600 h-20 md:h-auto text-white flex-1">Отменить</button>
    </div>
</div>