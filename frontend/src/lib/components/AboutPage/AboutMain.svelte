<script lang="ts">
	import SectionWraper from '../SectionWraper.svelte';
	import About from './About.svelte';
	import Feedback from './Feedback.svelte';
</script>

<SectionWraper>
	<div class="relative">
		<div class="absolute inset-0 bg-red-700/40"></div>
		<div class="absolute inset-0 bg-black/40"></div>
		<About />
		<Feedback />
	</div>
</SectionWraper>
