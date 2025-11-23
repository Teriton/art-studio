import { fetchClosestWorkshop, fetchMasters } from '$lib/api/api';

export async function load() {
	const workshop = await fetchClosestWorkshop();
	const masters = await fetchMasters();
	return {
		workshop: workshop,
		masters: masters
	};
}
