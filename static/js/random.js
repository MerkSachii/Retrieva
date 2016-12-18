$(function() {


    $('#encinno').click(function() {
      var toEncrypt = $('#innoEnc').val();
        $.ajax({
            url: '/encRandom',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#innoEnc').css('border-color' , '#3366FF');
                $('#innoDec').css('border-color' , '#24ff00');
                $('#innoDec').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#decinno').click(function() {
      var toDecrypt = $('#innoDec').val();
        $.ajax({
            url: '/decRandom',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#innoDec').css('border-color' , '#3366FF');
                $('#innoEnc').css('border-color' , '#24ff00');
                $('#innoEnc').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
