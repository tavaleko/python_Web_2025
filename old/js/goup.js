// получить доступ к кнопке
const topBTn = document.querySelector(".go-top")
// скроллинг окна
window.addEventListener("scroll", trackScroll);
// реакция на нажатие
window.addEventListener("click", goTop);

function trackScroll() {
// вычесляем положение от верхушкти окна скролинга
const scrolled = window.pageYOffset;
// высота окна браузера
const wh = document.documentElement.clientHeight;
//в прокрутке вышли за пределы одного экрана
if(scrolled > wh) {
//topBTn.classList.add("go-top--show");
topBtn.style.display = 'block';
} else {
// или исчезает
//topBTn.classList.remove("go-top--show");
topBtn.style.display = 'none';
}
}
function goTop() {
// пока не дошли до верха
if (window.pageYOffset > 0) {
// скролим к верху
window.scrollBy(0,-500); //по У на 28 px
setTimeout(goTop, 0); //рекурсивный вызов самой себя через задержку
}
}