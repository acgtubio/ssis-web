$( () => {
    $('#searchBtn').click(() => {
        var s = $('#searchInput').val();
        if (s != ""){
            $.ajax('/api/searchStudent',{
                method: 'get',
                data: {keyword: s},

                success: (res) => {
                    $('#studentList').empty()
                    for (var r of res){
                        var parsedJSON = JSON.parse(r);
                        $('#studentList').append(`<tr>
                        <td>${parsedJSON.id}</td>
                        <td>${parsedJSON.firstname}</td>
                        <td>${parsedJSON.lastname}</td>
                        <td>${parsedJSON.course}</td>
                        <td>${parsedJSON.year}</td>
                        <td>${parsedJSON.gender}</td>
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
    $('.table').on('click', '.btn-edit', function(){
        id = $(this).data('id');
        location.href = `/students/edit?id=${id}`
    });
    $('.table').on('click', '.btn-delete', function(){
        id = $(this).data('id');
        if (confirm(`Delete student with ID "${id}"?`)){
            $.ajax('/api/deleteStudent',{
                method: 'POST',
                data: {id: id},

                success: (res) => {
                    if (res.success){
                        alert("User successfully deleted.")
                        location.reload()
                    }
                }
            });
        }
    });
});