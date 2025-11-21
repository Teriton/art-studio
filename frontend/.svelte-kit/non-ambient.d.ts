
// this file is generated — do not edit it


declare module "svelte/elements" {
	export interface HTMLAttributes<T> {
		'data-sveltekit-keepfocus'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-noscroll'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-preload-code'?:
			| true
			| ''
			| 'eager'
			| 'viewport'
			| 'hover'
			| 'tap'
			| 'off'
			| undefined
			| null;
		'data-sveltekit-preload-data'?: true | '' | 'hover' | 'tap' | 'off' | undefined | null;
		'data-sveltekit-reload'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-replacestate'?: true | '' | 'off' | undefined | null;
	}
}

export {};


declare module "$app/types" {
	export interface AppTypes {
		RouteId(): "/(user)" | "/(registration)" | "/(app)" | "/" | "/admin" | "/admin/masters" | "/admin/profile" | "/admin/users" | "/admin/workshops" | "/(registration)/login" | "/(registration)/logout" | "/(user)/orders" | "/(user)/profile" | "/(user)/schedule" | "/(user)/schedule/[id]" | "/(registration)/signup";
		RouteParams(): {
			"/(user)/schedule/[id]": { id: string }
		};
		LayoutParams(): {
			"/(user)": { id?: string };
			"/(registration)": Record<string, never>;
			"/(app)": Record<string, never>;
			"/": { id?: string };
			"/admin": Record<string, never>;
			"/admin/masters": Record<string, never>;
			"/admin/profile": Record<string, never>;
			"/admin/users": Record<string, never>;
			"/admin/workshops": Record<string, never>;
			"/(registration)/login": Record<string, never>;
			"/(registration)/logout": Record<string, never>;
			"/(user)/orders": Record<string, never>;
			"/(user)/profile": Record<string, never>;
			"/(user)/schedule": { id?: string };
			"/(user)/schedule/[id]": { id: string };
			"/(registration)/signup": Record<string, never>
		};
		Pathname(): "/" | "/admin" | "/admin/" | "/admin/masters" | "/admin/masters/" | "/admin/profile" | "/admin/profile/" | "/admin/users" | "/admin/users/" | "/admin/workshops" | "/admin/workshops/" | "/login" | "/login/" | "/logout" | "/logout/" | "/orders" | "/orders/" | "/profile" | "/profile/" | "/schedule" | "/schedule/" | `/schedule/${string}` & {} | `/schedule/${string}/` & {} | "/signup" | "/signup/";
		ResolvedPathname(): `${"" | `/${string}`}${ReturnType<AppTypes['Pathname']>}`;
		Asset(): "/assets/back_33.jpg" | "/assets/backgroud2.jpg" | "/assets/info_back.jpg" | "/assets/info_back1.jpg" | "/assets/pastel1.jpg" | "/assets/reg_back.jpg" | "/img/alcoholink.jpg" | "/img/apple-touch-icon.png" | "/img/art-studio.jpeg" | "/img/back.jpg" | "/img/back1.jpg" | "/img/back2.jpg" | "/img/back3.jpg" | "/img/back_2.jpg" | "/img/back_3.jpg" | "/img/ceramics.jpg" | "/img/dance.sql" | "/img/decoupage.jpg" | "/img/doge1.jpg" | "/img/doge2.png" | "/img/doge3.jpg" | "/img/ebru.jpg" | "/img/epoxyresin.jpg" | "/img/favicon.png" | "/img/home1.jpg" | "/img/homepage.jpg" | "/img/images.jfif" | "/img/img1.jpg" | "/img/img12.jpeg" | "/img/img15.jpg" | "/img/img2.jpg" | "/img/img3.jpg" | "/img/img5.jpg" | "/img/img6.jpg" | "/img/img7.jpg" | "/img/img8.jpg" | "/img/img9.jpg" | "/img/info_back.jpg" | "/img/info_back1.jpg" | "/img/mosaic.jpg" | "/img/new.sql" | "/img/pastel1.jpg" | "/img/pastel2.jpg" | "/img/port1.jfif" | "/img/port2.jfif" | "/img/port3.jpg" | "/img/port4.jpg" | "/img/port5.jpg" | "/img/port6.jpg" | "/img/rajesh.jpg" | "/img/testimonial-2.jpg" | "/img/texture.jpg" | "/img/toa-heftiba-TPfN82nkLTE-unsplash.jpg" | "/img/watercolor.jpg" | "/robots.txt" | string & {};
	}
}