$(function() {


    $('#encplus1').click(function() {
      var toEncrypt = $('#cplus1Enc').val();
        $.ajax({
            url: '/encCaesarPlus1',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cplus1Enc').css('border-color' , '#3366FF');
                $('#cplus1Dec').css('border-color' , '#24ff00');
                $('#cplus1Dec').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#decplus1').click(function() {
      var toDecrypt = $('#cplus1Dec').val();
        $.ajax({
            url: '/decCaesarPlus1',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#cplus1Dec').css('border-color' , '#3366FF');
                $('#cplus1Enc').css('border-color' , '#24ff00');
                $('#cplus1Enc').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
