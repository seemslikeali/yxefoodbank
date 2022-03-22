var updateBtns = document.getElementsByClassName('button is-danger is-small update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productName= this.dataset.product
        var action = this .dataset.action
        console.log('productName:', productName, 'Action:', action)
    })
}