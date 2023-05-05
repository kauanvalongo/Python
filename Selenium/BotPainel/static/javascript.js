
function atualizarValores() {
    fetch('/perdas_atualizar')
        .then(response => response.json())
        .then(data => {
        document.getElementById('perda_total').innerHTML = 'R$' + data.perdas[0] + '&#10132;' ;
        document.getElementById('perda_totalp').innerHTML = 'R$' + data.perdas[1] + '&#10132;';
        document.getElementById('perda_totalb').innerHTML = 'R$' + data.perdas[2] + '&#10132;';
        obterDados(data.perdas);       
        })
        .then(() => {
            setTimeout(() => {
                atualizarValores();
            }, 100);
        })
    .catch(error => {
    console.error('Erro ao atualizar valor: ', error);
    })
};
atualizarValores()
var somav = 0
var somap = 0
var somab = 0
function obterDados(perdas) {
    var numerov = parseFloat(perdas[6])
    var numerop = parseFloat(perdas[7])
    var numerob = parseFloat(perdas[8])
    var spanElementv = document.getElementById("valor_realv");
    var spanElementp = document.getElementById("valor_realp");
    var spanElementb = document.getElementById("valor_realb");
    setTimeout(() => { // Adicionar setTimeout aqui
        fetch('/atualizar_dados') // Substitua a URL com a rota correta do servidor Flask
            .then(response => response.json())
            .then(data => {
                // Atualizar o código HTML com base nos dados obtidos
                var dados = data.dados;
                dados = dados
                if (dados[59] == 'V') {           
                    somav += numerov ;
                    somap -= numerop ;
                    somab -= numerob ;
                    document.getElementById('valor_realv').innerText = 'R$' + somav.toFixed(2) ;
                    document.getElementById('valor_realp').innerText = 'R$' + somap.toFixed(2) ;
                    document.getElementById('valor_realb').innerText = 'R$' + somab.toFixed(2) ;
                    
                }
                if (dados[59] == 'P') {
                    somav -= numerov ;
                    somap += numerop ;
                    somab -= numerob ;
             
                    document.getElementById('valor_realv').innerText = 'R$' + somav.toFixed(2) ;
                    document.getElementById('valor_realp').innerText = 'R$' + somap.toFixed(2) ;
                    document.getElementById('valor_realb').innerText = 'R$' + somab.toFixed(2) ;
                }
                if (dados[59] == 'B') {
                    somav -= numerov ;
                    somap -= numerop  ;
                    somab += numerob * 12 ;

                    document.getElementById('valor_realv').innerText = 'R$' + somav.toFixed(2) ;
                    document.getElementById('valor_realp').innerText = 'R$' + somap.toFixed(2) ;
                    document.getElementById('valor_realb').innerText = 'R$' + somab.toFixed(2) ;
                }


                if (somav > 0) {
                    spanElementv.classList.remove("negativo");
                    spanElementv.classList.add("positivo");
                } else {
                    spanElementv.classList.remove("positivo");
                    spanElementv.classList.add("negativo");
                }   
            
                if (somap > 0) { 
                    spanElementp.classList.remove("negativo");
                    spanElementp.classList.add("positivo");
                } else {
                    spanElementp.classList.remove("positivo");
                    spanElementp.classList.add("negativo");
                }    
            
                if (somab > 0) {
                    spanElementb.classList.remove("negativo");
                    spanElementb.classList.add("positivo");
                } else {
                    spanElementb.classList.remove("positivo");
                    spanElementb.classList.add("negativo");
                }    
            })
            .catch(error => {
                console.error('Erro ao obter dados atualizados: ', error);
            });
    }, 10800); // Definir o atraso de 5 segundos aqui
}


var total1
var total2
var total3
setInterval(function() {
    // Fazer uma requisição ao servidor para obter o valor atualizado de pegar_total
    fetch('/atualizar_total')
        .then(response => response.json())
        .then(data => {
        total1 = parseInt(data.pegar_total[0]);
        total2 = parseInt(data.pegar_total[1]);
        total3 = parseInt(data.pegar_total[2]);
        var img1 = document.getElementById('valor_totali')
        var img2 = document.getElementById('valor_total2i')
        var img3 = document.getElementById('valor_total3i')
        // Atualizar o valor do elemento com o novo valor obtido do servidor
        document.getElementById('valor_total').innerText = data.pegar_total[0] + 'x';
        document.getElementById('valor_total2').innerText = data.pegar_total[1] + 'x';
        document.getElementById('valor_total3').innerText = data.pegar_total[2] + 'x';
        if (total1 > total2){
            img1.classList.remove('valor_totali2')
            img2.classList.remove('valor_total2i2')
            img1.classList.add('valor_totali')
            img2.classList.add('valor_total2i')

        }
        if (total1 < total2){
            
            img1.classList.remove('valor_totali')
            img2.classList.remove('valor_total2i')
            img1.classList.add('valor_totali2')
            img2.classList.add('valor_total2i2')
        }
        })
        .catch(error => {
        console.error('Erro ao atualizar valor: ', error);
        });
    }, 15000); // 5000 ms = 5 segundos

function criarImagem(cor) {
    var imagem = document.createElement('img');
    imagem.src = 'static/imagens/' + cor + '.png';
    imagem.alt = cor;
    return imagem;
}

function atualizarHTML(dados) {
    var imagensContainer = document.getElementById('imagens-container');
    if (imagensContainer) {
        imagensContainer.innerHTML = '';
        for (var i = 0; i < dados.length; i++) {
            var cor = dados[i];
            var imagem = criarImagem(cor);
            imagensContainer.appendChild(imagem);
        }
    }
}

function obterDadosAtualizados() {
    var percentp = document.getElementById('porcentagemp')
    var percentv = document.getElementById('porcentagemv')
    var percentb = document.getElementById('porcentagemb')
    var indicada = document.getElementById('imgindicada')
    var pindicada = document.getElementById('pindicada')
    fetch('/atualizar_dados') 
        .then(response => response.json())
        .then(data => {
            var dados = data.dados;
            atualizarHTML(dados);
           
            if (somav > 10000.00 && total1 > 31 && dados[58] === "P" && dados[59] === "V") {
      
                percentp.innerHTML = "43,8%";
                percentv.innerHTML = "52,0%";
                percentb.innerHTML = "4,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '52,0%'
            }

            else if (somap > 10000.00 && total2 > 31 && dados[58] === "V" && dados[59] === "P") {
      
                percentv.innerHTML = "41,8%";
                percentp.innerHTML = "54,0%";
                percentb.innerHTML = "4,2%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '54,0%'
            }

            else if (total1 >= 30 && dados[57] === "P" && dados[58] === "V" && dados[59] === "V") {
      
                percentp.innerHTML = "41,6%";
                percentv.innerHTML = "53,2%";
                percentb.innerHTML = "4,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '53,2%'
            }
            else if (total2 >= 30 && dados[57] === "V" && dados[58] === "P" && dados[59] === "P") {
      
                percentv.innerHTML = "41,6%";
                percentp.innerHTML = "53,2%";
                percentb.innerHTML = "4,2%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '53,2%'
            }

            else if (total1 >= 35 && dados[58] === "P" && dados[59] === "V") {
      
                percentp.innerHTML = "46,6%";
                percentv.innerHTML = "48,2%";
                percentb.innerHTML = "4,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '53,2%'
            }
            else if (total2 >= 35 && dados[58] === "V" && dados[59] === "P") {
      
                percentv.innerHTML = "43,6%";
                percentp.innerHTML = "51,2%";
                percentb.innerHTML = "4,2%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '53,2%'
            }

            else if (dados[56] === "P" && dados[57] === "P" && dados[58] === "V" && dados[59] === "V") {
                percentp.innerHTML = "35,8%";
                percentv.innerHTML = "45,5%";
                percentb.innerHTML = "19,1%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '45,5%'
            }
            else if (dados[56] === "V" && dados[57] === "V" && dados[58] === "P" && dados[59] === "P") {
         
                percentv.innerHTML = "33,8%";
                percentp.innerHTML = "48,5%";
                percentb.innerHTML = "19,1%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '48,5%'
            }

            else if (dados[55] === "P" && dados[56] === "P" && dados[57] === "V" && dados[58] === "V" && dados[59] === "P") {
      
                percentp.innerHTML = "31,8%";
                percentv.innerHTML = "55,5%";
                percentb.innerHTML = "14,1%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '55,5%'
            }

            else if (dados[55] === "V" && dados[56] === "V" && dados[57] === "P" && dados[58] === "P" && dados[59] === "V") {
          
                percentv.innerHTML = "31,8%";
                percentp.innerHTML = "55,5%";
                percentb.innerHTML = "14,1%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '55,5%'
            }




            //============================


            else if (somap < somav && total2 < total1 && dados[53] === "P" && dados[54] === "V" && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
      
                percentv.innerHTML = "15,8%";
                percentp.innerHTML = "65,0%";
                percentb.innerHTML = "19,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '65,0%'
            }
            
            
            else if (somap < somav && total2 < total1 && dados[53] === "V" && dados[54] === "P" && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
         
                percentp.innerHTML = "18,7%";
                percentv.innerHTML = "63,6%";
                percentb.innerHTML = "17,7%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '63,6%'
            }

            else if (somap > somav && total2 < total1 && dados[53] === "P" && dados[54] === "V" && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
       
                percentv.innerHTML = "27,4%";
                percentp.innerHTML = "40,3%";
                percentb.innerHTML = "21,7%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '40,3%'
            }
            
            else if (somap < somav && total2 > total1 && dados[53] === "V" && dados[54] === "P" && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P"){
    
                percentp.innerHTML = "25,7%";
                percentv.innerHTML = "58,7%";
                percentb.innerHTML = "15,6%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '58,7%'
            }

            else if (somap > somav && total2 < total1 && dados[53] === "V" && dados[54] === "P" && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
      
                percentp.innerHTML = "27,4%";
                percentv.innerHTML = "40,3%";
                percentb.innerHTML = "21,7%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '40,3%'
            }
            
            else if (somap < somav && total2 > total1 && dados[53] === "P" && dados[54] === "V" && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V"){
      
                percentv.innerHTML = "25,7%";
                percentp.innerHTML = "58,7%";
                percentb.innerHTML = "15,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '58,7%'
            }


            else if (somap > somav && total2 > total1 && dados[53] === "P" && dados[54] === "V" && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {

                percentv.innerHTML = "30,8%";
                percentp.innerHTML = "59,0%";
                percentb.innerHTML = "10,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '59,0%'
            }
            
            
            else if (somap > somav && total2 > total1 && dados[53] === "V" && dados[54] === "P" && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
        
                percentp.innerHTML = "31,7%";
                percentv.innerHTML = "60,6%";
                percentb.innerHTML = "7,7%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '60,6%'
            }

        

//=================================================================

            else if (somap < somav && total2 < total1 && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
        
                percentv.innerHTML = "21,4%";
                percentp.innerHTML = "70,8%";
                percentb.innerHTML = "7,8%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '70,8%'
            }
            
            else if (somap < somav && total2 < total1 && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
 
                percentp.innerHTML = "20,4%";
                percentv.innerHTML = "69,8%";
                percentb.innerHTML = "9,8%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '69,8%'
            }
            


            else if (somap > somav && total2 < total1 && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
 
                percentv.innerHTML = "27,4%";
                percentp.innerHTML = "40,3%";
                percentb.innerHTML = "21,7%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '40,3%'
            }
            
            else if (somap < somav && total2 > total1 && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V"){
        
                percentv.innerHTML = "25,7%";
                percentp.innerHTML = "58,7%";
                percentb.innerHTML = "15,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '58,7%'
            }

            else if (somap > somav && total2 < total1 && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {

                percentp.innerHTML = "27,4%";
                percentv.innerHTML = "40,3%";
                percentb.innerHTML = "21,7%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '40,3%'
            }
            
            else if (somap < somav && total2 > total1 && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P"){
   
                percentp.innerHTML = "25,7%";
                percentv.innerHTML = "58,7%";
                percentb.innerHTML = "15,6%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '58,7%'
            }


            else if (somap > somav && total2 > total1 && dados[55] === "V" && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
   
                percentv.innerHTML = "35,4%";
                percentp.innerHTML = "55,9%";
                percentb.innerHTML = "8,7%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '55,9%'
            }
            
            else if (somap > somav && total2 > total1 && dados[55] === "P" && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
        
                percentp.innerHTML = "40,3%";
                percentv.innerHTML = "50,9%";
                percentb.innerHTML = "8,8%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '50,9%'
            }


            //=========================================================================



            
            else if (somap < somav && total2 < total1 && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
          
                percentv.innerHTML = "32,9%";
                percentp.innerHTML = "58,6%";
                percentb.innerHTML = "8,5%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '58,6%'
            }

            else if (somap < somav && total2 < total1 && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
        
                percentp.innerHTML = "31,5%";
                percentv.innerHTML = "52,4%";
                percentb.innerHTML = "16,1%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '52,4%'
            }
            else if (somap > somav && total2 < total1 && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
       
                percentv.innerHTML = "24,7%";
                percentp.innerHTML = "60,7%";
                percentb.innerHTML = "14,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '60,7%'
            }
            
            else if (somap < somav && total2 > total1 && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
         
                percentp.innerHTML = "35,4%";
                percentv.innerHTML = "56,4%";
                percentb.innerHTML = "8,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '56,4%'
            }
            else if (somap > somav && total2 < total1 && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
       
                percentp.innerHTML = "39,5%";
                percentv.innerHTML = "55,0%";
                percentb.innerHTML = "5,5%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '55,0%'
            }

            else if (somap < somav && total2 > total1 && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V" ) {
        
                percentv.innerHTML = "40,4%";
                percentp.innerHTML = "48,5%";
                percentb.innerHTML = "11,1%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '48,5%'
                
            }

            else if (somap > somav && total2 > total1 && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
        
                percentv.innerHTML = "34,7%";
                percentp.innerHTML = "50,7%";
                percentb.innerHTML = "14,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '50,7%'
            }
            
            else if (somap > somav && total2 > total1 && dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
       
                percentp.innerHTML = "38,4%";
                percentv.innerHTML = "53,2%";
                percentb.innerHTML = "8,4%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '53,2%'
            }

            else if (dados[56] === "P" && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
       
                percentp.innerHTML = "39,4%";
                percentv.innerHTML = "54,2%";
                percentb.innerHTML = "8,4%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '54,2%'
            }

            else if (dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
       
                percentv.innerHTML = "42,3%";
                percentp.innerHTML = "55,3%";
                percentb.innerHTML = "4,4%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '55,3%'
            }


            //======================================================================================
            
            
            else if (somap < somav && total2 < total1&& dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
     
                percentv.innerHTML = "41,5%";
                percentp.innerHTML = "46,9%";
                percentb.innerHTML = "11,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '46,9%'
            }

            else if (somap < somav && total2 < total1 && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
       
                percentp.innerHTML = "42,4%";
                percentv.innerHTML = "52,4%";
                percentb.innerHTML = "5,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '52,4%'

            }
            else if (somap > somav && total2 < total1 && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
        
                percentv.innerHTML = "39,6%";
                percentp.innerHTML = "45,8%";
                percentb.innerHTML = "14,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '45,8%'
            }
            
            else if (somap < somav && total2 > total1 && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
   
                percentp.innerHTML = "41,5%";
                percentv.innerHTML = "50,3%";
                percentb.innerHTML = "8,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '50,3%'
                
            }

            else if (somap > somav && total2 < total1 && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
      
                percentp.innerHTML = "41,0%";
                percentv.innerHTML = "53,0%";
                percentb.innerHTML = "6,0%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '53,0%'
            }

            else if (somap < somav && total2 > total1 && dados[57] === "V" && dados[58] === "V" && dados[59] === "V" ) {
         
                percentv.innerHTML = "41,4%";
                percentp.innerHTML = "45,9%";
                percentb.innerHTML = "4,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '45,9%'
            }

            else if (somap > somav && total2 > total1 && dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
 
                percentv.innerHTML = "44,8%";
                percentp.innerHTML = "50,6%";
                percentb.innerHTML = "4,6%";
                indicada.src = 'static/imagens/p.png'
                pindicada.innerText = '50,6%'
            }
            
            else if (somap > somav && total2 > total1 && dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
       
                percentp.innerHTML = "43,3%";
                percentv.innerHTML = "50,5%";
                percentb.innerHTML = "6,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '50,5%'
            }

            else if (dados[57] === "P" && dados[58] === "P" && dados[59] === "P") {
       
                percentp.innerHTML = "41,5%";
                percentv.innerHTML = "52,3%";
                percentb.innerHTML = "6,2%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '52,3%'
            }

            else if (dados[57] === "V" && dados[58] === "V" && dados[59] === "V") {
       
                percentv.innerHTML = "42,0%";
                percentp.innerHTML = "51,3%";
                percentb.innerHTML = "6,7%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '51,3%'
            }


            //=====================================================================

            else if (somap < somav && total2 < total1 && dados[58] === "V" && dados[59] === "V") {

                percentv.innerHTML = "44,5%";
                percentp.innerHTML = "48,6%";
                percentb.innerHTML = "6,9%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '48,6%'
            }

            else if (somap > somav && total2 > total1 && dados[58] === "P" && dados[59] === "P") {

                percentp.innerHTML = "42,5%";
                percentv.innerHTML = "52,7%";
                percentb.innerHTML = "4,8%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '52,7%'
            }

            else if (somap > somav && total2 < total1 && dados[58] === "V" && dados[59] === "V") {
 
                percentv.innerHTML = "46,0%";
                percentp.innerHTML = "51,0%";
                percentb.innerHTML = "3,0%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '51,0%'
            }

            else if (somap < somav && total2 > total1 && dados[58] === "P" && dados[59] === "P" ) {
      
                percentp.innerHTML = "40,9%";
                percentv.innerHTML = "46,4%";
                percentb.innerHTML = "4,6%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '46,4%'
            }

            else if (somap > somav && total2 < total1 && dados[58] === "P" && dados[59] === "P") {
    
                percentp.innerHTML = "45,5%";
                percentv.innerHTML = "51,5%";
                percentb.innerHTML = "3,0%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '51,5%'
            }

            else if (somap < somav && total2 > total1 && dados[58] === "V" && dados[59] === "V" ) {
        
                percentv.innerHTML = "40,9%";
                percentp.innerHTML = "46,4%";
                percentb.innerHTML = "4,6%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '46,4%'
            }
            

            else if (somap > somav && total2 > total1 && dados[58] === "V" && dados[59] === "V") {
                percentv.innerHTML = "41,2%";
                percentp.innerHTML = "49,6%";
                percentb.innerHTML = "9,2%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '49,6%'
            }
            
            else if (somap < somav && total2 < total1 && dados[58] === "P" && dados[59] === "P") {
          
                percentp.innerHTML = "44,5%";
                percentv.innerHTML = "51,0%";
                percentb.innerHTML = "4,5%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '51,0%'
            }

            else if (dados[58] === "P" && dados[59] === "P") {
          
                percentp.innerHTML = "45,5%";
                percentv.innerHTML = "49,0%";
                percentb.innerHTML = "5,5%";
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '49,0%'
            }

            else if (dados[58] === "V" && dados[59] === "V") {
          
                percentv.innerHTML = "45,0%";
                percentp.innerHTML = "48,5%";
                percentb.innerHTML = "5,5%";
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '48,5%'
            }

            // ========================================================================================
            else if (somap < somav && total2 < total1 && dados[58] === "B" && dados[59] === "V") {
                percentv.innerHTML = "43,3%"
                percentp.innerHTML = "44,7%"
                percentb.innerHTML = "13,0%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '44,7%'
            }

            else if (somap < somav && total2 < total1 && dados[58] === "B" && dados[59] === "P") {
                percentp.innerHTML = "43,6%"
                percentv.innerHTML = "48,7%"
                percentb.innerHTML = "8,7%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '48,7%'
            }

            else if (somap < somav && total2 < total1 && dados[56] === "V" && dados[57] === "V" && dados[58] === "V" && dados[59] === "P") {
                percentp.innerHTML = "41,6%"
                percentv.innerHTML = "50,4%"
                percentb.innerHTML = "8,0%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '50,4%'
            }

            else if (somap > somav && total2 > total1 && dados[59] === "P") {
                percentp.innerHTML = "40,6%"
                percentv.innerHTML = "50,7%"
                percentb.innerHTML = "8,7%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '50,7%'
            }
            else if (somap < somav && total2 < total1 && dados[59] === "V") {
                percentv.innerHTML = "48,4%"
                percentp.innerHTML = "50,1%"
                percentb.innerHTML = "2,5%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '50,1%'
            }

            else if (somap < somav && total2 > total1 && dados[59] === "P") {
                percentp.innerHTML = "47,6%"
                percentv.innerHTML = "50,1%"
                percentb.innerHTML = "2,3%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '50,1%'
            }
            else if (somap > somav && total2 < total1 && dados[59] === "V") {
                percentv.innerHTML = "45,4%"
                percentp.innerHTML = "49,5%"
                percentb.innerHTML = "5,1%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '49,5%'
            }
            else if (somap < somav && total2 > total1 && dados[59] === "V") {
                percentv.innerHTML = "47,6%"
                percentp.innerHTML = "50,1%"
                percentb.innerHTML = "2,3%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '50,1%'
            }
            else if (somap > somav && total2 < total1 && dados[59] === "P") {
                percentp.innerHTML = "45,4%"
                percentv.innerHTML = "49,5%"
                percentb.innerHTML = "5,1%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '49,5%'
            }

            else if (somap < somav && total2 < total1 && dados[59] === "P") {
                percentp.innerHTML = "44,5%"
                percentv.innerHTML = "46,8%"
                percentb.innerHTML = "8,7%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '46,8%'
            }
            else if (somap > somav && total2 > total1 && dados[59] === "V") {
                percentv.innerHTML = "48,1%"
                percentp.innerHTML = "48,7%"
                percentb.innerHTML = "4,2%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '48,7%'
            }
            else if (somap > somav && total2 > total1 && dados[59] === "B") {
                percentp.innerHTML = "45,1%"
                percentv.innerHTML = "51,7%"
                percentb.innerHTML = "4,2%"
                indicada.src = 'static/imagens/V.png'
                pindicada.innerText = '51,7%'
            }

            else if (somap < somav && total2 < total1 && dados[59] === "B") {
                percentv.innerHTML = "45,1%"
                percentp.innerHTML = "51,7%"
                percentb.innerHTML = "4,2%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '51,7%'
            }

            else if (dados[59] === "B") {
                percentv.innerHTML = "48,4%"
                percentp.innerHTML = "48,4%"
                percentb.innerHTML = "4,2%"
                indicada.src = 'static/imagens/P.png'
                pindicada.innerText = '48,4%'
            }
    
            else {
                percentv.innerHTML = ""
                percentp.innerHTML = "Analisando Padrões..."
                percentb.innerHTML = ""
                pindicada.innerText = ''
                console.log('analisandi padr~pes ')
            }
            if (indicada.src !== 'static/imagens/money.jpg') {
                indicada.style.display = "block";
            }
            else {
                indicada.style.display = "none";
            }
        })
        

        .catch(error => {
            console.error('Erro ao obter dados atualizados: ', error);
        });
}
window.onload = function() {
    obterDadosAtualizados();
    setInterval(obterDadosAtualizados, 3000); 
}