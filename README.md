Chamada da API?
-----------------

1. Baseado no projeto de consulta de filmes Online do Rodrigo, https://github.com/rodrigorf/filmes-cartaz-json, criei essa api para termos acesso à blilbia católica Ave Maria utilizando o recurso de web scrapping utilizando Python.

A chamada da api deve seressa : 

Genesia -> http://127.0.0.1:5000/api/biblia/genesis/1 
Exodo ->http://127.0.0.1:5000/api/biblia/exodo/1

O número no final é o capítulo

Estrutura inicial do retorno em JSON
-----------------

{
    "genesis": [
        {
            "verso": "1. No princípio, Deus criou os céus e a terra."
        },
        {
            "verso": "2. A terra estava informe e vazia; as trevas cobriam o abismo e o Espírito de Deus pairava sobre as águas."
        },
        {
            "verso": "4. Deus viu que a luz era boa, e separou a luz das trevas."
        },
        {
            "verso": "6. Deus disse: \"Faça-se um firmamento entre as águas, e separe ele umas das outras\"."
        },
        {
            "verso": "8. E assim se fez. Deus chamou ao firmamento CÉUS. Sobreveio a tarde e depois a manhã: foi o segundo dia."
        },
        {
            "verso": "10. Deus chamou ao elemento árido TERRA, e ao ajuntamento das águas MAR. E Deus viu que isso era bom."
        },
        {
            "verso": "12. A terra produziu plantas, ervas que contêm semente segundo a sua espécie, e árvores que produzem fruto segundo a sua espécie, contendo o fruto a sua semente. E Deus viu que isso era bom."
        },
        {
            "verso": "14. Deus disse: \"Façam-se luzeiros no firmamento dos céus para separar o dia da noite; sirvam eles de sinais e marquem o tempo, os dias e os anos,"
        },
        {
            "verso": "16. Deus fez os dois grandes luzeiros: o maior para presidir ao dia, e o menor para presidir à noite; e fez também as estrelas."
        },
        {
            "verso": "18. presidissem ao dia e à noite, e separassem a luz das trevas. E Deus viu que isso era bom."
        },
        {
            "verso": "20. Deus disse: \"Pululem as águas de uma multidão de seres vivos, e voem aves sobre a terra, debaixo do firmamento dos céus.\""
        },
        {
            "verso": "22. E Deus os abençoou: \"Frutificai, disse ele, e multiplicai-vos, e enchei as águas do mar, e que as aves se multipliquem sobre a terra.\""
        },
        {
            "verso": "24. Deus disse: \"Produza a terra seres vivos segundo a sua espécie: animais domésticos, répteis e animais selvagens, segundo a sua espécie.\" E assim se fez."
        },
        {
            "verso": "26. Então Deus disse: \"Façamos o homem à nossa imagem e semelhança. Que ele reine sobre os peixes do mar, sobre as aves dos céus, sobre os animais domésticos e sobre toda a terra, e sobre todos os répteis que se arrastem sobre a terra.\""
        },
        {
            "verso": "28. Deus os abençoou: \"Frutificai, disse ele, e multiplicai-vos, enchei a terra e submetei-a. Dominai sobre os peixes do mar, sobre as aves dos céus e sobre todos os animais que se arrastam sobre a terra.\""
        },
        {
            "verso": "30. E a todos os animais da terra, a todas as aves dos céus, a tudo o que se arrasta sobre a terra, e em que haja sopro de vida, eu dou toda erva verde por alimento.\" E assim se fez."
        },
        {
            "verso": "3. Deus disse: \"Faça-se a luz!\" E a luz foi feita."
        },
        {
            "verso": "5. Deus chamou à luz DIA, e às trevas NOITE. Sobreveio a tarde e depois a manhã: foi o primeiro dia."
        },
        {
            "verso": "7. Deus fez o firmamento e separou as águas que estavam debaixo do firmamento daquelas que estavam por cima."
        },
        {
            "verso": "9. Deus disse: \"Que as águas que estão debaixo dos céus se ajuntem num mesmo lugar, e apareça o elemento árido.\" E assim se fez."
        },
        {
            "verso": "11. Deus disse: \"Produza a terra plantas, ervas que contenham semente e árvores frutíferas que dêem fruto segundo a sua espécie e o fruto contenha a sua semente.\" E assim foi feito."
        },
        {
            "verso": "13. Sobreveio a tarde e depois a manhã: foi o terceiro dia."
        },
        {
            "verso": "15. e resplandeçam no firmamento dos céus para iluminar a terra\". E assim se fez."
        },
        {
            "verso": "17. Deus colocou-os no firmamento dos céus para que iluminassem a terra,"
        },
        {
            "verso": "19. Sobreveio a tarde e depois a manhã: foi o quarto dia."
        },
        {
            "verso": "21. Deus criou os monstros marinhos e toda a multidão de seres vivos que enchem as águas, segundo a sua espécie, e todas as aves segundo a sua espécie. E Deus viu que isso era bom."
        },
        {
            "verso": "23. Sobreveio a tarde e depois a manhã: foi o quinto dia."
        },
        {
            "verso": "25. Deus fez os animais selvagens segundo a sua espécie, os animais domésticos igualmente, e da mesma forma todos os animais, que se arrastam sobre a terra. E Deus viu que isso era bom."
        },
        {
            "verso": "27. Deus criou o homem à sua imagem; criou-o à imagem de Deus, criou o homem e a mulher."
        },
        {
            "verso": "29. Deus disse: \"Eis que eu vos dou toda a erva que dá semente sobre a terra, e todas as árvores frutíferas que contêm em si mesmas a sua semente, para que vos sirvam de alimento."
        },
        {
            "verso": "31. Deus contemplou toda a sua obra, e viu que tudo era muito bom. Sobreveio a tarde e depois a manhã: foi o sexto dia."
        }
    ]
}

____________________________________________________________________________

{
    "exodo": [
        {
            "verso": "1. Eis os nomes dos filhos de Israel que vieram para o Egito com Jacó, cada um com sua família:"
        },
        {
            "verso": "2. Rubem, Simeão, Levi, Judá,"
        },
        {
            "verso": "4. Dã, Neftali, Gad e Aser."
        },
        {
            "verso": "6. E, morto José, assim como todos os seus irmãos e toda aquela geração,"
        },
        {
            "verso": "8. Entretanto, subiu ao trono do Egito um novo rei, que não tinha conhecido José."
        },
        {
            "verso": "10. Vamos! É preciso tomar precaução contra eles e impedir que se multipliquem, para não acontecer que, sobrevindo uma guerra, se unam com os nossos inimigos e combatam contra nós, e se retirem do país."
        },
        {
            "verso": "12. Quanto mais os acabrunhavam, porém, tanto mais eles se multiplicavam e se espalhavam, a ponto de os egípcios os aborrecerem."
        },
        {
            "verso": "14. e amarguravam-lhes a vida com duros trabalhos na argamassa e na fabricação de tijolos, bem como com toda sorte de trabalhos nos campos e todas as tarefas que se lhes impunham tiranicamente."
        },
        {
            "verso": "16. e disse-lhes: Quando assistirdes às mulheres dos hebreus, e as virdes sobre o leito, se for um filho, matá-lo-eis; mas se for uma filha, deixá-la-eis viver."
        },
        {
            "verso": "18. O rei mandou-as chamar então e disse-lhes: Por que agistes assim, e deixastes viver os meninos?"
        },
        {
            "verso": "20. Deus beneficiou as parteiras: o povo continuou a multiplicar-se e a espalhar-se."
        },
        {
            "verso": "22. Então o faraó deu esta ordem a todo o seu povo: Todo menino que nascer, atirá-lo-eis ao Nilo. Deixareis, porém, viver todas as meninas."
        },
        {
            "verso": "3. Issacar, Zabulon, Benjamim,"
        },
        {
            "verso": "5. Todas as pessoas saídas de Jacó eram em número de setenta. José estava já no Egito."
        },
        {
            "verso": "7. os israelitas foram fecundos e multiplicaram-se; tornaram-se tão numerosos e tão fortes, que a terra ficou cheia deles."
        },
        {
            "verso": "9. Ele disse ao seu povo: Vede: os israelitas tornaram-se numerosos e fortes demais para nós."
        },
        {
            "verso": "11. Estabeleceu, pois, sobre eles, feitores para acabrunhá-los com trabalhos penosos: eles construíram para o faraó as cidades de Pitom e Ramsés, que deviam servir de entreposto."
        },
        {
            "verso": "13. Impunham-lhes a mais dura servidão,"
        },
        {
            "verso": "15. O rei do Egito dirigiu-se, igualmente, às parteiras dos hebreus uma se chamava Séfora e a outra, Fua),"
        },
        {
            "verso": "17. Mas as parteiras temiam a Deus, e não executaram as ordens do rei do Egito, deixando viver os meninos."
        },
        {
            "verso": "19. Porque, responderam elas ao faraó, as mulheres dos hebreus não são como as dos egípcios: elas são vigorosas, e já dão à luz antes que chegue a parteira."
        },
        {
            "verso": "21. Porque elas haviam temido a Deus, ele fez prosperar suas famílias."
        }
    ]
}


