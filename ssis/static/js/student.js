$( () => {
    $('.table').on('click', '.btn-edit', function(){
        var id = $(this).data('id');
        location.href = `/students/edit?id=${id}`
    });
    $('.table').on('click', '.btn-delete', function(){
        var id = $(this).data('id');
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