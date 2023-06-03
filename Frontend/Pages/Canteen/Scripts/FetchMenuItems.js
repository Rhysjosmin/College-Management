
let CART=[]

let MediaFolder='Media/'
function AddtoMenu(Name,ImageID){

    fetch(SERVER_URL+'GetImage/'+ImageID)
    .then(r=>r.json())
    .then(Image=>{
      const item=document.createElement('div')
      item.className='item'
      item.innerHTML=`<img src="${'data:image/jpeg;base64,'+Image.$binary.base64}" alt="">
      <h1>${Name}</h1>`
      item.onclick=()=>{
         item.classList.toggle('SelectedItem')
         if (CART.includes(Name)){
            CART=CART.filter(function (letter) {
               return letter !== Name;
           });
     

         }else{
  
            CART.push(Name)
         }
         // console.log(CART)
      }
      document.getElementById('Menu').appendChild(item)
    
    })

}
function AddToCart(ItemName){

console.log(CART)
}
fetch(SERVER_URL+'/Canteen/Menu')
.then(R=>R.json())
.then(data=>{
   console.log(data)
   return data
})
.then(FoodMenu=>{
   FoodMenu.forEach(element => {
      try {
         AddtoMenu(element.Name,element.Image_ID.$oid)
      } catch (error) {
         console.log(error)
      }
      
   });

})