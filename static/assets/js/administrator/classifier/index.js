$(document).ready(function(){


    $('.remove').click(function(){
       toastr.info(
               '<div>' +
                 '<a  type="button" id="okBtn" class="btn btn-primary">Confirmar</a>' +
                 '<a  type="button" id="surpriseBtn" class="btn" >Cancelar</a>' +
               '</div>'
            ,'Deseja realmente excluir ?',
            {
               positionClass: "toast-bottom-center",
               closeButton: false,
               allowHtml: true,
               onShown: function (toast) {
                  $("#okBtn").click(function(){
                    alert('scascasca')
                  });
               }
            }
        );

    });





});