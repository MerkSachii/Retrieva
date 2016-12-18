$(function() {


    $('#encmin3').click(function() {
      var toEncrypt = $('#cmin3Enc').val();
        $.ajax({
            url: '/encCaesarMin3',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cmin3Enc').css('border-color' , '#3366FF');
                $('#cmin3Dec').css('border-color' , '#24ff00');
                $('#cmin3Dec').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#decmin3').click(function() {
      var toDecrypt = $('#cmin3Dec').val();
        $.ajax({
            url: '/decCaesarMin3',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cmin3Dec').css('border-color' , '#3366FF');
                $('#cmin3Enc').css('border-color' , '#24ff00');
                $('#cmin3Enc').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
