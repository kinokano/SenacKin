$carrinho = [['fone' -> 1, 2]]

function validacao


function realizarCompra($idUsuario, $carrinho){
    for ($carrinho as $item){
        insert($idUsuario, $item['idProduto'], $item['qtd'])
    }
}