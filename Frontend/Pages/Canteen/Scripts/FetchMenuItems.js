const MenuItemTemplate = document.getElementById('MenuItemTemplate')

let MediaFolder='Media/'
function AddtoMenu(Name,Image){
    const MenuItem=MenuItemTemplate.content.cloneNode(true)
MenuItem.children[0].children[0].src=MediaFolder+Image
MenuItem.children[0].children[1].innerText=Name
document.getElementById('Menu').appendChild(MenuItem)
}

fetch(SERVER_URL+'/Canteen/Menu')
.then(R=>R.json())
.then(data=>{
   return data.Food
})
.then(FoodMenu=>{
   for (const key in FoodMenu) {
    Name=key.split('#')[0]
    console.log(Name)
    AddtoMenu(Name,FoodMenu[key].Image)
   }
})