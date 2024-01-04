// call html node(element)
// find current time
// find end date 
// current time - end date
// put diff time to html

const dateNode = document.querySelector('#date');
const hourNode = document.querySelector('#hour');
const minuteNode = document.querySelector('#minute');
const secondNode = document.querySelector('#second');

//milliseconds -> seconds 1s * 1000ms
const secondToMillisecond = 1000;
const minuteToMillisecond = 60 * secondToMillisecond;
const hourToMillisecond = 60 * minuteToMillisecond;
const dayToMillisecond = 24 * hourToMillisecond;
// 1 day -> 24 * 60 * 60 * 1000 milliseconds
// 1 hour -> 60 * 60 * 1000 milliseconds
// 1 minute -> 60 * 1000 milliseconds
// 1 second -> 1000 milliseconds

function calculateDiffTime() {
    const now = new Date();
    //UTC + 9
    const endDate = new Date("2024-02-20:00:00:00+0900");
    const diffTime = endDate.getTime() - now.getTime();
    
    const date = Math.floor(diffTime / dayToMillisecond);
    const hour = Math.floor(diffTime % dayToMillisecond / hourToMillisecond);
    const minute = Math.floor(diffTime % hourToMillisecond / minuteToMillisecond);
    const second = Math.floor(diffTime % minuteToMillisecond / secondToMillisecond);

    return {date, hour, minute, second};
}


function countdown(){
    const {date, hour, minute, second} = calculateDiffTime();

    dateNode.innerText = String(date).padStart(2, '0');
    hourNode.innerText = String(hour).padStart(2, '0');
    minuteNode.innerText = String(minute).padStart(2, '0');
    secondNode.innerText = String(second).padStart(2, '0')
}

// 1초마다 한번씩 이 함수를 실행한다.
setInterval(() => {
    countdown();
}, 1000);


countdown();
