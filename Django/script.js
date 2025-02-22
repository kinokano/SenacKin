async function buscarDados(){
    try {
        const response = await fetch("http://127.0.0.1:8000/api/funcionarios/")
        const dados = await response.json()
        console.log(dados)
    } catch (error) {
        
    }
}

buscarDados()