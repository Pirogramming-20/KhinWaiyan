
function toggleFavorite(ideaId) {
    $.ajax({
        url: 'toggle_favorite/',
        type: "POST",
        data: {
            'idea_id': ideaId,
            'csrfmiddlewaretoken': csrfToken
        },
        success: function(response) {
            if (response.success) {
                let favoriteBtn = $('.favorite-btn[data-idea-id=' + ideaId + ']');
                if (response.is_favorite) {
                    favoriteBtn.addClass('favorited');
                } else {
                    favoriteBtn.removeClass('favorited');                }
            }
        }
    });
}


function changeInterest(ideaId, change) {
    let currentInterest = parseInt($('#interest-value-' + ideaId).text(), 10);
    
    // Prevent decrementing below 0
    //prevent the AJAX request from being sent if the interest is already at 0
    if (currentInterest === 0 && change === -1) {
        return;
    }
    $.ajax({
        url: '/change_interest/',  // URL to the Django view that handles the change
        type: 'POST',
        data: {
            'idea_id': ideaId,
            'change': change,
            'csrfmiddlewaretoken': csrfToken
        },
        success: function(response) {
            if (response.success) {
                $('#interest-value-' + ideaId).text(response.new_interest);
            }
        },
        error: function(xhr, status, error) {
            // Handle errors
        }
    });
}