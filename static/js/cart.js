function addCart(event) {
        var name = document.getElementById(event).parentElement.children[3].textContent;
        var prices = document.getElementById(event).parentElement.children[2].textContent;
        
        if (localStorage.getItem(name) == null){
            var storeThis = {'name': name, 'price': prices, 'quantity': 1};
            localStorage.setItem(name, JSON.stringify(storeThis));
        }
        else{
            var temp = JSON.parse(localStorage.getItem(name));
            temp.quantity++;
            localStorage.setItem(name, JSON.stringify(temp));
        }
}

function addCart1(event) {
        var name = document.getElementById(event).parentElement.children[1].textContent;
        var prices = document.getElementById(event).parentElement.children[2].textContent;
        if (localStorage.getItem(name) == null){
            var storeThis = {'name': name, 'price': prices, 'quantity': 1};
            localStorage.setItem(name, JSON.stringify(storeThis));
        }
        else{
            var temp = JSON.parse(localStorage.getItem(name));
            temp.quantity++;
            localStorage.setItem(name, JSON.stringify(temp));
        }W
}

// ---

function cartItems(){
    if(localStorage.length > 0){
        for (i = 0; i < localStorage.length; i++){

            var key = localStorage.key(i);
            var item = JSON.parse(localStorage.getItem(key));

            var div = document.createElement('div');

            var name = document.createElement("H2");
            name.setAttribute("id", "prodName");
            name.innerHTML = item.name;
            div.appendChild(name);

            var name = document.createElement("p");
            name.setAttribute("id", "prodQty");
            name.innerHTML = item.quantity;
            div.appendChild(name);

            var name = document.createElement("p");
            name.setAttribute("id", "prodPrice");
            name.innerHTML = "$" + item.price * item.quantity;
            
            div.appendChild(name);

            var butt = document.createElement('button');
            butt.onclick= function(){
                var name = this.parentElement.children[0].textContent;
                localStorage.removeItem(name);
                location.reload();
            };
            
            butt.className = 'button2';
            div.appendChild(butt);

            div.className = "cart-item";
            document.getElementById('page-wrapper').appendChild(div);
        }
    }
    
    else{
        var empty = document.createElement('h3');
        empty.innerHTML = "No items in cart...";
        empty.className = "empty-message";
        document.getElementById('page-wrapper').appendChild(empty);
    }

}

function getTotal(){
    if(localStorage.length > 0){
        var total = 0;
        for (i = 0; i < localStorage.length; i++){

            var key = localStorage.key(i);
            var item = JSON.parse(localStorage.getItem(key));
            total += item.price * item.quantity;
        }
        var name = document.createElement("H2");
        name.innerHTML = "subtotal";
        document.getElementById('tot').appendChild(name);
        
        var name = document.createElement("H2");
        name.innerHTML = "$"+total;
        document.getElementById('tot').appendChild(name);
    //
        var name = document.createElement("H2");
        name.innerHTML = "total";
        document.getElementById('tot').appendChild(name);

        var name = document.createElement("H2");
        name.innerHTML = "$"+(total*1.11).toFixed(2);
        document.getElementById('tot').appendChild(name);
    }
}

function thanks(){
    alert("Thank you for shopping.");
}

