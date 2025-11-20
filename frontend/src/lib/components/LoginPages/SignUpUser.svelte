<script lang="ts">
	import { registerUser } from '$lib/api/api';
	import type { UserAddDTO } from '$lib/models';

	let passwordVisible = $state(false);
	let passwordError = $state(false);
	let error = $state('');

	let user = $state<UserAddDTO>({
		first_name: '',
		last_name: '',
		login: '',
		phone_number: '',
		email: '',
		psw: '',
		admin: false
	});
	let repeatPassword = $state('');

	async function handleLogin() {
		if (user.psw !== repeatPassword) {
			passwordError = true;
			return;
		}
		let res = await registerUser(user);
		if (!res) error = 'Ошибка регистрации';
		else location.href = '/login';
	}
</script>

<div class="duration-300">
	<div
		class="flex w-full max-w-md flex-col items-center gap-6 rounded-xl bg-amber-50/80 p-10 shadow-xl"
	>
		<h1 class="text-center text-3xl font-semibold text-black">Регистрация</h1>
		<input
			type="text"
			name="first_name"
			id="first_name"
			placeholder="Имя"
			bind:value={user.first_name}
			class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
		/>

		<input
			type="text"
			name="last_name"
			id="last_name"
			placeholder="Фамилия"
			bind:value={user.last_name}
			class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
		/>
		<input
			type="text"
			name="login"
			id="login"
			placeholder="Логин"
			bind:value={user.login}
			class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
		/>
		<input
			type="text"
			name="phone_number"
			id="phone_number"
			placeholder="Номер телефона"
			bind:value={user.phone_number}
			class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
		/>
		<input
			type="text"
			name="email"
			id="email"
			placeholder="Email"
			bind:value={user.email}
			class="w-full rounded-md border border-gray-300 bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none"
		/>
		<div class="flex w-full items-center gap-1">
			<input
				type={passwordVisible ? 'text' : 'password'}
				name="password"
				id="password"
				placeholder="Пароль"
				bind:value={user.psw}
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
		<input
			type={passwordVisible ? 'text' : 'password'}
			name="repeat_password"
			id="repeat_password"
			placeholder="Повторите пароль"
			bind:value={repeatPassword}
			class={'w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ' +
				(passwordError ? ' border-red-500 text-red-500' : 'border-gray-300')}
		/>

		<div
			class="w-full rounded-md bg-linear-to-l from-[#f87777] to-[#fff7ba] opacity-50 duration-300 hover:opacity-100"
		>
			<button
				type="submit"
				class="w-full rounded-md px-6 py-3 font-bold tracking-wide text-white uppercase focus:ring-2 focus:ring-amber-400 focus:outline-none"
				style="border: 0px;"
				onclick={handleLogin}
			>
				Зарегестрироваться
			</button>
		</div>
		{#if error}
			<div>
				<p class="mt-2 text-sm text-red-500">{error}</p>
			</div>
		{/if}
		<p class="text-sm font-light text-gray-600">
			Уже есть аккаунт ? <a class="font-semibold text-black underline" href="/login">Войти</a>
		</p>
	</div>
</div>
