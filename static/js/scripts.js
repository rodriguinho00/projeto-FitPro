/* ================================================
   FitPro Academia — JavaScript Premium (2026)
   Desenvolvido por: Rodrigo Santos
   Funcionalidades: Confirmações, Alertas, Interatividade
   ================================================ */

// Aguarda o carregamento completo do DOM (HTML) antes de executar o script
document.addEventListener('DOMContentLoaded', function () {

    // ── 1. Confirmação ao clicar em Excluir ──────────────────────────────
    // Seleciona todos os botões que possuem a classe 'btn-excluir'
    const botoesExcluir = document.querySelectorAll('.btn-excluir');
    
    // Adiciona um evento de clique para cada botão encontrado
    botoesExcluir.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault(); // Impede o comportamento padrão do botão
            
            // Pega o nome do registro que está no atributo 'data-nome' do botão
            const nome = btn.getAttribute('data-nome') || 'este registro';
            
            // Exibe uma caixa de confirmação personalizada
            const confirmar = confirm(
                '⚠️ ATENÇÃO!\n\nDeseja realmente excluir "' + nome + '"?\n\n' +
                'Esta ação NÃO pode ser desfeita!'
            );
            
            // Se o usuário clicar em "Cancelar", a ação é interrompida
            if (!confirmar) {
                return false;
            }
            
            // Se clicar em "OK", exibe um alerta simulando a exclusão
            alert('✅ Registro "' + nome + '" excluído com sucesso!\n(Simulado para fins de demonstração)');
        });
    });

    // ── 2. Auto-fechar alertas após 5 segundos ────────────────────────────
    // Seleciona alertas de sucesso e informativos
    const alertas = document.querySelectorAll('.alert.alert-success, .alert.alert-info');
    alertas.forEach(function (alerta) {
        // Define um temporizador de 5000 milissegundos (5 segundos)
        setTimeout(function () {
            // Usa a API do Bootstrap para fechar o alerta suavemente
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alerta);
            bsAlert.close();
        }, 5000);
    });

    // ── 3. Efeito de "Glow" nos cards ao passar o mouse ────────────────
    // Seleciona todos os cards do sistema
    const cards = document.querySelectorAll('.card-premium');
    cards.forEach(function (card) {
        card.addEventListener('mouseenter', function () {
            // Adiciona um efeito de brilho ao passar o mouse
            this.style.boxShadow = '0 0 30px rgba(255, 0, 85, 0.4)';
        });
        
        card.addEventListener('mouseleave', function () {
            // Remove o efeito ao sair do mouse
            this.style.boxShadow = '0 8px 32px rgba(0, 0, 0, 0.3)';
        });
    });

    // ── 4. Validação de Formulários ────────────────────────────────────
    // Seleciona todos os formulários da página
    const formularios = document.querySelectorAll('form');
    formularios.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            // Pega todos os campos obrigatórios (required)
            const camposObrigatorios = form.querySelectorAll('[required]');
            let todosPreenchidos = true;
            
            // Verifica se todos os campos estão preenchidos
            camposObrigatorios.forEach(function (campo) {
                if (campo.value.trim() === '') {
                    todosPreenchidos = false;
                    campo.classList.add('is-invalid'); // Adiciona classe de erro
                } else {
                    campo.classList.remove('is-invalid'); // Remove classe de erro
                }
            });
            
            // Se algum campo estiver vazio, impede o envio do formulário
            if (!todosPreenchidos) {
                e.preventDefault();
                alert('⚠️ Por favor, preencha todos os campos obrigatórios!');
            }
        });
    });

    // ── 5. Animação de Scroll Suave ────────────────────────────────────
    // Adiciona scroll suave para links internos (âncoras)
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // ── 6. Tooltip do Bootstrap ────────────────────────────────────────
    // Ativa os tooltips do Bootstrap em toda a página
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // ── 7. Contador de Caracteres em Textarea ──────────────────────────
    // Seleciona todos os textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(function (textarea) {
        // Cria um elemento para mostrar o contador
        const contador = document.createElement('small');
        contador.className = 'text-muted d-block mt-1';
        textarea.parentElement.appendChild(contador);
        
        // Atualiza o contador a cada digitação
        textarea.addEventListener('input', function () {
            const caracteres = this.value.length;
            const maximo = this.getAttribute('maxlength') || 'ilimitado';
            contador.textContent = `${caracteres}${maximo !== 'ilimitado' ? '/' + maximo : ''} caracteres`;
        });
    });

});
