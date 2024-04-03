// a JavaScript script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function() {
    function translate() {
        const language = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${language}`, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translate);

    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Enter key code
            translate();
        }
    });
});
