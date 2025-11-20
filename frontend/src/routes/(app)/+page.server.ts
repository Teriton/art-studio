import { fetchClosestWorkshop, fetchMasters } from '$lib/api/api';
import { openModal } from '$lib/stores/OpenModal.svelte';

export async function load() {
	let workshop = await fetchClosestWorkshop();
	let masters = await fetchMasters();
	return {
		workshop: workshop,
		masters: masters
	};
}
