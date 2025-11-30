import type {
	MasterAddDTO,
	MasterDTO,
	OrderRelsDTO,
	PaymentDTO,
	PaymentMethod,
	PaymentOrderDTO,
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

export async function fetchPayments(): Promise<PaymentOrderDTO[]| null> {
	const res = await fetch(`http://127.0.0.1:8000/payments`, {
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include'
	})
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	const data = await res.json()
	return data as PaymentOrderDTO[];
}

export async function fetchOrders(): Promise<OrderRelsDTO[]| null> {
	const res = await fetch(`http://127.0.0.1:8000/orders`, {
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include'
	})
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	const data = await res.json()
	return data as OrderRelsDTO[];
}

export async function cancelOrder(order_id: number): Promise<boolean | null> {
	const res = await fetch(`http://127.0.0.1:8000/order/${order_id}`, {
		method: 'DELETE',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include'
	})
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	return true
}

export async function makePayment(order_id: number, payment_method: PaymentMethod): Promise<boolean | null> {
	const res = await fetch(`http://127.0.0.1:8000/order/${order_id}`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify({
			payment_method: payment_method
		})
	})
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	return true
}


export async function fetchPaymentByOrderId(orderId: number): Promise<PaymentDTO | null> {
	const res = await fetch(`http://127.0.0.1:8000/payment_by_order/${orderId}`, {
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
	});
	if (res.status === 401) {
		return null; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	const data = await res.json();
	return data as PaymentDTO;
}

export async function delteUserById(userId:number): Promise<boolean> {
	const res = await fetch(`http://127.0.0.1:8000/admin/user?user_id=${userId}`,{
		method: 'DELETE',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
	});
	if (res.status === 401) {
		return false; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	return true
}

export async function fetchMastersAdmin(): Promise<MasterDTO[] | null> {
	const res = await fetch(`http://127.0.0.1:8000/admin/masters`,{
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
	});
	if (!res.ok) {return null};
	const data = await res.json();
	return data as MasterDTO[];
}

export async function delteMasterById(masterId:number): Promise<boolean> {
	const res = await fetch(`http://127.0.0.1:8000/admin/master?master_id=${masterId}`,{
		method: 'DELETE',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
	});
	if (res.status === 401) {
		return false; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	return true
}

export async function updateMasterById(masterId:number ,master: MasterAddDTO) {
	const res = await fetch(`http://127.0.0.1:8000/admin/master?master_id=${masterId}`, {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(master)
	});
	return res.body;
}

export async function addMasterAdmin(master: MasterAddDTO) {
	const res = await fetch(`http://127.0.0.1:8000/admin/master`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(master)
	});
	return res.body;
}

export async function fetchWorkshopsAdmin(): Promise<WorkshopRelDTO[] | null> {
	const res = await fetch(`http://127.0.0.1:8000/admin/workshops`,{
		method: 'GET',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
	});
	if (!res.ok) {return null};
	const data = await res.json();
	return data as WorkshopRelDTO[];
}

export async function delteWorkshopById(workshopId:number): Promise<boolean> {
	const res = await fetch(`http://127.0.0.1:8000/admin/workshop?workshop_id=${workshopId}`,{
		method: 'DELETE',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
	});
	if (res.status === 401) {
		return false; // Нет активного пользователя
	} else if (!res.ok) {
		throw new Error(`Ошибка ${res.text}`);
	}
	return true
}