async function enviarFormulario(evento){
    evento.preventDefault()
    
    var nome = document.getElementById('nome').value
    var email = document.getElementById('email').value
    var msg = document.getElementById('msg')

    const resposta = await fetch('/api/user/', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username: nome, password: email})
    })

    if(resposta.ok){
        window.location.href = "/home"
    }
    else{
        msg.innerHTML = 'Erro ao cadastrar'
    }


}

var alunoForm = document.getElementById('alunoForm').addEventListener("submit", enviarFormulario)