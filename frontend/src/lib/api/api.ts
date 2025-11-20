import type {
	MasterDTO,
	Seats,
	UserAddDTO,
	UserDTO,
	WorkshopAllRelDTO,
	WorkshopMasterDTO,
	WorkshopRelDTO
} from '$lib/models.ts';

export async function fetchClosestWorkshop(): Promise<WorkshopMasterDTO> {
	const res = await fetch(`http://127.0.0.1:8000/workshopClosest`);
	if (!res.ok) throw new Error('Ошибка загрузки мастеркласса');
	const data = await res.json();
	return data as WorkshopMasterDTO;
}

export async function fetchMasters(): Promise<MasterDTO[]> {
	const res = await fetch(`http://127.0.0.1:8000/masters`);
	if (!res.ok) throw new Error('Ошибка загрузки мастеров');
	const data = await res.json();
	return data as MasterDTO[];
}

export async function loginUser(username: string, password: string): Promise<boolean> {
	// OAuth2 token endpoint expects application/x-www-form-urlencoded body
	const params = new URLSearchParams();
	params.append('grant_type', 'password');
	params.append('username', username);
	params.append('password', password);

	const res = await fetch('http://127.0.0.1:8000/token', {
		method: 'POST',
		headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
		credentials: 'include', // важно, чтобы браузер принял Set-Cookie
		body: params.toString()
	});

	return res.ok;
}

export async function fetchActiveUser(): Promise<UserDTO | null> {
	const res = await fetch(`http://127.0.0.1:8000/user/info`, {
		method: 'GET',
		credentials: 'include'
	});
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error('Ошибка загрузки информации о пользователе');
	}
	const data = await res.json();
	return data as UserDTO;
}

export async function logoutUser(): Promise<boolean> {
	const res = await fetch(`http://127.0.0.1:8000/logout`, {
		method: 'POST',
		credentials: 'include'
	});
	return res.ok;
}

export async function registerUser(user: UserAddDTO): Promise<boolean> {
	const res = await fetch('http://127.0.0.1:8000/signup', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(user)
	});
	return res.ok;
}

export async function updateUserInfo(user: UserAddDTO) {
	// try to persist — if you have an endpoint, enable this
	const res = await fetch('http://127.0.0.1:8000/user/updateInfo', {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(user)
	});
	return res.ok;
}

export async function fetchWorkshops(): Promise<WorkshopRelDTO[] | null> {
	const res = await fetch('http://127.0.0.1:8000/workshops', {
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include'
	});
	if (res.status === 401) {
		return null;
	} else if (!res.ok) {
		throw new Error('Ошибка загрузки мастеркласса');
	}
	const data = await res.json();
	return data as WorkshopRelDTO[];
}

export async function fetchWorkshopById(workshopId: number): Promise<WorkshopAllRelDTO | null> {
	const res = await fetch(`http://127.0.0.1:8000/workshop/${workshopId}`, {
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
	});
	const data = await res.json();
	return data as WorkshopAllRelDTO;
}

export async function fetchNumberOfSeatsAvalable(sessionId: number): Promise<Seats> {
	const res = await fetch(`http://127.0.0.1:8000/sessionSeatsAvailable/${sessionId}`, {
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
	});

	const data = await res.json()
	return data as Seats
}

export async function bookSessionPost(sessionId:number) {
	const res = await fetch(`http://127.0.0.1:8000/bookSession?session_id=${sessionId}`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include'
	})
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	return res.ok;
}