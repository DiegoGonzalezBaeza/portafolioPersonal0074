document.addEventListener('DOMContentLoaded', function () {
    const mainContent = document.querySelector('main');
    mainContent.classList.add('loaded');
});


document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const themeIcon = document.getElementById('theme-icon');

    themeToggleBtn.addEventListener('click', () => {
        // Cambia el tema del body
        const isDark = document.body.classList.toggle('dark-theme');

        // Cambia el ícono
        themeIcon.classList.toggle('bi-moon', !isDark);
        themeIcon.classList.toggle('bi-sun', isDark);

        // Guarda la preferencia en una cookie
        document.cookie = `theme=${isDark ? 'dark' : 'light'}; path=/; max-age=31536000`;
    });
});