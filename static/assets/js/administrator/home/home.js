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
    String.prototype.capitalize = function (str) {
     return string.sub(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }


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

        var nenhum = '<li class="collection-item in-progress">' +
                '<p> Nenhum Resultado  <br>' +
                 
                '</p>';



         $.ajax({
             url: 'classifier/getDisease',
             data: form,
             processData: false,
             contentType: false,
             type: 'POST',
             success: function (data) {
                 $("#taskHeader").removeClass("displaynone");
                 var ulTasks = $('#tasks').find('ul');
                 ulTasks.find('li').nextAll('li').remove();
                 //console.log(data);  
          
                 if (data.images[0].classifiers.length > 0) {
                    // console.log('im', data.images[0]); 
                    for (value  in data.images[0].classifiers) {
                       
                         var classes = data.images[0].classifiers[value];
                          
 
                        
                         $.each(classes.classes, function (index, value) {
                           console.log(value);
                       
                          var c = value.class.replace('b', ' '); 
                     
                          ulTasks.append(html.replace('{{title}}',
                               c.toUpperCase())
                              .replace('{{porc}}', Math.ceil(value.score * 100))
                              .replace('{{porc}}', Math.ceil(value.score * 100))
                             );
                        });
                    }

                 } else {
                     ulTasks.append(nenhum);
                    
                 }

                 

             }
         });

    })

});