<script lang="ts">
	import Payment from "$lib/components/PaymentPage/Payment.svelte";
	import { onMount } from "svelte";
	import type { PageProps } from './$types';
	import { goto } from "$app/navigation";

	let { data }: PageProps = $props();

</script>
{#if data.orderId}
	<Payment orderId={data.orderId}></Payment>
{/if}