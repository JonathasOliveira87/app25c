
document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtenha o valor digitado no campo de pesquisa
    var searchTerm = document.getElementById("search").value;

    // Faça algo com o termo de pesquisa (por exemplo, exiba no console)
    console.log("Termo de pesquisa:", searchTerm);

    // Execute a ação desejada, como enviar uma solicitação AJAX para buscar resultados

    // Limpe o campo de pesquisa
    document.getElementById("search").value = "";
});


<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
// Quando o link da foto de perfil for clicado
document.getElementById('profile-photo-link').addEventListener('click', async function(e) {
    e.preventDefault(); // Impede o comportamento padrão de abrir o link
    
    const { value: accept } = await Swal.fire({
        title: 'Termos e Condições',
        input: 'checkbox',
        inputValue: 1,
        inputPlaceholder: 'Eu concordo com os termos e condições',
        confirmButtonText: 'Continuar <i class="fa fa-arrow-right"></i>',
        inputValidator: (result) => {
            return !result && 'Você precisa concordar com os termos e condições';
        }
    });

    if (accept) {
        Swal.fire('Você concordou com os termos e condições :)');
        document.getElementById('photo-input').click(); // Simula o clique no input de arquivo
    }
});

// Quando uma foto for selecionada
document.getElementById('photo-input').addEventListener('change', function() {
    var reader = new FileReader();

    // Quando a foto for carregada
    reader.onload = function(e) {
        document.getElementById('profile-photo').src = e.target.result; // Define a nova foto de perfil
    };

    // Lê o arquivo da foto como uma URL de dados
    reader.readAsDataURL(this.files[0]);
});


