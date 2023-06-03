
console.log('hello world quiz')
const url =window.location.href
const quizBox = document.getElementById('quiz-box')

$.ajax({
    type: 'GET',
    url: `${url}data`,
      
    success: function(response){
        console.log(response)
        data = response.data
        data.forEach(el => {
            console.log(Object.entries(el))
            for([question,answers] of Object.entries(el))
               quizBox.innerHTML +=`
                 <hr>
                 <div clss ="mb-2">
                    <b>${question}</b>
                 </div>
            
            `
            answers.forEach(answer=>{
                quizBox.innerHTML +=`
                       <div>
                           <input type = 'radio' class ='ans' id ="${question}-${answer}" name ="${question}" value ="${answer}">
                           <lable for ="${question}">${answer}</label>
                        </div>
                `
            })

            
        });

    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById("quiz-form")
const csrf =document.getElementsByName('csrfmiddlewaretoken')
const elements =[...document.getElementsByClassName('ans')]