<script lang="ts">
	let { children = () => null, id = null } = $props();
</script>

<section {id} class={'mig-h-screen flex flex-col'}>
	<div class="mx-auto flex w-full max-w-[1400px] flex-1 flex-col"></div>
	{@render children?.()}
</section>
