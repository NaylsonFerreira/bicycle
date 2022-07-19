const client_http = (url, options) => {
    const token = localStorage.getItem('token');
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const headers = new Headers({
        "Content-Type": "application/json",
        "Authorization": "Token" + token,
        "X-CSRFToken": csrftoken,
        ...options?.headers,
    });
    const request = new Request('/api/' + url, { ...options, headers });
    fetch(request)
        .then(() => document.location.reload(true))
        .catch(console.error);

}


const toggle_menu = () => $('.ui.sidebar').sidebar('toggle');

$(document).ready(function () {

    // Aplicando css do semantic
    $('form').addClass("ui form");
    $('input').addClass("ui input");
    $('select').addClass("ui select dropdown search");
    $(".ui.select[multiple='']").addClass("fluid dropdown");
    // 
    $('.dropdown').dropdown();

});