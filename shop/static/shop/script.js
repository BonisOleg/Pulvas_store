document.addEventListener('DOMContentLoaded', () => {
    // --- Preloader --- 
    const body = document.body;
    const startTime = Date.now(); // Record start time
    const minDisplayTime = 1715; // Reduced minimum display time further by 30% (2450 * 0.7)
    const fadeOutDelay = 200; // Small delay before starting fade out

    // Ensure preloader is visible initially if JS is enabled
    body.classList.remove('loaded');

    // --- Визначаємо, чи це мобільний пристрій (за шириною вікна) --- 
    const isMobile = window.innerWidth < 768;

    window.addEventListener('load', () => {
        const loadTime = Date.now();
        const elapsedTime = loadTime - startTime;
        const delayNeeded = Math.max(0, minDisplayTime - elapsedTime);

        setTimeout(() => {
            body.classList.add('loaded');

            // --- Запуск анімації секцій "Про нас" ПІСЛЯ прелоадера --- 
            const allAboutSections = document.querySelectorAll('.about-section');

            if (isMobile) {
                // --- Мобільна логіка: залишається без змін (тільки перша) --- 
                allAboutSections.forEach((section, index) => {
                    if (index === 0) {
                        section.classList.add('animate-slow');
                        setTimeout(() => {
                            section.classList.add('is-visible');
                        }, 0);
                    }
                });
            } else {
                // --- Десктоп/Планшет логіка: ТІЛЬКИ перша секція --- 
                allAboutSections.forEach((section, index) => {
                    if (index < 1) {
                        section.classList.add('animate-slow');
                        setTimeout(() => {
                            section.classList.add('is-visible');
                        }, 0);
                    }
                });
            }
            // --- Кінець запуску анімації --- 

        }, delayNeeded + fadeOutDelay);
    });

    const burger = document.querySelector('.burger-menu');
    const mobileNav = document.querySelector('.mobile-nav');

    if (burger && mobileNav) {
        burger.addEventListener('click', () => {
            mobileNav.classList.toggle('is-open');
        });
    }

    // --- Typewriter effect for subtitle ON THE HOME PAGE ONLY --- 
    // Шукаємо підзаголовок ТІЛЬКИ всередині секції товарів
    const subtitleElement = document.querySelector('.products-section .section-subtitle');

    // Запускаємо анімацію тільки якщо знайшли цей специфічний підзаголовок
    if (subtitleElement) {
        const textToType = "Ми працюємо щоб Ви виглядали розкішно!"; // Цей текст актуальний для головної
        const typingSpeed = 100;
        const erasingSpeed = 50;
        const delayBeforeErase = 4000;
        const delayBeforeRestart = 500;

        let charIndex = 0;
        let isDeleting = false;

        function typeWriter() {
            if (!subtitleElement) return;

            const currentText = textToType.substring(0, charIndex);
            subtitleElement.textContent = currentText;

            if (!isDeleting && charIndex < textToType.length) {
                charIndex++;
                setTimeout(typeWriter, typingSpeed);
            } else if (isDeleting && charIndex > 0) {
                charIndex--;
                setTimeout(typeWriter, erasingSpeed);
            } else if (!isDeleting && charIndex === textToType.length) {
                isDeleting = true;
                subtitleElement.classList.remove('typing');
                setTimeout(typeWriter, delayBeforeErase);
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                subtitleElement.classList.add('typing');
                setTimeout(typeWriter, delayBeforeRestart);
            }
        }

        // Start the animation
        subtitleElement.classList.add('typing');
        typeWriter();
    } // Кінець умови if (subtitleElement)

    // --- Intersection Observer для анімації решти секцій при прокрутці ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                requestAnimationFrame(() => {
                    entry.target.classList.add('is-visible');
                });
                observer.unobserve(entry.target);
            }
        });
    };

    const intersectionObserver = new IntersectionObserver(observerCallback, observerOptions);

    // Визначаємо, з якої секції починати спостереження
    const startIndexToObserve = isMobile ? 1 : 1;

    const sectionsToObserve = document.querySelectorAll('.about-section');
    sectionsToObserve.forEach((section, index) => {
        if (index >= startIndexToObserve) {
            intersectionObserver.observe(section);
        }
    });
    // --- End Intersection Observer ---

}); 