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
});