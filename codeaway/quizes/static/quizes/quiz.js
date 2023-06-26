 

console.log('hello world quiz')
const url =window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
 
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
                 <div class ="mb-2" >
                    <h5><span style="font-weight: 600">${question}</span><h5>
                 </div>
            `

            answers.forEach(answer=>{
                quizBox.innerHTML +=`
                       <div style = 'text-align'>
                           <input type = 'radio' class ='answers' id ="${question}-${answer}" name ="${question}" value ="${answer}">
                           <label for ="${question}"><span style="font-weight: 480">${answer}</span></label>
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
const csrf =document.getElementsByName("csrfmiddlewaretoken")


const sendData = () => {
     const elements =[...document.getElementsByClassName("answers")]
     const data ={}
     data["csrfmiddlewaretoken"] = csrf[0].value
     elements.forEach(el => {
        if (el.checked){
            data[el.name] = el.value
        } else{
            if (!data[el.name]) {
                data[el.name] =  null
            }
        }
     })
     
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data : data,

        success: function(response){
            const results = response.results
            
            quizForm.classList.add('not-visible')
            scoreBox.innerHTML = `${response.passed ? 'Congrats' : 'Ups...!'}   Your result is ${response.score}%`
            
            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question,resp] of Object.entries(res)){
        

                    resDiv.innerHTML += question
                    const cls = ['container','p-3','text-light','h4']
                    resDiv.classList.add(...cls)
                    
                    const answer = resp['answered']
                    const correct = resp['correct_answer']
          
                    if (resp=='not_answered') {
                        resDiv.classList.add('bg-danger')
                        resDiv.innerHTML += `! Correct Answer: ${correct}`
                        resDiv.innerHTML += `! Answered : ${answer}`
                        
                    }
                    else{
                        

                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += `! Answered : ${answer}`
                        }
                        else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += `! Correct Answer: ${correct}`
                            resDiv.innerHTML += `! Answered : ${answer}`
                        }
                    }
                }
                resultBox.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit',e=>{
    e.preventDefault()
    sendData()
})



 

