$(function() {


    $('#encmin2').click(function() {
      var toEncrypt = $('#cmin2Enc').val();
        $.ajax({
            url: '/encCaesarMin2',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cmin2Enc').css('border-color' , '#3366FF');
                $('#cmin2Dec').css('border-color' , '#24ff00');
                $('#cmin2Dec').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#decmin2').click(function() {
      var toDecrypt = $('#cmin2Dec').val();
        $.ajax({
            url: '/decCaesarMin2',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cmin2Dec').css('border-color' , '#3366FF');
                $('#cmin2Enc').css('border-color' , '#24ff00');
                $('#cmin2Enc').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
