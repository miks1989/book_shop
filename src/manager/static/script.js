$('document').ready(function (){
    $('.like-comment').on('click', function (){

    let id=$(this).attr('id')
    console.log($(this))
    console.log('jquery is a power 1234, id = ', id)

    $.ajax({url: '/add_like_ajax',
            data: {'book_id': id.split('-')[1]},
            method: 'GET',
            success: function ( data ){
                $('#' + id).html('LIKKEs: ' + data['count_likes'])
                console.log('get response - ', data)
            }

            })

    });
});


console.log('bye');
