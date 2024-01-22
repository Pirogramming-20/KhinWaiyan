const requestLike = new XMLHttpRequest();

    const onClickLike = (id) => {
        const url = "/toggle_like/"
        requestLike.open("POST", url, true);
        requestLike.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        requestLike.send(JSON.stringify({ post_id: id }));
    }

    requestLike.onreadystatechange = () => {
        if (requestLike.readyState === XMLHttpRequest.DONE){
            if (requestLike.status < 400){
                const response = JSON.parse(requestLike.response);
                const { post_id, like_count, is_liked } = JSON.parse(requestLike.response);
                console.log(`Response Post ID: ${post_id}, Like Count: ${like_count}, Is Liked: ${is_liked}`);
                const likeButton = document.querySelector(`.like-btn[data-post-id="${post_id}"] i`);
                const likeCountElement = document.querySelector(`.like-count[data-post-id="${post_id}"]`);
                if (is_liked) {
                    likeButton.classList.remove('fa-regular');
                    likeButton.classList.add('fa-solid');

                } else {
                    likeButton.classList.remove('fa-solid');
                    likeButton.classList.add('fa-regular');
                }

                likeCountElement.innerHTML = `${like_count} likes`;  
            }
        }
    };

// Toggle comment box 
// function toggleCommentBox(postId) {
//     var commentSection = document.getElementById("comments" + postId);
//     if (commentSection.style.display === "none") {
//         commentSection.style.display = "block";
//     } else {
//         commentSection.style.display = "none";
//     }
// }

// Add a comment
function addComment(postId) {
    const req = new XMLHttpRequest();
    const formData = new FormData(document.getElementById("comment-form-" + postId));
    formData.append('post_id', postId); // Add post_id to FormData
    // Send POST request
    const url = "/add_comment/"
    req.open('POST', url , true); 

    req.onload = function () {
        if (this.status >= 200 && this.status < 300) {
            var response = JSON.parse(this.responseText);
            // Append new comment to comments list
            var commentsList = document.getElementById("comments-list-" + postId);
            commentsList.insertAdjacentHTML('beforeend', 
                `<div class="comment" id="comment-${response.comment_id}">
                    <span>${response.username}: ${response.content}</span>
                    <button onclick="deleteComment(${postId}, ${response.comment_id})">Delete</button>
                </div>`
            );
            // Clear input field
            document.getElementById("comment-form-" + postId).reset();
        }
    };
    req.send(formData);
}

// Delete a comment
function deleteComment(postId, commentId) {
    var req = new XMLHttpRequest();
    req.open('POST', '/delete_comment/', true); // Adjust URL as needed
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    req.onload = function () {
        if (this.status >= 200 && this.status < 300) {
            // Remove comment from comments list
            var comment = document.getElementById("comment-" + commentId);
            comment.parentNode.removeChild(comment);
        }
    };
    req.send('comment_id=' + commentId);
}



function deletePost(postId) {
    if (confirm("Are you sure you want to delete this post?")) {
        var req = new XMLHttpRequest();
        req.open('POST', '/delete_post/', true); // Adjust URL as needed
        req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        req.onload = function () {
            if (this.status >= 200 && this.status < 300) {
                // Remove post element from the page
                var postElement = document.getElementById("post-" + postId);
                postElement.parentNode.removeChild(postElement);
            }
        };
        req.send('post_id=' + postId);
    }
}
