<script lang="ts">
	import About from '$lib/components/AboutPage/AboutMain.svelte';
	import Contact from '$lib/components/Contact.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import Masters from '$lib/components/Masters.svelte';
	import Services from '$lib/components/Services.svelte';
	let { data } = $props();
</script>

<main class="flex flex-col">
	<Hero workshop={data.workshop} />
	<div class=" w-full bg-[url('/assets/backgroud2.jpg')] bg-cover bg-fixed bg-center">
		<Services />
		<Masters masters={data.masters} />
	</div>
	<div class=" w-full bg-[url('/assets/back_33.jpg')] bg-cover bg-fixed bg-center">
		<About />
		<Contact />
	</div>
</main>
