document.addEventListener('DOMContentLoaded', function() {
    var image = document.getElementById('robotImage');
    setTimeout(function() {
        image.classList.add('visible');
    }, 100); // Retrasa la animación 0.5 segundos
});
