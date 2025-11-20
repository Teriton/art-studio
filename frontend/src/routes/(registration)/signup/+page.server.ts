import type { Actions } from './$types';
import type { UserAddDTO } from '$lib/models';
import { registerUser } from '$lib/api/api';

export const actions = {
	default: async (event) => {
		const data = await event.request.formData();
		const user: UserAddDTO = {
			login: data.get('login') as string,
			psw: data.get('password') as string,
			first_name: data.get('first_name') as string,
			last_name: data.get('last_name') as string,
			email: data.get('email') as string,
			phone_number: data.get('phone_number') as string,
			admin: false
		};
		console.log(user);
		const res = await registerUser(user);
		if (!res) {
			return { success: false, error: 'Ошибка регистрации пользователя' };
		}
		return { success: true };
	}
} satisfies Actions;
