function atualizarValores() {
            // return new Promise((resolve, reject) => {
            fetch('/perdas_atualizar')
                .then(response => response.json())
                .then(data => {
                // Atualizar o valor do elemento com o novo valor obtido do servidor
                document.getElementById('perda_total').innerText = 'R$ ' + data.perdas[0] + ' --> ' ;
                document.getElementById('perda_totalp').innerText = 'R$ ' + data.perdas[2] + ' --> ';
                document.getElementById('perda_totalb').innerText = 'R$ ' + data.perdas[1] + ' --> ';
                obterDados(data.perdas);
                // resolve();
                })
                .catch(error => {
                console.error('Erro ao atualizar valor: ', error);
                // reject(error);
                });
            };
        // }
        setInterval(function() {
            // Chamar a função atualizarValores e esperar a Promise ser resolvida antes de chamar novamente o setInterval
            atualizarValores()
            .then(() => {
                // A função atualizarValores foi concluída, então pode chamar novamente o setInterval
                setTimeout(() => {
                setInterval(arguments.callee, 1000);
                }, 3000);
            })
            .catch(error => {
                // Tratar erro caso ocorra na função atualizarValores
                console.error('Erro ao atualizar valor: ', error);
            });
        }, 4000);

            var somav = 0
            var somap = 0
            var somab = 0

            function obterDados(perdas) {
            
            var numerov = 0
            var numerop = 0
            var numerob = 0
        

            fetch('/atualizar_dados') // Substitua a URL com a rota correta do servidor Flask
                .then(response => response.json())
                .then(data => {
                    // Atualizar o código HTML com base nos dados obtidos
                    var dados = data.dados;
                    dados=dados
                    document.getElementById('perda_totalletra').innerText = 'Letra : ' + dados[59];
                    if (dados[59] == 'V') {
                        numerov = parseFloat(perdas[7])
                        numerop = parseFloat(perdas[9])
                        numerob = parseFloat(perdas[8])
                        somav += numerov; 
                        somap -= numerop;
                        somab -= numerob;
                        console.log(somav + " V");
                        

                        
                        
                    }
                    if (dados[59] == 'P') {
                        numerov = parseFloat(perdas[7])
                        numerop = parseFloat(perdas[9])
                        numerob = parseFloat(perdas[8])                              
                        somav -= numerov; 
                        somap += numerop;
                        somab -= numerob;
                        console.log(somap + " P");
                    }
                    if (dados[59] == 'B') {
                        numerov = parseFloat(perdas[7])
                        numerop = parseFloat(perdas[9])
                        numerob = parseFloat(perdas[8])                   
                        somav -= numerov; 
                        somap -= numerop;
                        somab += numerob * 12;
                        console.log(somab + " B");
                        
                    }
                })
                .catch(error => {
                    console.error('Erro ao obter dados atualizados: ', error);
                });
                }
                setTimeout(() => {
                console.log('Dentro do setTimeout'); // Esta mensagem será exibida após 3 segundos
                obterDados(perdas); // Chamar a função obterDados() após o atraso de 3 segundos
                }, 1000);



setInterval(function() {
    // Fazer uma requisição ao servidor para obter o valor atualizado de pegar_total
    fetch('/atualizar_total')
        .then(response => response.json())
        .then(data => {
        // Atualizar o valor do elemento com o novo valor obtido do servidor
        document.getElementById('valor_total').innerText = data.pegar_total[0] + 'X';
        document.getElementById('valor_total2').innerText = data.pegar_total[1] + 'X';
        document.getElementById('valor_total3').innerText = data.pegar_total[2] + 'X';
        })
        .catch(error => {
        console.error('Erro ao atualizar valor: ', error);
        });
    }, 15000); // 5000 ms = 5 segundos