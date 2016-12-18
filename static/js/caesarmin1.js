$(function() {


    $('#encmin1').click(function() {
      var toEncrypt = $('#cmin1Enc').val();
        $.ajax({
            url: '/encCaesarMin1',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cmin1Enc').css('border-color' , '#3366FF');
                $('#cmin1Dec').css('border-color' , '#24ff00');
                $('#cmin1Dec').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#decmin1').click(function() {
      var toDecrypt = $('#cmin1Dec').val();
        $.ajax({
            url: '/decCaesarMin1',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cmin1Dec').css('border-color' , '#3366FF');
                $('#cmin1Enc').css('border-color' , '#24ff00');
                $('#cmin1Enc').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
