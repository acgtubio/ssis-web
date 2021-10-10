$(() => {
    $('.table').on('click', '.btn-edit', function() {
        var id = $(this).data('id')
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
});