$( () => {
    $('#gender-2').click(() => {
        $('#customGender').prop('readonly', false);
    });
    $('#gender-0').click(() => {
        $('#customGender').prop('readonly', true);
        $('#customGender').val('');
    });
    $('#gender-1').click(() => {
        $('#customGender').prop('readonly', true);
        $('#customGender').val('');
    });
    $('#photo').change(function() {
        const file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $("#stPhoto")
                  .attr("src", event.target.result);
            };
            reader.readAsDataURL(file);
        }
    })
});