export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0'),
	() => import('./nodes/1'),
	() => import('./nodes/2'),
	() => import('./nodes/3'),
	() => import('./nodes/4'),
	() => import('./nodes/5'),
	() => import('./nodes/6'),
	() => import('./nodes/7'),
	() => import('./nodes/8'),
	() => import('./nodes/9'),
	() => import('./nodes/10'),
	() => import('./nodes/11'),
	() => import('./nodes/12'),
	() => import('./nodes/13'),
	() => import('./nodes/14'),
	() => import('./nodes/15'),
	() => import('./nodes/16'),
	() => import('./nodes/17')
];

export const server_loads = [];

export const dictionary = {
		"/(app)": [~6,[2]],
		"/admin/masters": [14,[5]],
		"/admin/profile": [15,[5]],
		"/admin/users": [16,[5]],
		"/admin/workshops": [17,[5]],
		"/(registration)/login": [7,[3]],
		"/(registration)/logout": [8,[3]],
		"/(user)/orders": [10,[4]],
		"/(user)/profile": [11,[4]],
		"/(user)/schedule": [12,[4]],
		"/(user)/schedule/[id]": [~13,[4]],
		"/(registration)/signup": [~9,[3]]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),
	
	reroute: (() => {}),
	transport: {}
};

export const decoders = Object.fromEntries(Object.entries(hooks.transport).map(([k, v]) => [k, v.decode]));
export const encoders = Object.fromEntries(Object.entries(hooks.transport).map(([k, v]) => [k, v.encode]));

export const hash = false;

export const decode = (type, value) => decoders[type](value);

export { default as root } from '../root.js';