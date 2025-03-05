async function enviarFormulario(evento){
    evento.preventDefault()
    
    var nome = document.getElementById('nome').value
    var email = document.getElementById('email').value
    var senha = document.getElementById('senha').value

    const resposta = await fetch('/api/usuarios/', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({nome: nome, email: email, senha: senha})
    })

    if(resposta.ok){
        window.location.href = "/"
    }



}


var formCadastro = document.getElementById('formCadastro').addEventListener("submit", enviarFormulario)