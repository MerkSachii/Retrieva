$(function() {


    $('#encemo').click(function() {
      var toEncrypt = $('#emoEnc').val();
        $.ajax({
            url: '/encEmoticon',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#emoEnc').css('border-color' , '#3366FF');
                $('#emoDec').css('border-color' , '#24ff00');
                $('#emoDec').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#decemo').click(function() {
      var toDecrypt = $('#emoDec').val();
        $.ajax({
            url: '/decEmoticon',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#emoDec').css('border-color' , '#3366FF');
                $('#emoEnc').css('border-color' , '#24ff00');
                $('#emoEnc').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
