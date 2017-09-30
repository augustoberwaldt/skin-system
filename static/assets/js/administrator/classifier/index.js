$(document).ready(function(){
    toastr.options = {
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
      "positionClass": "toast-bottom-center",
      "preventDuplicates": false,
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut",
      "showDuration": "0",
      "hideDuration": "0",
      "timeOut": "0",
      "extendedTimeOut": "0",
    };

    $('.remove').click(function(){
       toastr["info"](
           '<div>' +
             '<button  type="button" id="okBtn" class="btn btn-primary">Confirmar</button>' +
             '<button  type="button" id="surpriseBtn" class="btn" >Cancelar</button>' +
           '</div>'
        );
    });

    $('#okBtn').click(function(){

        alert('scascascas');
    });



});