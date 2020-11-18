function ajaxSend(url, params) {
    // Sending a request
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

// const form = document.querySelector('form[name=filter]');

// form.addEventListener('submit', function (e) {
//     // Recieving form data
//     e.preventDefault();
//     let url = this.action;
//     let params = new URLSearchParams(new FormData(this)).toString();
//     ajaxSend(url, params);
// });

function render(data) {
    // Rendering a template
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.left-ads-display>.row');
    div.innerHTML = output;
}

//Template
let html = '\
{{#films}}\
    <div class="col-md-4 product-men">\
        <div class="product-shoe-info editContent text-center mt-lg-4">\
            <div class="men-thumb-item">\
                <img src="media/{{ poster }}" class="img-fluid" alt="">\
            </div>\
            <div class="item-info-product">\
                <h4 class="">\
                    <a href="/{{ url }}" class="editContent">{{ title }}</a>\
                </h4>\
                <div class="product_price">\
                    <div class="grid-price">\
                        <span class="money editContent">{{ tagline }}</span>\
                    </div>\
                </div>\
                <ul class="stars">\
                    <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-o" aria-hidden="true"></span></a></li>\
                </ul>\
            </div>\
        </div>\
    </div>\
{{/films}}'

//Add rating star

const rating = document.querySelector('form[name=rating]')

rating.addEventListener("change", function (e) {
    // Recieving form data
    let data = new FormData(this)
    
    fetch(`${this.action}`, {
        method: "POST",
        body: data
    })
    .then( response => alert("Rating updated successful"))
    .catch(error => console.error(error))
})