let startTime;
let elapsedTime = 0;
let timerInterval;

const startBtn = document.getElementById('start');
const stopBtn = document.getElementById('stop');
const resetBtn = document.getElementById('reset');
const trashBtn = document.getElementById('trash-button');
const selectAllBtn = document.getElementById('selectAll');

startBtn.addEventListener("click", start);
stopBtn.addEventListener("click", stop);
resetBtn.addEventListener("click", reset);
trashBtn.addEventListener('click', trashBtnClick);
selectAllBtn.addEventListener('click', selectAllCheck);

function displayRecord(time) {
  const recordList = document.querySelector(".record-list");
  const recordItem = document.createElement("li");
  recordItem.className = "record-item";
    

    // Create check-button
    const checkButton = document.createElement("button");
    checkButton.className = "check-button";
    const icon = document.createElement("i");
    icon.className = "fa-regular fa-circle";
    checkButton.appendChild(icon);
  
    checkButton.addEventListener("click", checkBtnClick);
  
    // Create record-time element
    const recordTime = document.createElement("div");
    recordTime.className = "record-time";
    recordTime.innerText = time;

    // Append 
    recordItem.appendChild(checkButton);
    recordItem.appendChild(recordTime);

    recordList.appendChild(recordItem);
    
  }
  
  
function formatTime(time) {
  // time is in milliseconds
  let numHours = time / 3600000;
  let hour = Math.floor(numHours);

  let numMins = (numHours - hour) * 60;
  let min = Math.floor(numMins);

  let numSec = (numMins - min) * 60;
  let sec = Math.floor(numSec);

  return `${min.toString().padStart(2, "0")}:${sec.toString().padStart(2, "0")}`;
}

function start() {
  stopBtn.disabled = false;
  timeText = document.getElementById('time');
  startTime = Date.now() - elapsedTime; // timer starts from where it left off
  timerInterval = setInterval(() => {
    elapsedTime = Date.now() - startTime; // calculate time passed since start button is clicked
    time.innerText = formatTime(elapsedTime); // display time passed
  },1000); // 1000ms means do this every second
  startBtn.disabled = true;
}

function stop() {
  clearInterval(timerInterval);
  displayRecord(formatTime(elapsedTime));
  startBtn.disabled = false;
  stopBtn.disabled = true;
}

function reset() {
  clearInterval(timerInterval);
  elapsedTime = 0;
  timeText.innerText = '00:00';
  startBtn.disabled = false;
}


function checkBtnClick(event) {
  const icon = event.target;
  const button = icon.parentElement;
  const recordItem = button.parentElement;

  recordItem.classList.toggle('checked');

  if (recordItem.classList.contains('checked')) {
    icon.className = "fa-solid fa-check-circle";
  } else {
    icon.className = "fa-regular fa-circle";
  }
}



function trashBtnClick() {
  // Select all checked items
  const checkedItems = document.querySelectorAll('.record-item.checked');
  if (checkedItems.length === 0) {
      return;
  }
  checkedItems.forEach(item => {
      item.remove();
  });

  const selectAllIcon = selectAllBtn.querySelector('i');
  selectAllIcon.className = "fa-regular fa-circle";
}



  
  

// Function to toggle all check-buttons
function selectAllCheck() {
  const recordItems = document.querySelectorAll('.record-item');
  const checkButtons = document.querySelectorAll('.check-button i');

  // Check 
  let shouldCheck = false;
  recordItems.forEach(item => {
    if (!item.classList.contains('checked')) {
      shouldCheck = true;
    }
  });
  
  // Toggle 
  recordItems.forEach(item => {
      if (shouldCheck) {
          item.classList.add('checked');
      } else {
          item.classList.remove('checked');
      }
  });

  // Update icons
  checkButtons.forEach(icon => {
      if (shouldCheck) {
          icon.className = "fa-solid fa-check-circle"; 
      } else {
          icon.className = "fa-regular fa-circle"; 
      }
  });
}

// Date.now() returns the number of milliseconds elapsed since January 1, 1970 00:00:00 UTC.
// use setInterval(function,interval) to update the timer every interval
// use clearInterval(intervalId) to stop the interval
// use Math.floor() to round down to the nearest whole number
// use padStart() to add a leading zero if the number is less than 10
// use querySelectorAll() to select all elements 