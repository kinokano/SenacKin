// async function GetData(){
//     try {
//         const resposta = await fetch('https://fakestoreapi.com/products')
        
//         var dados = await resposta.json()
//         console.log(dados)
//         var lista = document.getElementById("lista")

//         dados.forEach(item => {
//             var conteudo = document.createElement('div')
//             conteudo.className = 'produto'
//             conteudo.innerHTML = `
//                 <img src="${item.image}">
//                 <h3>${item.title}</h3>
//                 <p>${item.price}</p>
//                 `
//             lista.appendChild(conteudo)

//         })
        


//     } catch (error) {
        
//     }

// }

// GetData()

// async function PostData(){
//     const novoProduto = {
//         title: 'novoProduto',
//         price: 13.3,
//         description: "descricao",
//         image: "https://i.pravatar.cc",
//         category: "eletronic"
//     }

//     var resposta = await fetch("https://fakestoreapi.com/products", {
//         method:"POST",
//         headers: {"Content-Type": "application/json"},
//         body: JSON.stringify(novoProduto)
//     })

//     console.log(await resposta.json())


// }

// PostData()


async function API(url, method="GET", body=null, headers={}){
    try {
        const options = {
            method,
            headers:{
                "Content-Type":"application/json",
                ...headers
            }

        }

        if(body){
            options.body = JSON.stringify(body)
        }

        const reposta = await fetch(url, options)
        const dados = await reposta.json()
        return dados

    } catch (error) {
        
    }
}

async function Busca(){
    const resposta = await API("https://fakestoreapi.com/products/1")
    console.log(resposta)
}

Busca()