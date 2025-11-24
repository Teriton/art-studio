<script lang="ts">
	import { goto } from "$app/navigation";
	import { fetchPaymentByOrderId, makePayment } from "$lib/api/api";
	import type { PaymentDTO } from "$lib/models";
	import { onMount } from "svelte";
	import SectionWraper from "../SectionWraper.svelte";
    import { PaymentMethod } from "$lib/models";

    let {orderId}: {orderId: number} = $props()

	// Состояния
	let paymentMethod = $state<PaymentMethod>(PaymentMethod.cash); // по умолчанию — на месте
	let cardNumber = $state('');
	let cardExpiry = $state(''); // MM/YY
	let cardCVC = $state('');
	let cardholderName = $state('');
	let loading = $state(false);
	let error: string | null = $state(null);
    let payment: PaymentDTO | null = $state(null);

	// Ошибки
	let errors = $state({
		cardNumber: '',
		cardExpiry: '',
		cardCVC: '',
		cardholderName: ''
	});

	function validateCardFields() {
		let valid = true;
		const newErrors = { cardNumber: '', cardExpiry: '', cardCVC: '', cardholderName: '' };

		if (paymentMethod === PaymentMethod.card) {
			// Проверка номера карты (упрощённо: только цифры и длина 13–19)
			const cleanCard = cardNumber.replace(/\D/g, '');
			if (!/^\d{13,19}$/.test(cleanCard)) {
				newErrors.cardNumber = 'Неверный номер карты';
				valid = false;
			}

			// Проверка срока действия (MM/YY)
			const expiryMatch = cardExpiry.match(/^(\d{2})\/(\d{2})$/);
			if (!expiryMatch) {
				newErrors.cardExpiry = 'Формат: MM/YY';
				valid = false;
			} else {
				const [_, mm, yy] = expiryMatch;
				const month = parseInt(mm, 10);
				const year = parseInt(yy, 10);
				const currentYear = new Date().getFullYear() % 100;
				const currentMonth = new Date().getMonth() + 1;

				if (month < 1 || month > 12 || year < currentYear || (year === currentYear && month < currentMonth)) {
					newErrors.cardExpiry = 'Срок действия истёк';
					valid = false;
				}
			}

			// CVC: 3–4 цифры
			if (!/^\d{3,4}$/.test(cardCVC)) {
				newErrors.cardCVC = 'Неверный CVC';
				valid = false;
			}

			// Имя держателя
			if (!cardholderName.trim()) {
				newErrors.cardholderName = 'Укажите имя на карте';
				valid = false;
			}
		}

		errors = newErrors;
		return valid;
	}

	async function handlePayment() {
		if (!validateCardFields()) return;

		// Здесь — логика отправки данных на сервер
		// Например:
		const res = await makePayment(orderId,paymentMethod);
        if(res) {
            goto("/orders");
        } else {
            error="Ошибка";
        }
		// alert(`Оплата выбрана: ${paymentMethod === 'on-site' ? 'на месте' : 'картой'}`);
		// location.href = '/success';
	}


	async function fetchData() {
		loading = true;
		error = null;
		try {
			payment = await fetchPaymentByOrderId(orderId);
			if (payment === null) {
				goto('/login');
				return;
			}
		} catch (err) {
			console.error(err);
			error = String(err);
		} finally {
			loading = false;
		}
  	}

    onMount(async ()=> {await fetchData()})

</script>

<SectionWraper>
    <main class="flex items-center justify-center mt-10 mx-auto md:mt-[4em] w-full max-w-5xl px-6 py-12">
        <div class="flex w-full max-w-md flex-col items-center gap-6 rounded-xl bg-amber-50/80 p-10 shadow-xl">
            {#if error}
                <p>{error}</p>
            {:else}
                <h1 class="text-center text-3xl font-semibold text-black">Оплата. Заказ №{payment?.id}</h1>
                <h2 class="text-2xl">Стоимость: {payment?.fee} руб.</h2>
                <!-- Выбор способа оплаты -->
                <div class="flex w-full gap-4">
                    <button
                        type="button"
                        onclick={() => (paymentMethod = PaymentMethod.cash)}
                        class={`flex-1 rounded-md py-2 px-4 text-center font-medium transition-colors ${
                            paymentMethod === PaymentMethod.cash
                                ? 'bg-amber-500 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        На месте
                    </button>
                    <button
                        type="button"
                        onclick={() => (paymentMethod = PaymentMethod.card)}
                        class={`flex-1 rounded-md py-2 px-4 text-center font-medium transition-colors ${
                            paymentMethod === PaymentMethod.card
                                ? 'bg-amber-500 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        Картой
                    </button>
                </div>
        
                <!-- Поля для оплаты картой -->
                {#if paymentMethod === PaymentMethod.card}
                    <input
                        type="text"
                        placeholder="Номер карты"
                        bind:value={cardNumber}
                        oninput={() => (errors.cardNumber = '')}
                        class={`w-full rounded-md border px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-400 bg-white/50 ${
                            errors.cardNumber ? 'border-red-500' : 'border-gray-300'
                        }`}
                    />
                    {#if errors.cardNumber}
                        <p class="text-sm text-red-500">{errors.cardNumber}</p>
                    {/if}
        
                    <div class="flex w-full gap-3">
                        <input
                            type="text"
                            placeholder="MM/YY"
                            bind:value={cardExpiry}
                            oninput={() => (errors.cardExpiry = '')}
                            maxlength="5"
                            class={`flex-1 rounded-md border px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-400 bg-white/50 ${
                                errors.cardExpiry ? 'border-red-500' : 'border-gray-300'
                            }`}
                        />
                        <input
                            type="text"
                            placeholder="CVC"
                            bind:value={cardCVC}
                            oninput={() => (errors.cardCVC = '')}
                            maxlength="4"
                            class={`w-24 rounded-md border px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-400 bg-white/50 ${
                                errors.cardCVC ? 'border-red-500' : 'border-gray-300'
                            }`}
                        />
                    </div>
                    {#if errors.cardExpiry || errors.cardCVC}
                        <div class="flex gap-2">
                            {#if errors.cardExpiry}
                                <p class="text-sm text-red-500">{errors.cardExpiry}</p>
                            {/if}
                            {#if errors.cardCVC}
                                <p class="text-sm text-red-500">{errors.cardCVC}</p>
                            {/if}
                        </div>
                    {/if}
        
                    <input
                        type="text"
                        placeholder="Имя на карте"
                        bind:value={cardholderName}
                        oninput={() => (errors.cardholderName = '')}
                        class={`w-full rounded-md border px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-400 bg-white/50 ${
                            errors.cardholderName ? 'border-red-500' : 'border-gray-300'
                        }`}
                    />
                    {#if errors.cardholderName}
                        <p class="text-sm text-red-500">{errors.cardholderName}</p>
                    {/if}
                {/if}
        
                <!-- Подсказка для оплаты на месте -->
                {#if paymentMethod === PaymentMethod.cash}
                    <p class="text-sm text-gray-600 text-center">
                        Оплата будет произведена наличными или картой при получении.
                    </p>
                {/if}
        
                <!-- Кнопка подтверждения -->
                <div class="w-full rounded-md bg-linear-to-l from-[#f87777] to-[#fff7ba] opacity-50 duration-300 hover:opacity-100">
                    <button
                        type="button"
                        onclick={handlePayment}
                        class="w-full rounded-md px-6 py-3 font-bold tracking-wide text-white uppercase focus:ring-2 focus:ring-amber-400 focus:outline-none border-0"
                    >
                        Подтвердить оплату
                    </button>
                </div>
        
                <!-- Ссылка назад -->
                <p class="text-sm font-light text-gray-600">
                    <a class="font-semibold text-black underline" href="/orders">← Вернуться к заказам</a>
                </p>
            {/if}
            </div>
        </main>
</SectionWraper>