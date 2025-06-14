// let root = document.querySelector(":root");
// let themeButton = document.querySelector("#themeToggle");

// themeButton.addEventListener('click', () => {
// 	event.preventDefault();
// 	root.classList.toggle('dark');
// 	if (themeToggle.textContent === 'Переключить'){
// 		themeToggle.textContent = 'Переключить';
// 	} else {
// 		themeToggle.textContent = 'Переключить';
// 	}
// })

let styleMode = localStorage.getItem('styleMode');
const themeToggle = document.getElementById('themeToggle');

const enableDarkStyle = () => {
    document.body.setAttribute('dark', '')
    localStorage.setItem('styleMode', 'dark');
    themeToggle.checked = true;
}
const disableDarkStyle = () => {
    document.body.removeAttribute('dark');
    localStorage.setItem('styleMode', 'light');
    themeToggle.checked = false;
}

const ChangeTheme = (isChecked) => {
    if (isChecked) {
        enableDarkStyle()
    } else {
        disableDarkStyle()
    }
}

if (styleMode === 'dark') {
    enableDarkStyle();
}

themeToggle.addEventListener('change', (event) => {
    ChangeTheme(event.target.checked);
});