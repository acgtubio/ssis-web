$( () => {
    $('.btn-delete').click(() => {
        alert($(this).attr('data-id'));
    });

    $('#searchBtn').click(() => {
        // alert($('#searchInput').val());
        confirm('ey');
    });
});