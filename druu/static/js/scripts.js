//this is for the nav toggle display
document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggle');
    const navList = document.querySelector('.nav-unorder');

    toggleButton.addEventListener('click', function () {
        navList.classList.toggle('show');
    });
});


