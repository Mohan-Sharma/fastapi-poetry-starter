$(function() {
    $('#upload-form').on('submit', async function(event) {
        event.preventDefault();
        $('#loader').removeClass('hidden');
        $('#download-section').addClass('hidden');

        const formData = new FormData();
        formData.append('file', $('#file')[0].files[0]);

        try {
            const response = await $.ajax({
                url: '/generate',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false
            });

            $('#loader').addClass('hidden');
            $('#download-link').attr('href', `/download/${response.filename}`);
            $('#download-section').removeClass('hidden');
        } catch (error) {
            $('#loader').addClass('hidden');
            let errorMessage = "An error occurred while processing your file.";
            if (error.responseJSON && error.responseJSON.detail) {
                errorMessage = error.responseJSON.detail;
            }
            alert(errorMessage);
        }
    });
});
