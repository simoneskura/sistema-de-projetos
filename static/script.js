document.addEventListener('DOMContentLoaded', function() {

    // Máscara para o CPF
    const cpfInput = document.querySelector('input[name="cpf"]');
    if (cpfInput) {
        cpfInput.addEventListener('input', function(e) {
            let v = e.target.value.replace(/\D/g, ""); 
            
            if (v.length > 11) v = v.slice(0, 11);

            v = v.replace(/(\d{3})(\d)/, "$1.$2");
            v = v.replace(/(\d{3})(\d)/, "$1.$2");
            v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
            
            e.target.value = v;
        });
    }

    // Máscara para o telefone
    const telInput = document.querySelector('input[name="telefone"]');
    if (telInput) {
        telInput.addEventListener('input', function(e) {
            let v = e.target.value.replace(/\D/g, ""); 
            
            if (v.length > 11) v = v.slice(0, 11);

            v = v.replace(/^(\d{2})(\d)/g, "($1) $2");
            v = v.replace(/(\d{5})(\d)/, "$1-$2");
            
            e.target.value = v;
        });
    }

    // Foco automático em alertas
    const alerta = document.querySelector('[role="alert"]');
    if (alerta) {
        alerta.setAttribute('tabindex', '-1'); 
        alerta.focus();

        document.addEventListener('keydown', function(e) {
            if (e.key === "Escape") {
                alerta.style.display = 'none';
            }
        });
    }

    // Aviso de dados que não foram salvos
    let formularioAlterado = false;
    const formCadastro = document.querySelector('form');
    if (formCadastro) {
        formCadastro.addEventListener('input', () => {
            formularioAlterado = true;
        });
        window.addEventListener('beforeunload', (e) => {
            if (formularioAlterado) {
                e.preventDefault();
                e.returnValue = ''; 
            }
        });
        formCadastro.addEventListener('submit', () => {
            formularioAlterado = false;
        });
    }
});