<script lang="ts">
	import { page } from '$app/state';
	import { loginUser } from '$lib/api/api';

	let passwordVisible = $state(false);
	let username = $state('');
	let password = $state(''); // TODO: Доработать дизайн глазикаы
	let error = $state('');

	async function handleLogin() {
		let res = await loginUser(username, password);
		if (!res) error = 'Неверный логин или пароль';
		else location.href = '/';
	}
</script>

<div onkeydown={(e)=> {if (e.key == "Enter") handleLogin()}} role="presentation">
	<div
		class="flex w-full max-w-md flex-col items-center gap-6 rounded-xl bg-amber-50/80 p-10 shadow-xl"
	>
		<h1 class="text-center text-3xl font-semibold text-black">Вход</h1>
		<input
			type="text"
			name="username"
			id="username"
			placeholder="Логин"
			bind:value={username}
			class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
		/>
		<div class="flex w-full items-center gap-1">
			<input
				type={passwordVisible ? 'text' : 'password'}
				name="password"
				id="password"
				placeholder="Пароль"
				bind:value={password}
				class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
			/>
			<button class="h-full" onclick={() => (passwordVisible = !passwordVisible)}>
				{#if passwordVisible}
					<i class="fa-solid fa-eye-slash"></i>
				{:else}
					<i class="fa-solid fa-eye"></i>
				{/if}
			</button>
		</div>

		<div
			class="w-full rounded-md bg-linear-to-l from-[#f87777] to-[#fff7ba] opacity-50 duration-300 hover:opacity-100"
		>
			<button
				type="submit"
				class="w-full rounded-md px-6 py-3 font-bold tracking-wide text-white uppercase focus:ring-2 focus:ring-amber-400 focus:outline-none"
				style="border: 0px;"
				onclick={handleLogin}
			>
				Войти
			</button>
		</div>
		{#if error}
			<p class="mt-2 text-sm text-red-500">{error}</p>
		{/if}
		<p class="text-sm font-light text-gray-600">
			У вас нет аккаунта ? <a class="font-semibold text-black underline" href="/signup"
				>Регистрация</a
			>
		</p>
	</div>
</div>
