const requestLike = new XMLHttpRequest();
const requestComment = new XMLHttpRequest();
const requestDeleteComment = new XMLHttpRequest();

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

    const addComment = (postId) => {
        const url = "/add_comment/"

        const formData = new FormData(document.getElementById("comment-form-" + postId));
        formData.append('post_id', postId);

        requestComment.open("POST", url, true);
        requestComment.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        const formObj = {};
        formData.forEach((value, key) => formObj[key] = value);
        requestComment.send(JSON.stringify(formObj)); // send {content: "content", post_id: 1}
    }

    requestComment.onreadystatechange = () => {
        if (requestComment.readyState === XMLHttpRequest.DONE) {
            if (requestComment.status < 400){
                const response = JSON.parse(requestComment.response);
                console.log(response);
                const commentsList = document.getElementById("comments-list-" + response.post_id);
                // add the comment to the list
                //use beforeend to insert after the last child
                commentsList.insertAdjacentHTML( 'beforeend',
                `<div class="comment" id="comment-${response.comment_id}">
                    <span>${response.username}: ${response.content}</span>
                    <button onclick="deleteComment(${response.post_id}, ${response.comment_id})">Delete</button>
                </div>`
            );
            document.getElementById("comment-form-" + response.post_id).reset(); // Clear input field
            }
        }
        else {
            console.error('HTTP Error:', requestComment.statusText);
        }
    }


    const deleteComment = (postId, commentId) => {
        const url = "/delete_comment/"
        requestDeleteComment.open("POST", url, true);
        requestDeleteComment.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        const data = {comment_id: commentId, post_id: postId};
        requestDeleteComment.send(JSON.stringify(data));
    }

    requestDeleteComment.onreadystatechange = () => {
        if (requestComment.readyState === XMLHttpRequest.DONE) {
            if (requestComment.status < 400){
                const response = JSON.parse(requestDeleteComment.response);
                const comment = document.getElementById("comment-" + response.comment_id);
                if (comment) {
                    comment.parentNode.removeChild(comment);
                }
            }
        }
        else {
            console.error('HTTP Error:', requestDeleteComment.statusText);
        }
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
