import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	let error = '';
	const orderId = parseInt(params.id);

	if (orderId == null) {
		error = 'param is not a num';
		return {
			error: error
		};
	}

    return {
        orderId: orderId
	};
};