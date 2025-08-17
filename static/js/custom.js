document.addEventListener('DOMContentLoaded', () => {
    const topAppBarElement = document.querySelector('.mdc-top-app-bar');
    if (topAppBarElement) {
        const topAppBar = new mdc.topAppBar.MDCTopAppBar(topAppBarElement);
    }

    const buttons = document.querySelectorAll('.mdc-button');
    buttons.forEach(button => {
        mdc.ripple.MDCRipple.attachTo(button);
    });

    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-theme');
        });
    }
});