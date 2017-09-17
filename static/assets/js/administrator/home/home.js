$(document).ready(function(){
    $('.dropify').dropify({
       messages: {
        'default': 'Arraste e solte um arquivo aqui ou clique em',
        'replace': 'Arraste e solte ou clique para substituir',
        'error'  : 'Ooops, aconteceu algo de errado !'
       }
    });

    var form;
    $('#input-file-now').change(function (event) {
        form = new FormData();
        form.append('fileUpload', event.target.files[0]); // para apenas 1 arquivo

    });

    $('#process').click(function(){
         form.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());

         var html =
             '<li class="collection-item in-progress">' +
                '<p>{{title}}<br>' +
                 '<span class="secondary-content">{{porc}}%</span> ' +
                '</p>'+
                '<div class="progress">'+
                  '<div class="determinate" style="width: {{porc}}%"></div>'+
                '</div>'+
             '</li>';
         var ulTasks = $('#tasks').find('ul');

         if (ulTasks.find('li').size() == 1) {
             $.ajax({
                 url: 'classifier/getDisease',
                 data: form,
                 processData: false,
                 contentType: false,
                 type: 'POST',
                 success: function (data) {

                     var classes = data.images[0].classifiers[0].classes;
                     $.each(classes, function (index, value) {
                         ulTasks.append(html.replace('{{title}}', value.class)
                             .replace('{{porc}}', Math.ceil(value.score * 100))
                             .replace('{{porc}}', Math.ceil(value.score * 100))
                         );
                     });

                 }
             });
         }
    })

});