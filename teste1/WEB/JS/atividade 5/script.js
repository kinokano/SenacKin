const form = document.getElementById("form")
const usuario = document.getElementById("usuario")
const senha = document.getElementById("senha")

function ShowError(input, mensagem){
    const formControl = input.parentElement
    formControl.className = "form-control error"
    const small = formControl.querySelector("small")
    small.innerHTML = mensagem
}
function ShowSucesso(input){
    const formControl = input.parentElement
    formControl.className = "form-control sucesso"
}

function checkRequired(listaInput){

    let valido = true
    listaInput.forEach(function (input) {
        if(input.value == ""){
            ShowError(input,"Campo obrigatorio")
            valido = false
        }else{
            ShowSucesso(input)
        }
    })
    return valido

}

function CheckSize(input,max,min){
    let valido = true
    if(input.value.length < min){
        ShowError(input,`Tem que ter no minimo ${min}`)
        valido = false
    }else if(input.value.length > max){
        ShowError(input, `Maior que ${max}`)
        valido = false
    }
    return valido
} 

form.addEventListener("submit",function(event) {
    event.preventDefault()
    let isValid = checkRequired([usuario,senha])

    isValid = CheckSize(usuario,15,3) && isValid
    isValid = CheckSize(senha,15,3) && isValid

    if(isValid){
        const dados = {
            usuarioNome: usuario.value,
            usuarioSenha: senha.value
        }
       console.log(dados)

       window.location.href = "./home.html"
    }
})
