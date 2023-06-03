console.log("HelloWorld")


const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start')
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click',() =>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')
     
    modelBody.innerHTML = 
    `<div class = "h5 mb-3">Are you sure you want to begin"<b>${name}</b>
    <div class = "test-muted>
       <ul>
           <li>difficulty : <b>${difficulty}</li>
           <li>no of questions: <b>${numQuestions}</li>
           <li>score to pass : <b>${scoreToPass}</li>
           <li>time : <b>${time}</li>
       </ul>
    `

    startBtn.addEventListener('click',() =>{
         window.location.href = url +pk
    })
    
})) 