// getting minus and plus buttons
const minusBtn = document.getElementById("minus");
const plusBtn = document.getElementById("plus");
const countText = document.getElementById("cnt");

//do something on click event
// something => function
// function : calculate the countText

minusBtn.addEventListener("click",  () => {
    countText.innerText = Number(countText.innerText) - 1;
})

plusBtn.addEventListener("click",  () => {
    countText.innerText = Number(countText.innerText) + 1;
})


//onclick method
plusBtn.onclick = () => {
    countText.innerText = Number(countText.innerText) + 1;
}