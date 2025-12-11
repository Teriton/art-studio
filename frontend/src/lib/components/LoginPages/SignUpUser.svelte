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

	let errors = $state({
		first_name: '',
		last_name: '',
		login: '',
		phone_number: '',
		email: '',
		psw: '',
		repeatPassword: ''
	});

	function validateEmail(emailValue: string): boolean {
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		return emailRegex.test(emailValue);
	}

	function validatePhone(phoneValue: string): boolean {
		const phoneRegex = /^[\d\s\-\+\(\)]+$/;
		return phoneRegex.test(phoneValue) && phoneValue.replace(/\D/g, '').length >= 10;
	}

	function validateLogin(loginValue: string): boolean {
		return loginValue.length >= 3 && /^[a-zA-Z0-9_-]+$/.test(loginValue);
	}

	function validatePassword(passwordValue: string): boolean {
		return passwordValue.length >= 6;
	}

	function validateForm(): boolean {
		let valid = true;
		errors = {
			first_name: '',
			last_name: '',
			login: '',
			phone_number: '',
			email: '',
			psw: '',
			repeatPassword: ''
		};

		if (!user.first_name.trim()) {
			errors.first_name = 'Укажите имя';
			valid = false;
		}

		if (!user.last_name.trim()) {
			errors.last_name = 'Укажите фамилию';
			valid = false;
		}

		if (!user.login.trim()) {
			errors.login = 'Укажите логин';
			valid = false;
		} else if (!validateLogin(user.login)) {
			errors.login = 'Логин: минимум 3 символа, буквы, цифры, - и _';
			valid = false;
		}

		if (!user.phone_number.trim()) {
			errors.phone_number = 'Укажите телефон';
			valid = false;
		} else if (!validatePhone(user.phone_number)) {
			errors.phone_number = 'Телефон должен содержать минимум 10 цифр';
			valid = false;
		}

		if (!user.email.trim()) {
			errors.email = 'Укажите email';
			valid = false;
		} else if (!validateEmail(user.email)) {
			errors.email = 'Некорректный формат email';
			valid = false;
		}

		if (!user.psw.trim()) {
			errors.psw = 'Укажите пароль';
			valid = false;
		} else if (!validatePassword(user.psw)) {
			errors.psw = 'Пароль должен быть минимум 6 символов';
			valid = false;
		}

		if (!repeatPassword.trim()) {
			errors.repeatPassword = 'Повторите пароль';
			valid = false;
		} else if (user.psw !== repeatPassword) {
			errors.repeatPassword = 'Пароли не совпадают';
			passwordError = true;
			valid = false;
		} else {
			passwordError = false;
		}

		return valid;
	}

	async function handleLogin() {
		if (!validateForm()) {
			return;
		}

		let res = await registerUser(user);
		if (!res) error = 'Ошибка регистрации';
		else location.href = '/login';
	}
</script>

<div class="flex justify-center duration-300 w-xl">
	<form
		class="flex w-full max-w-md flex-col items-center gap-6 rounded-xl bg-amber-50/80 p-10 shadow-xl"
		onsubmit={(e) => { e.preventDefault(); handleLogin(); }}
	>
		<h1 class="text-center text-3xl font-semibold text-black">Регистрация</h1>
		<div class="w-full">
			<input
				type="text"
				name="first_name"
				id="first_name"
				placeholder="Имя"
				bind:value={user.first_name}
				oninput={() => (errors.first_name = '')}
				class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
					errors.first_name ? 'border-red-500' : 'border-gray-300'
				}`}
			/>
			{#if errors.first_name}
				<p class="mt-1 text-sm text-red-500">{errors.first_name}</p>
			{/if}
		</div>

		<div class="w-full">
			<input
				type="text"
				name="last_name"
				id="last_name"
				placeholder="Фамилия"
				bind:value={user.last_name}
				oninput={() => (errors.last_name = '')}
				class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
					errors.last_name ? 'border-red-500' : 'border-gray-300'
				}`}
			/>
			{#if errors.last_name}
				<p class="mt-1 text-sm text-red-500">{errors.last_name}</p>
			{/if}
		</div>

		<div class="w-full">
			<input
				type="text"
				name="login"
				id="login"
				placeholder="Логин (минимум 3 символа)"
				bind:value={user.login}
				oninput={() => (errors.login = '')}
				class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
					errors.login ? 'border-red-500' : 'border-gray-300'
				}`}
			/>
			{#if errors.login}
				<p class="mt-1 text-sm text-red-500">{errors.login}</p>
			{/if}
		</div>

		<div class="w-full">
			<input
				type="text"
				name="phone_number"
				id="phone_number"
				placeholder="Номер телефона"
				bind:value={user.phone_number}
				oninput={() => (errors.phone_number = '')}
				class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
					errors.phone_number ? 'border-red-500' : 'border-gray-300'
				}`}
			/>
			{#if errors.phone_number}
				<p class="mt-1 text-sm text-red-500">{errors.phone_number}</p>
			{/if}
		</div>

		<div class="w-full">
			<input
				type="text"
				name="email"
				id="email"
				placeholder="Email"
				bind:value={user.email}
				oninput={() => (errors.email = '')}
				class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
					errors.email ? 'border-red-500' : 'border-gray-300'
				}`}
			/>
			{#if errors.email}
				<p class="mt-1 text-sm text-red-500">{errors.email}</p>
			{/if}
		</div>

		<div class="w-full">
			<div class="gap-1 relative w-full">
				<input
					type={passwordVisible ? 'text' : 'password'}
					name="password"
					id="password"
					placeholder="Пароль (минимум 6 символов)"
					bind:value={user.psw}
					oninput={() => (errors.psw = '')}
					class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
						errors.psw ? 'border-red-500' : 'border-gray-300'
					}`}
				/>
				<button
					type="button"
					class="absolute right-0 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-700 h-full"
					onclick={() => (passwordVisible = !passwordVisible)}
				>
					{#if passwordVisible}
						<i class="fa-solid fa-eye-slash"></i>
					{:else}
						<i class="fa-solid fa-eye"></i>
					{/if}
				</button>
			</div>
			{#if errors.psw}
				<p class="mt-1 text-sm text-red-500">{errors.psw}</p>
			{/if}
		</div>

		<div class="w-full">
			<input
				type={passwordVisible ? 'text' : 'password'}
				name="repeat_password"
				id="repeat_password"
				placeholder="Повторите пароль"
				bind:value={repeatPassword}
				oninput={() => (errors.repeatPassword = '')}
				class={`w-full rounded-md border bg-white/50 px-4 py-3 focus:ring-2 focus:ring-amber-400 focus:outline-none ${
					errors.repeatPassword ? 'border-red-500' : 'border-gray-300'
				}`}
			/>
			{#if errors.repeatPassword}
				<p class="mt-1 text-sm text-red-500">{errors.repeatPassword}</p>
			{/if}
		</div>

		<div
			class="w-full rounded-md bg-linear-to-l from-[#f87777] to-[#fff7ba] opacity-50 duration-300 hover:opacity-100"
		>
			<button
				type="submit"
				class="w-full rounded-md px-6 py-3 font-bold tracking-wide text-white uppercase focus:ring-2 focus:ring-amber-400 focus:outline-none"
				style="border: 0px;"
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
	</form>
</div>
