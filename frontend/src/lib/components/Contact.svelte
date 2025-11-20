<script lang="ts">
	// Данные контактов
	const contactInfo = {
		address: 'просп. Независимости, 62',
		phone: '+375 (29) 221-01-53',
		email: 'artstudio@gmail.com',
		social: [
			{ name: 'Facebook', icon: 'fa-brands fa-facebook-f', url: '#' },
			{ name: 'Instagram', icon: 'fa-brands fa-instagram', url: '#' },
			{ name: 'Twitter', icon: 'fa-brands fa-x-twitter', url: '#' }
		]
	};
</script>

<div class="relative w-full bg-cover bg-center">
	<!-- Контент -->
	<div class="relative z-10 flex h-full flex-col items-start justify-center px-8 py-12 text-white">
		<!-- Заголовок -->
		<h2 class="mb-4 text-4xl leading-tight font-bold">
			Связаться<br />с нами
		</h2>

		<!-- Разделитель -->
		<div class="mb-8 h-1 w-16 bg-red-400"></div>

		<!-- Контакты -->
		<div class="mb-8 space-y-4">
			<!-- Адрес -->
			<div class="flex items-center gap-3">
				<i class="fa-solid fa-house text-red-400"></i>
				<span>{contactInfo.address}</span>
			</div>

			<!-- Телефон -->
			<div class="flex items-center gap-3">
				<i class="fa-solid fa-phone text-red-400"></i>
				<span>{contactInfo.phone}</span>
			</div>

			<!-- Email -->
			<div class="flex items-center gap-3">
				<i class="fa-solid fa-envelope text-red-400"></i>
				<span>{contactInfo.email}</span>
			</div>
		</div>

		<!-- Социальные сети -->
		<div class="mb-8 flex space-x-4">
			{#each contactInfo.social as social}
				<a
					href={social.url}
					target="_blank"
					rel="noopener noreferrer"
					class="flex h-12 w-12 items-center justify-center rounded-full border-2 border-red-400 text-black transition-colors duration-300 hover:bg-red-400 hover:text-white"
					aria-label={social.name}
				>
					<i class={social.icon}></i>
				</a>
			{/each}
		</div>

		<!-- Copyright -->
		<div class="text-sm opacity-80">
			© Copyright <span class="font-semibold">Art Workshop</span>. All Rights Reserved
		</div>
	</div>
</div>

<style>
	@media (max-width: 768px) {
		.text-4xl {
			font-size: 2rem;
		}
		.w-12.h-12 {
			width: 40px;
			height: 40px;
			font-size: 1rem;
		}
	}
</style>
