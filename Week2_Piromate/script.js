
const addTaskBtn = document.getElementById('addTaskBtn');
const listContainer = document.getElementById('listContainer');

addTaskBtn.addEventListener('click', addTask );

function addTask() {
    // Disable the Add Task button to prevent multiple inputs
    addTaskBtn.disabled = true;

    // Check if an input field already exists
    if (document.getElementById('taskInput')) {
        console.warn('이미 입력창이 존재합니다. 지금 작업을 완료해주세요.');
        return; // Exit the function if an input field is already present
    }


    //make li tag
    const li = document.createElement('li');
    
    //make input tag
    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('placeholder', '할 일을 입력하세요');
    input.setAttribute('id', 'taskInput');

    //make div tag
    const btn = document.createElement('div');
    btn.classList.add('add-task-btn');
    btn.addEventListener('click', confirmTask );

    //make i tag
    const icon = document.createElement('i');
    icon.classList.add('ri-add-line');

    //append
    btn.appendChild(icon);
    li.appendChild(input);    //append input before btn
    li.appendChild(btn);

    listContainer.appendChild(li);
}

function saveData() {
    localStorage.setItem('data', listContainer.innerHTML); // key, value
}

function showData() {
    listContainer.innerHTML = localStorage.getItem('data');
}
function confirmTask() {
    const taskInput = document.getElementById('taskInput');
    const task = taskInput.value;

    // Check if the input field is empty
    if(task === '') {
        alert('할 일을 입력하세요');
    }
    else{
        const li = document.createElement('li');
        li.innerText = task;
        listContainer.appendChild(li);
        // Remove the task input field and button
        listContainer.removeChild(taskInput.parentElement);
        // taskInput.parentElement.remove();
        // Re-enable the Add Task button

        // Save the data to localStorage
        saveData();
    }
    addTaskBtn.disabled = false;
}


// exception handling for several text input added
// Disable the Add Task button to prevent multiple inputs
// Check if an input field already exists
// Remove the task input field and button
// Re-enable the Add Task button

//implement check button 
listContainer.addEventListener('click', (e) => {
    e.target.classList.toggle('checked');
    // <li class=checked>할일 2</li>
    // console.log(e.target.tagName); => LI
    let checkedTodos = document.getElementById('today').innerText;

    // if(e.target.tagName !== 'INPUT' && e.target.tagName !== 'I'){
    if(e.target.tagName === 'LI'){
        if(e.target.classList.contains('checked')){
            checkedTodos = parseInt(checkedTodos) + 1; // use let since it will be changed
        }
        else if(checkedTodos != 0){
            checkedTodos = parseInt(checkedTodos) - 1;
        }
    }
    document.getElementById('today').innerText = checkedTodos;

  
});


showData();
// localStorage.clear();

// const TODO_LIST_DATA = [
//     "후회없는 여름방학 보내기",
//     "좋은 인연 많이 만들기",
//     "헤맨만큼 내 땅이다! 마음껏 헤매기",
//     "자식같은 프로젝트 해보기",
// ];

// TODO_LIST_DATA.forEach((item) => {
//     const li = document.createElement('li');
//     li.innerText = item;
//     listContainer.appendChild(li); 
// });


const TODO_LIST_DATA = [
    {
    category: "이번 방학",
    todolist: [
        "후회없는 여름방학 보내기",
        "좋은 인연 많이 만들기",
        "헤맨만큼 내 땅이다! 마음껏 헤매기",
        "자식같은 프로젝트 해보기",
    ],
    },
    {
    category: "학교",
    todolist: ["등교하기", "하교하기"],
    },
];

//getElementsByClassName은 배열로 반환
const main = document.getElementsByClassName('main')[0];

//block contains category, todolist
TODO_LIST_DATA.forEach((block) => {
    //create category tag
    const category = document.createElement('div');
    category.classList.add('category');
    //create p tag
    const p = document.createElement('p');
    p.innerText = block.category;
    //create add-task-btn tag
    const btn = document.createElement('div');
    btn.classList.add('add-task-btn');
    btn.setAttribute('id', 'addTaskBtn');
    //create i tag
    const icon = document.createElement('i');
    icon.classList.add('ri-add-line');
    btn.appendChild(icon);

    category.appendChild(p);
    category.appendChild(btn);
    main.appendChild(category);


    //create ul tag
    const ul = document.createElement('ul');
    ul.setAttribute('id', 'listContainer');

    //create li tag
    block.todolist.forEach((item) => {
        const li = document.createElement('li');
        li.innerText = item;
        ul.appendChild(li);
    });
    main.appendChild(ul);
});



// change listContainer into class
// also change in css