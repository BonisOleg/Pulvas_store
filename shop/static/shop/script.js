document.addEventListener('DOMContentLoaded', () => {
    // --- Preloader --- 
    const body = document.body;
    const startTime = Date.now(); // Record start time
    const minDisplayTime = 1715; // Reduced minimum display time further by 30% (2450 * 0.7)
    const fadeOutDelay = 200; // Small delay before starting fade out

    // --- Знаходимо форму контактів --- 
    const contactForm = document.querySelector('.contact-form-animate');

    // Ensure preloader is visible initially if JS is enabled
    body.classList.remove('loaded');

    window.addEventListener('load', () => {
        const loadTime = Date.now();
        const elapsedTime = loadTime - startTime;
        const delayNeeded = Math.max(0, minDisplayTime - elapsedTime);

        setTimeout(() => {
            body.classList.add('loaded');

            // --- Анімація перших блоків після прелоадера --- 
            const highlightBlock = document.querySelector('.about-highlight-block');
            const firstAboutSection = document.querySelector('.about-section');

            // Запуск анімації для виділеного блоку
            if (highlightBlock) {
                setTimeout(() => { highlightBlock.classList.add('is-visible'); }, 0);
            }
            // Запуск анімації для першої секції .about-section
            if (firstAboutSection) {
                setTimeout(() => { firstAboutSection.classList.add('is-visible'); }, 0);
            }

            // --- Анімація форми контактів після прелоадера --- 
            if (contactForm) {
                setTimeout(() => { contactForm.classList.add('is-visible'); }, 0);
            }

        }, delayNeeded + fadeOutDelay);
    });

    // --- Mobile Navigation Toggle ---
    const burgerMenu = document.querySelector('.burger-menu');
    const mobileNav = document.querySelector('.mobile-nav');

    if (burgerMenu && mobileNav) {
        burgerMenu.addEventListener('click', function () {
            // Додаємо/прибираємо клас is-open і для навігації, і для іконки бургера
            mobileNav.classList.toggle('is-open');
            burgerMenu.classList.toggle('is-open');

            // Блокуємо/розблоковуємо скрол сторінки
            if (mobileNav.classList.contains('is-open')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Закриття меню при кліку на посилання (якщо потрібно)
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileNav.classList.remove('is-open');
                burgerMenu.classList.remove('is-open');
                document.body.style.overflow = '';
            });
        });
    }
    // --- End Mobile Navigation Toggle ---

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

    // --- Intersection Observer для анімації секцій при скролі --- 
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

    // Спостерігаємо за всіма .about-section, починаючи з другого (індекс 1)
    const sectionsToObserve = document.querySelectorAll('.about-section');
    sectionsToObserve.forEach((section, index) => {
        if (index >= 1) { // Починаємо з індексу 1
            intersectionObserver.observe(section);
        }
    });

    // --- End Intersection Observer ---

    const openModalBtn = document.getElementById('open-filter-modal-btn');
    const modal = document.getElementById('filter-modal');
    const closeModalBtn = modal ? modal.querySelector('.close-modal-btn') : null;
    const modalBackdrop = modal ? modal.querySelector('.modal-backdrop') : null;

    // Перевіряємо, чи всі елементи знайдені
    if (openModalBtn && modal && closeModalBtn && modalBackdrop) {
        // Відкриття модального вікна
        openModalBtn.addEventListener('click', () => {
            modal.classList.add('is-open');
            document.body.style.overflow = 'hidden'; // Забороняємо скрол сторінки під вікном
        });

        // Закриття модального вікна по кнопці
        closeModalBtn.addEventListener('click', () => {
            modal.classList.remove('is-open');
            document.body.style.overflow = ''; // Дозволяємо скрол сторінки
        });

        // Закриття модального вікна по кліку на фон
        modalBackdrop.addEventListener('click', () => {
            modal.classList.remove('is-open');
            document.body.style.overflow = '';
        });

        // Закриття модального вікна по кнопці Escape
        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && modal.classList.contains('is-open')) {
                modal.classList.remove('is-open');
                document.body.style.overflow = '';
            }
        });
    } else {
        // Якщо якийсь елемент не знайдено, виводимо попередження (для відладки)
        // console.warn('Filter modal elements not found. Modal functionality disabled.');
        if (!openModalBtn) console.warn('Button #open-filter-modal-btn not found.');
        if (!modal) console.warn('Modal #filter-modal not found.');
        if (!closeModalBtn) console.warn('Close button .close-modal-btn not found inside modal.');
        if (!modalBackdrop) console.warn('Backdrop .modal-backdrop not found inside modal.');
    }

    // --- Логіка для фіксованих префіксів в полях Telegram --- 
    const telegramUsernameInput = document.getElementById('telegram_username');
    const telegramPhoneInput = document.getElementById('telegram_phone');

    const handleInput = (input, prefix) => {
        if (!input.value.startsWith(prefix)) {
            input.value = prefix;
        }
    };

    const handleKeydown = (event, prefix) => {
        const input = event.target;
        // Забороняємо видалення префіксу через Backspace/Delete
        if ((event.key === 'Backspace' || event.key === 'Delete') && input.selectionStart <= prefix.length && input.selectionEnd <= prefix.length && input.value === prefix) {
            event.preventDefault();
        } else if ((event.key === 'Backspace' || event.key === 'Delete') && input.selectionStart === prefix.length && input.selectionEnd === prefix.length) {
            // Додаткова перевірка: забороняємо видалення, якщо курсор стоїть одразу після префіксу
            event.preventDefault();
        }
    };

    if (telegramUsernameInput) {
        telegramUsernameInput.addEventListener('input', () => handleInput(telegramUsernameInput, '@'));
        telegramUsernameInput.addEventListener('keydown', (e) => handleKeydown(e, '@'));
        // Встановлюємо початковий курсор після префіксу при фокусі
        telegramUsernameInput.addEventListener('focus', () => {
            if (telegramUsernameInput.value === '@') {
                // Невеликий хак з setTimeout, щоб обійти можливі проблеми з встановленням курсору одразу
                setTimeout(() => telegramUsernameInput.setSelectionRange(1, 1), 0);
            }
        });
    }

    if (telegramPhoneInput) {
        telegramPhoneInput.addEventListener('input', () => handleInput(telegramPhoneInput, '+380'));
        telegramPhoneInput.addEventListener('keydown', (e) => handleKeydown(e, '+380'));
        // Встановлюємо початковий курсор після префіксу при фокусі
        telegramPhoneInput.addEventListener('focus', () => {
            if (telegramPhoneInput.value === '+380') {
                setTimeout(() => telegramPhoneInput.setSelectionRange(4, 4), 0);
            }
        });
    }
    // --- Кінець логіки префіксів ---

}); 