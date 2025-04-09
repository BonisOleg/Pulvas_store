document.addEventListener('DOMContentLoaded', () => {
    // --- Preloader --- 
    const body = document.body;
    const startTime = Date.now(); // Record start time
    const minDisplayTime = 1715; // Reduced minimum display time further by 30% (2450 * 0.7)
    const fadeOutDelay = 200; // Small delay before starting fade out

    // Ensure preloader is visible initially if JS is enabled
    body.classList.remove('loaded');

    window.addEventListener('load', () => {
        const loadTime = Date.now();
        const elapsedTime = loadTime - startTime;
        const delayNeeded = Math.max(0, minDisplayTime - elapsedTime);

        setTimeout(() => {
            body.classList.add('loaded');

            // --- Trigger animations for the FIRST TWO About Us sections AFTER preloader --- 
            const allAboutSections = document.querySelectorAll('.about-section');
            allAboutSections.forEach((section, index) => {
                if (index < 2) { // Only animate the first two sections here
                    section.classList.add('animate-slow'); // ADD slow animation class
                    // Check if the index is odd (1) to apply right animation
                    if (index % 2 !== 0) {
                        section.classList.add('from-right'); // Гарантовано додаємо клас
                    }
                    // Stagger the animation start time
                    setTimeout(() => {
                        section.classList.add('is-visible');
                    }, index * 200); // Stagger delay
                }
            });
            // --- End Trigger for first two ---

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

    // --- Intersection Observer for animations from the THIRD section onwards ---
    const observerOptions = {
        root: null, // relative to document viewport
        rootMargin: '0px',
        threshold: 0.2 // Trigger when 20% is visible (Adjust if needed)
    };

    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Use requestAnimationFrame to ensure the initial state is rendered first
                requestAnimationFrame(() => {
                    entry.target.classList.add('is-visible');
                });
                observer.unobserve(entry.target); // Stop observing once triggered
            }
        });
    };

    const intersectionObserver = new IntersectionObserver(observerCallback, observerOptions);

    // Observe sections starting from the third one (index 2)
    const sectionsToObserve = document.querySelectorAll('.about-section');
    sectionsToObserve.forEach((section, index) => {
        if (index >= 2) { // Start observing from the third section
            // Check if the index is odd (3, 5, ...) to apply right animation
            if (index % 2 !== 0) {
                section.classList.add('from-right'); // Гарантовано додаємо клас
            }
            intersectionObserver.observe(section);
        }
    });
    // --- End Intersection Observer ---

}); 