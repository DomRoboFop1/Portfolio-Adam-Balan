// let hello = 'hello';
// hello = 'goodbye';

// const hi = 'hi';

// const currentYear = '2023';
// let currentDate = '2-ого апреля 2023 года';

// const main = document.querySelector('.tiktok__title');
// main.style.color = "red";
const mainTitle = document.getElementById('mainText');

function changeTitleBack() {
    eventTitle.textContent = 'Секция событий';
    eventTitle.style.color = 'white';
}

// showMessage();

function consol() {
    console.log('Вывод в консоль');
}

const eventTitle = document.querySelector('#eventTitle');

function changeTitle() {
    eventTitle.textContent = 'Заменили текст!';
    eventTitle.style.color = 'red';
}

// mainTitle.innerHTML = `<p class="name">Привет, ${prompt('Введите своё имя','Имя')}!</p>`;

const string = 'привет!';
console.log(`Всем ${string}`);

const lightThemeBtn = document.getElementById("light");
const darkThemeBtn = document.getElementById("dark");
const html = document.querySelector("html");

function changeThemeToDark() {
    html.setAttribute("theme", "dark")
}

function changeThemeToLight() {
    html.setAttribute("theme", "light")
}

lightThemeBtn.onclick = changeThemeToLight;
darkThemeBtn.onclick = changeThemeToDark;