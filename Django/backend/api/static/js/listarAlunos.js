
async function deletar(id){

    const resposta = await fetch(`/api/alunos/${id}`, {
        method:'DELETE'
    })
    if(resposta.ok){
        var linhaAluno = document.getElementById(`aluno-${id}`)
        linhaAluno.remove()
    }

}

function editar(id){
    window.location.href = "/criarAluno/"+id
}