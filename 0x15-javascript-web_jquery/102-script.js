// a JavaScript script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function() {
    $('#btn_translate').click(function() {
        const language = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${language}`, function(data) {
            $('#hello').text(data.hello);
        });
    });
});
