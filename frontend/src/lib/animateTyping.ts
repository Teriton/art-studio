export function animateTyping(node: HTMLElement, texts: string[]) {
	let index = 0;
	let charIndex = 0;
	let currentText = '';
	let isDeleting = false;

	function type() {
		const fullText = texts[index];
		if (isDeleting) {
			currentText = fullText.substring(0, charIndex--);
		} else {
			currentText = fullText.substring(0, charIndex++);
		}

		node.textContent = currentText;

		if (!isDeleting && charIndex === fullText.length) {
			isDeleting = true;
			setTimeout(type, 1000); // pause before deleting
		} else if (isDeleting && charIndex === 0) {
			isDeleting = false;
			index = (index + 1) % texts.length;
			setTimeout(type, 500); // pause before typing next
		} else {
			setTimeout(type, isDeleting ? 50 : 100);
		}
	}

	type();
}
