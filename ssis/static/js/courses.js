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
});