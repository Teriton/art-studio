
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
	// const workshop = await fetchWorkshopById(workshopId);
	// let sessions;
	// if (workshop != null) {
	// 	sessions = organizeSchedulesByDate(workshop.sessions);
	// }

	// return {
	// 	workshop: workshop,
	// 	sessions: sessions,
	// 	error: error
	// };
}
