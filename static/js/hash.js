$(function() {


    $('#encmd5').click(function() {
      var toEncrypt = $('#md5en').val();
        $.ajax({
            url: '/encMD5',
            data: {'plainText': toEncrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#md5en').css('border-color' , '#3366FF');
                $('#md5out').css('border-color' , '#24ff00');
                $('#md5out').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });

    $('#encsha').click(function() {
      var toDecrypt = $('#shaen').val();
        $.ajax({
            url: '/encSHA',
            data: {'plainText': toDecrypt},
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log('Success!!!');
                $('#shaen').css('border-color' , '#3366FF');
                $('#shaout').css('border-color' , '#24ff00');
                $('#shaout').val(response)
            },
            error: function(error) {
                console.log('Error!!!')
                console.log(error);

            }
        });
    });
});
