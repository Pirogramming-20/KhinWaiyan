const slider = document.getElementById('slider');

// getting class using querySelector
const texts = document.querySelector('.text');
//getting child => text.children

// do when input is entered
// event.target.value => value of input
slider.addEventListener('input', (event) => {
    console.log(event)
    for(let text of texts.children) {
        text.style.fontWeight = event.target.value * 10;
    }
})
