import { fetchWorkshopById } from '$lib/api/api.js';
import type { ScheduleDTO } from '$lib/models';

function organizeSchedulesByDate(schedules: ScheduleDTO[]): Map<string, ScheduleDTO[]> {
	if (!schedules.length) {
		return new Map();
	}

	// Сортируем все расписания по полной дате (преобразуем строки в Date объекты)
	const sorted = [...schedules].sort((a, b) => {
		const dateA = new Date(a.date).getTime();
		const dateB = new Date(b.date).getTime();
		return dateA - dateB;
	});

	const result = new Map<string, ScheduleDTO[]>();

	for (const schedule of sorted) {
		const dateKey = new Date(schedule.date).toISOString().split('T')[0];

		if (!result.has(dateKey)) {
			result.set(dateKey, []);
		}

		result.get(dateKey)!.push(schedule);
	}

	return result;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export async function load({ params }: {params:any}) {
	let error = '';
	const workshopId = parseInt(params.id);

	if (workshopId == null) {
		error = 'param is not a num';
		return {
			error: error
		};
	}
	const workshop = await fetchWorkshopById(workshopId);
	let sessions;
	if (workshop != null) {
		sessions = organizeSchedulesByDate(workshop.sessions);
	}

	return {
		workshop: workshop,
		sessions: sessions,
		error: error
	};
}
