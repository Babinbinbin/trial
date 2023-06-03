console.log('hello world quiz')


$.ajax({
    type: 'GET',
    url: '${url}data',
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    }
})