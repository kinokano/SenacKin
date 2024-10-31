async function puxarMenu(){
    await fetch('../menu_colaborador/menu_colaborador.html').then(response => response.text()).then(data =>{document.getElementById('menuColaborador').innerHTML = data})
}

puxarMenu()