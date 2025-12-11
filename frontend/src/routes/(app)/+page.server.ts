import { fetchClosestWorkshop, fetchMasters } from '$lib/api/api';

export async function load() {
	const workshop = await fetchClosestWorkshop(true);
	const masters = await fetchMasters(true);
	return {
		workshop: workshop,
		masters: masters
	};
}
