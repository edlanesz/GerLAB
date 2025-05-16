function toggleDescricao(button) {
    var descricao = button.previousElementSibling;

    if (descricao.classList.contains('descricao-expandida')) {
        descricao.classList.remove('descricao-expandida');
        button.textContent = 'Mostrar Mais';
    } else {
        descricao.classList.add('descricao-expandida');
        button.textContent = 'Mostrar Menos';
    }
}

function filtrarPorResponsavel() {
    var responsavelSelecionado = document.getElementById('inputResponsavel').value;
    var unidadeSelecionada = document.getElementById('inputUnidade').value;
    var laboratorioSelecionado = document.getElementById('inputLaboratorio').value;
    var equipamentoSelecionado = document.getElementById('inputEquipamento').value;

    var queryParams = '';

    // Adicione os parâmetros de filtro à URL
    if (responsavelSelecionado.trim() !== '') {
        queryParams += '?responsavel=' + encodeURIComponent(responsavelSelecionado);
    }
    if (unidadeSelecionada.trim() !== '') {
        queryParams += (queryParams ? '&' : '?') + 'unidade=' + encodeURIComponent(unidadeSelecionada);
    }
    if (laboratorioSelecionado.trim() !== '') {
        queryParams += (queryParams ? '&' : '?') + 'laboratorio=' + encodeURIComponent(laboratorioSelecionado);
    }
    if (equipamentoSelecionado.trim() !== '') {
        queryParams += (queryParams ? '&' : '?') + 'equipamento=' + encodeURIComponent(equipamentoSelecionado);
    }

    // Redirecionar para a página de filtragem com os parâmetros selecionados
    window.location.href = '/filtrar-por-responsavel/' + queryParams;
}



   function printPage() {
        window.print();
    }