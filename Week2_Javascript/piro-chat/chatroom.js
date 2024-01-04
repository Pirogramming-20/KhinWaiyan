const chatInput = document.getElementById('chat-input');
const hashtagBtn = document.getElementById('hashtag');
const sendBtn = document.getElementById('btn-send');

// change of button & icon on input
chatInput.addEventListener('input', (event) => {
    if(event.target.value !== '') { // chatInput.value can be used
        sendBtn.style.display = 'block';
        hashtagBtn.style.display = 'none';
    }else{
        sendBtn.style.display = 'none';
        hashtagBtn.style.display = 'block';
    }
});

// auto focus on refresh
chatInput.focus();
// enter button same effect as send button
chatInput.addEventListener('keypress', (event) => {
    if(event.code === 'Enter') {
        sendBtn.click();
    }
});
// senBtn click event => show 말풍선

// variable for 왔다갔다
let flag = true; // true: 내가 보낸 말풍선, false: 상대방이 보낸 말풍선
const chatBubbleContainer = document.getElementById('chat-bubble');
sendBtn.addEventListener('click', (event) => {
    if(chatInput.value !== '')  {// if empty, do nothing

    const contentDiv = document.createElement('div'); // creating div element
    // console.log(contentDiv);

    if(flag){
        flag = false;
        // 내 말풍선 띄우기
        /*<div class="my-bubble-content">
            <div class="my-bubble">
            안녕하세요
            </div>
        </div>*/
      contentDiv.className = 'my-bubble-content'; // adding class
      //   console.log(contentDiv);
        const bubble = document.createElement('div');
        bubble.className = 'my-bubble';
        bubble.innerText = chatInput.value;
        // be aware that  bubble is inside my-bubble-content
        contentDiv.appendChild(bubble);
        // console.log(contentDiv);
    }
    else{
        flag = true;
        // 상대방 말풍선 띄우기
        // <div class="your-bubble">
        // <div class="profile">
        //   <img src="./profile.png" alt="">
        // </div>
        // <div class="bubble-content">
        //   <div class="name">교육팀장님</div>
        //   <div class="bubble">
        //     반가워요
        //   </div>
        // </div>
        contentDiv.className = 'your-bubble';
        
        const profileDiv = document.createElement('div');
        profileDiv.className = 'profile';

        const profileImg = document.createElement('img');
        profileImg.src = './profile.png';

        profileDiv.appendChild(profileImg);
        contentDiv.appendChild(profileDiv);

        const bubbleContentDiv = document.createElement('div');
        bubbleContentDiv.className = 'bubble-content';

        const nameDiv = document.createElement('div');
        nameDiv.className = 'name';
        nameDiv.innerText = '교육팀장님';

        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        bubble.innerText = chatInput.value;
        
        bubbleContentDiv.appendChild(nameDiv);
        bubbleContentDiv.appendChild(bubble);
        contentDiv.appendChild(bubbleContentDiv);
    }
    // 말풍선 띄우기
    chatBubbleContainer.appendChild(contentDiv);
    chatInput.value = ''; // clear input
    chatBubbleContainer.scrollTop = chatBubbleContainer.scrollHeight; // scroll to bottom
}});