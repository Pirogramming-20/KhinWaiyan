let attempt = 9;
let randNumbers = [];

//initialize game
function initGame() {
    //generate random number from 0 to 9
    while(randNumbers.length < 3) {
        let rand = Math.floor(Math.random() * 10); 
        //indexOf() returns -1 if the value to search for not exists
        if(randNumbers.indexOf(rand) === -1) {
            randNumbers.push(rand);
        }
    }
    console.log(randNumbers);

    //input & 결과 비우기 
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    document.querySelector('.result-display').innerHTML = '';
    document.getElementById('game-result-img').src = '';   

    //submit button 활성화
    const submitBtn = document.querySelector('.submit-button');
    submitBtn.disabled = false;
}

function check_numbers() {
    const number1 = document.getElementById('number1').value;
    const number2 = document.getElementById('number2').value;
    const number3 = document.getElementById('number3').value;
    const gameResultImg = document.getElementById('game-result-img');
    const submitBtn = document.querySelector('.submit-button');
    inputs = [number1, number2, number3];

    
    //Check if all inputs are filled
    if(inputs.includes('')) {
        alert("모든 숫자를 입력해주세요.");
        return;
    }
    
    //Compare input with randNumbers
    let strikes = 0, balls = 0;
    inputs.forEach((val, idx) => {
        val = parseInt(val);
        //same value & same position
        if(val == randNumbers[idx]) {
            strikes++;
        }
        //same value but different position
        else if(randNumbers.includes(val)) {
            balls++;
        }
    });


    displayResult(inputs, strikes, balls);

    //Decrease the attempt
    attempt--;

    //Display the result image
    if(strikes === 3){
        gameResultImg.src = 'success.png';
        submitBtn.disabled = true;
    }
    else if(attempt === 0) {
        gameResultImg.src = 'fail.png';
        submitBtn.disabled = true;
    }
}

//Display the result
function displayResult(inputs, strikes, balls) {
    const resultDisplay = document.querySelector('.result-display');
    const resultDiv = document.createElement('div');
    resultDiv.className = 'check-result';
    inputStr = inputs.join(' ');
    if(strikes === 0 && balls === 0){
        resultDiv.innerHTML = `
        <div class="left">${inputStr}</div>
        :
        <div class="right">
            <div class="out num-result">O</div>
        </div>
        `;
    }
    else{
        resultDiv.innerHTML = `
        <div class="left">${inputStr}</div>
        :
        <div class="right">
            ${strikes}
            <div class="strike num-result">S</div>
            ${balls}
            <div class="ball num-result">B</div>
        </div>
        `;
    }
    resultDisplay.appendChild(resultDiv);
}

initGame();