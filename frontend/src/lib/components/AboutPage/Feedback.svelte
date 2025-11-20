<script lang="ts">
	import { onMount, onDestroy } from 'svelte';

	// Тип отзыва
	interface Review {
		name: string;
		avatar: string;
		text: string;
		rating: number;
	}

	// Массив отзывов
	const reviews: Review[] = [
		{
			name: 'MEOW',
			avatar:
				'https://tse3.mm.bing.net/th/id/OIP.aFoaXiI1hVtcC_0td7papQHaE6?rs=1&pid=ImgDetMain&o=7&rm=3',
			text: 'Пришла на мастер-класс по декупажу с подругой — провели чудесный вечер! Все было продумано до мелочей: от музыки и чая до мельчайших деталей в технике. За пару часов создали две красивые шкатулки. Это не просто обучение — это эмоции, творчество и отдых для души. Обязательно вернёмся!',
			rating: 5
		},
		{
			name: 'BARK',
			avatar: 'https://thumbs.dreamstime.com/b/cute-doggy-3257704.jpg',
			text: 'Решил попробовать что-то новое и записался на мастер-класс по эпоксидной смоле. Думал, это сложно, но оказалось увлекательно и даже медитативно! Всё оборудование и материалы — качественные, инструктор — настоящий профессионал. Теперь у меня дома стоит уникальная подставка под кофе, сделанная своими руками.',
			rating: 5
		},
		{
			name: 'HAPPY HAPPY HAPPY',
			avatar:
				'https://www.acres4dogs.co.uk/wp-content/uploads/2024/12/Doggy-Day-Care-Right-for-Your-Pupp.webp',
			text: 'Посетила мастер-класс по акварели — впервые в жизни рисовала так, чтобы получилось красиво! Преподаватель терпеливо объяснял каждый шаг, атмосфера была очень уютной и вдохновляющей. Ушла с готовой картиной и желанием прийти снова!',
			rating: 5
		}
	];

	// Reactive state
	let currentReviewIndex = $state(0);
	let startX = 0;
	let isDragging = $state(false);
	let isAnimating = $state(false); // Для блокировки свайпа во время анимации

	// Утилиты переключения
	function goToReview(index: number) {
		if (isAnimating || index === currentReviewIndex) return;

		isAnimating = true;
		currentReviewIndex = index;

		// Сброс анимации через 300мс
		setTimeout(() => {
			isAnimating = false;
		}, 300);
	}

	function nextReview() {
		goToReview((currentReviewIndex + 1) % reviews.length);
	}

	function prevReview() {
		goToReview((currentReviewIndex - 1 + reviews.length) % reviews.length);
	}

	// Обработчики свайпа
	function handleTouchStart(e: TouchEvent) {
		if (isAnimating) return;
		startX = e.touches[0].clientX;
		isDragging = true;
	}

	function handleTouchMove(e: TouchEvent) {
		if (!isDragging || isAnimating) return;
		const deltaX = startX - e.touches[0].clientX;
		if (Math.abs(deltaX) > 50) {
			if (deltaX > 0) nextReview();
			else prevReview();
			isDragging = false;
		}
	}

	function handleTouchEnd() {
		isDragging = false;
	}

	// Обработчики мыши
	function handleMouseDown(e: MouseEvent) {
		if (isAnimating) return;
		startX = e.clientX;
		isDragging = true;
	}

	function handleMouseMove(e: MouseEvent) {
		if (!isDragging || isAnimating) return;
		const deltaX = startX - e.clientX;
		if (Math.abs(deltaX) > 50) {
			if (deltaX > 0) nextReview();
			else prevReview();
			isDragging = false;
		}
	}

	function handleMouseUp() {
		isDragging = false;
	}

	// Управление глобальными событиями
	let mouseDownHandler: ((e: MouseEvent) => void) | null = null;
	let mouseMoveHandler: ((e: MouseEvent) => void) | null = null;
	let mouseUpHandler: ((e: MouseEvent) => void) | null = null;

	onMount(() => {
		const container = document.querySelector<HTMLElement>('.review-container');
		if (!container) return;

		const handleMouseDown = (e: MouseEvent) => {
			if (isAnimating) return;
			startX = e.clientX;
			isDragging = true;
		};

		const handleMouseMove = (e: MouseEvent) => {
			if (!isDragging || isAnimating) return;
			const deltaX = startX - e.clientX;
			if (Math.abs(deltaX) > 50) {
				if (deltaX > 0) nextReview();
				else prevReview();
				isDragging = false;
			}
		};

		const handleMouseUp = () => {
			isDragging = false;
		};

		container.addEventListener('mousedown', handleMouseDown);
		document.addEventListener('mousemove', handleMouseMove);
		document.addEventListener('mouseup', handleMouseUp);

		// Cleanup
		return () => {
			container.removeEventListener('mousedown', handleMouseDown);
			document.removeEventListener('mousemove', handleMouseMove);
			document.removeEventListener('mouseup', handleMouseUp);
		};
	});

	onDestroy(() => {
		if (mouseMoveHandler) document.removeEventListener('mousemove', mouseMoveHandler);
		if (mouseUpHandler) document.removeEventListener('mouseup', mouseUpHandler);
	});
</script>

<div class="relative h-screen w-full bg-cover bg-center">
	<div class="text-center">
		<h3 class="text-3xl font-bold text-white">Отзывы</h3>
		<div class="mx-auto mt-2 h-0.5 w-24 bg-red-500 transition-all duration-300"></div>
	</div>
	<div
		class="review-container relative z-10 flex h-full flex-col items-center justify-center px-6 py-12 text-white select-none"
		ontouchstart={handleTouchStart}
		ontouchmove={handleTouchMove}
		ontouchend={handleTouchEnd}
	>
		<!-- Аватар -->
		<div
			class="mb-4 transform transition-all duration-500 ease-out"
			class:scale-110={isAnimating && currentReviewIndex !== undefined}
		>
			<img
				src={reviews[currentReviewIndex].avatar}
				alt="Аватар"
				class="h-32 w-32 rounded-full border-4 border-white object-cover shadow-lg"
				loading="lazy"
			/>
		</div>

		<!-- Имя -->
		<h3
			class="mb-6 transform text-2xl font-bold transition-all duration-500 ease-out"
			class:scale-105={isAnimating}
		>
			{reviews[currentReviewIndex].name}
		</h3>

		<!-- Текст отзыва -->
		<div
			class="mx-auto mb-8 max-w-md transform text-center leading-relaxed transition-all duration-500 ease-out"
			class:opacity-0={isAnimating}
			class:translate-y-4={isAnimating}
			class:opacity-100={true}
			class:-translate-y-0={true}
		>
			{reviews[currentReviewIndex].text}
		</div>

		<!-- Индикаторы -->
		<div class="flex space-x-2">
			{#each reviews as _, i}
				<button
					onclick={() => goToReview(i)}
					style="padding: 0.2em 0.5em;"
					class={`h-1 w-4 cursor-pointer rounded-full  transition-all duration-300 ${
						i === currentReviewIndex
							? 'scale-125 bg-white'
							: 'bg-opacity-50 hover:bg-opacity-75 bg-white'
					}`}
					aria-label={`Перейти к отзыву ${i + 1}`}
				></button>
			{/each}
		</div>
	</div>
</div>

<style>
	@media (max-width: 768px) {
		.max-w-md {
			max-width: 100%;
		}
	}

	.review-container {
		-webkit-user-select: none;
		-moz-user-select: none;
		user-select: none;
		touch-action: pan-y;
	}
</style>
