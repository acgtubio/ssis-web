$(() => {
    $('#tableRows').on('click', '.btn-edit', function(){
        location.href = `/courses/edit?id=${$(this).data('id')}`
    });
    $('#tableRows').on('click', '.btn-delete', function(){
        var id = $(this).data('id');

        if(confirm(`Delete Course with course code '${id}'?`)){
            $.ajax('/api/deleteCourse',{
                method: 'POST',
                data: {id: id},

                success: (res) => {
                    if (res.success){
                        alert("Course successfully deleted.")
                        location.reload()
                    }
                }
            });
        }
    });
    $('#searchBtn').click(() => {
        var s = $('#searchInput').val();
        if (s != ""){
            $.ajax('/api/searchCourse',{
                method: 'get',
                data: {keyword: s},

                success: (res) => {
                    $('#tableRows').empty()
                    for (var r of res){
                        var parsedJSON = JSON.parse(r);
                        $('#tableRows').append(`<tr>
                        <td>${parsedJSON.id}</td>
                        <td>${parsedJSON.course_name}</td>
                        <td>${parsedJSON.college_id}</td>
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