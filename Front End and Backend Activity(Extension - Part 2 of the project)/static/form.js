function my_magic_function(val){
    //modal.find('.modal-title').text('New message to ' + var);
   console.log(val);
   document.getElementById("result").innerHTML="Status : "+ val.toString();
}

$(document).ready(function () {
 $('form').on('submit', function (event) {
     $.ajax({
         data: JSON.stringify({
             Amount: $('#amountInput').val(),
             Time: $('#timeInput').val()
         }),
         type: 'POST',
         url: '/process',
         dataType: 'json',
         success : function(response){
         
             value = response.message;
 
               my_magic_function(value);
 
          }
     })

     error: (error) => {
         console.log(JSON.stringify(error));
     }
     event.preventDefault();

 });
});


function onClickedSubmitBtn(){
 console.log("Submit button clicked");
}