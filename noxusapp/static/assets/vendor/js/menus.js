const menus = async(id) => {
    let requisicao = await realizarRequisicao({
        origemRequisicao: `${location.origin}/noxus/menus/`,
        conteudoRequisicao: {url: location.pathname},
        tipoRequisicao: "POST"
    })
    let resultado = await requisicao.text()
    resultado = resultado.replaceAll('"', "'")
    document.querySelector(id).innerHTML += resultado
}