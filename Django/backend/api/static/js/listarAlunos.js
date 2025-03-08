
async function deletar(id){

    const resposta = await fetch(`/api/user/${id}`, {
        method:'DELETE'
    })
    if(resposta.ok){
        var linhaAluno = document.getElementById(`user-${id}`)
        linhaAluno.remove()
    }

}

function editar(id){
    window.location.href = "/criarAluno/"+id
}