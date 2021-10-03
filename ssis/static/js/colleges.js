$(() => {
    $('.table').on('click', '.btn-edit', function() {
        id = $(this).data('id')
        location.href = `/colleges/edit?college_code=${id}`;
    });
    $('.table').on('click', '.btn-delete', function(){
        id = $(this).data('id');
        if (confirm(`Delete college with college code "${id}"?`)){
            $.ajax('/api/deleteCollege',{
                method: 'POST',
                data: {id: id},

                success: (res) => {
                    if (res.success){
                        alert("College successfully deleted.")
                        location.reload()
                    }
                }
            });
        }
    });
    $('#searchBtn').click(() => {
        var s = $('#searchInput').val();
        if (s != ""){
            $.ajax('/api/searchCollege',{
                method: 'get',
                data: {keyword: s},

                success: (res) => {
                    $('#tableRows').empty()
                    for (var r of res){
                        var parsedJSON = JSON.parse(r);
                        $('#tableRows').append(`<tr>
                        <td>${parsedJSON.id}</td>
                        <td>${parsedJSON.college_name}</td>
                        <td class="align-to-right">
                            <button class="btn btn-warning btn-edit" data-id=${parsedJSON.id}>Edit</button> 
                            <button class="btn btn-danger btn-delete" data-id=${parsedJSON.id}>Delete</button>
                        </td>
                        </tr>`)
                    }
                }
            });
        }
        else{
            location.reload()
        }
    });
});