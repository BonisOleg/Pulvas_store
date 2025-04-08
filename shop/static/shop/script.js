document.addEventListener('DOMContentLoaded', () => {
    // --- Preloader --- 
    const body = document.body;
    const startTime = Date.now(); // Record start time
    const minDisplayTime = 3500; // Minimum display time in milliseconds (3.5 seconds)
    const fadeOutDelay = 200; // Small delay before starting fade out

    // Ensure preloader is visible initially if JS is enabled
    body.classList.remove('loaded');

    window.addEventListener('load', () => {
        const loadTime = Date.now();
        const elapsedTime = loadTime - startTime;
        const delayNeeded = Math.max(0, minDisplayTime - elapsedTime);

        setTimeout(() => {
            body.classList.add('loaded');
        }, delayNeeded + fadeOutDelay); // Total delay = remaining time + fade out buffer
    });

    const burger = document.querySelector('.burger-menu');
    const mobileNav = document.querySelector('.mobile-nav');

    if (burger && mobileNav) {
        burger.addEventListener('click', () => {
            mobileNav.classList.toggle('is-open');
        });
    }

    const subtitleElement = document.querySelector('.section-subtitle');
    const textToType = "Ми працюємо щоб Ви виглядали розкішно!";
    const typingSpeed = 100; // Milliseconds per character
    const erasingSpeed = 50;
    const delayBeforeErase = 4000; // 4 seconds
    const delayBeforeRestart = 500; // Delay after erasing before restart

    let charIndex = 0;
    let isDeleting = false;

    function typeWriter() {
        if (!subtitleElement) return; // Exit if element not found

        const currentText = textToType.substring(0, charIndex);
        subtitleElement.textContent = currentText;

        if (!isDeleting && charIndex < textToType.length) {
            // Typing
            charIndex++;
            setTimeout(typeWriter, typingSpeed);
        } else if (isDeleting && charIndex > 0) {
            // Erasing
            charIndex--;
            setTimeout(typeWriter, erasingSpeed);
        } else if (!isDeleting && charIndex === textToType.length) {
            // Finished typing, wait before erasing
            isDeleting = true;
            subtitleElement.classList.remove('typing'); // Optional: remove cursor style
            setTimeout(typeWriter, delayBeforeErase);
        } else if (isDeleting && charIndex === 0) {
            // Finished erasing, wait before restarting
            isDeleting = false;
            subtitleElement.classList.add('typing'); // Optional: add cursor style back
            setTimeout(typeWriter, delayBeforeRestart);
        }
    }

    // Start the animation
    if (subtitleElement) {
        subtitleElement.classList.add('typing'); // Optional: initial cursor
        typeWriter();
    }
}); 