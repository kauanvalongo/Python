<script>

function updateRandomNumber() {
    var randomNumberElement = document.getElementById('randomNumber');
    randomNumberElement.innerHTML = 'Número aleatório: ' + Math.floor(Math.random() * 100) + 1;
}

// Atualizar o número aleatório a cada 5 segundos
setInterval(updateRandomNumber, 5000); // 5000 milissegundos = 5 segundos
</script>


