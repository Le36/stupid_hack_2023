function createStar() {
    const star = document.createElement('div');
    star.classList.add('star');

    star.style.left = Math.random() * 100 + 'vw';
    star.style.top = Math.random() * 100 + 'vh';
    star.style.transform = `rotate(${Math.random() * 360}deg)`;

    star.style.width = `${Math.random() * 50}px`;
    star.style.height = star.style.width;

    document.body.appendChild(star);

    setTimeout(() => {
        star.remove();
    }, 5000);
}

setInterval(createStar, 50);