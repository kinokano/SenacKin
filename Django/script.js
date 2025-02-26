// async function buscarDados(){
//     try {
//         const response = await fetch("http://127.0.0.1:8000/api/funcionarios/")
//         const dados = await response.json()
//         console.log(dados)
//     } catch (error) {
        
//     }
// }

// buscarDados()
// const main = document.getElementById('main')
const table = document.getElementById('table')

async function buscarDados(){
    try {
        const response = await fetch("http://127.0.0.1:8000/api/produtos/")
        const dados = await response.json()
        console.log(dados)
        dados.forEach(element => {
            // var conteudo = document.createElement('div')
            var conteudo2 = document.createElement('tr')
            // conteudo.innerHTML = `
            // <h1> ${element.nome} </h1>
            // <p> ${element.descricao} </p>
            // <p> ${element.valor} </p>
            // <p> ${element.quantidade} </p>
            // `
            conteudo2.innerHTML = `
            <td>${element.nome} </td>
            <td> ${element.descricao} </td>
            <td> ${element.valor} </td>
            <td> ${element.quantidade} </td>
            `
            // main.appendChild(conteudo)
            table.appendChild(conteudo2)
        });

    } catch (error) {
        
    }
}

buscarDados()



