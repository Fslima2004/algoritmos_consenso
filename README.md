Descrição do Projeto

Este projeto implementa uma simulação do algoritmo Proof of Stake (PoS) em um ambiente distribuído. O PoS é amplamente utilizado em sistemas de blockchain como alternativa ao Proof of Work (PoW), oferecendo maior eficiência energética e incentivo para participação honesta dos validadores. 
Na simulação, um conjunto de nós representa os participantes da rede. Cada nó possui uma quantidade de "stake" (participação), que influencia suas chances de ser escolhido como validador de blocos. O sistema implementa falhas simuladas e mecanismos de recuperação para demonstrar a resiliência do algoritmo.



Configuração do Ambiente e Execução do Código

Para executar o projeto, é necessário ter instalado o Python 3.8 ou superior
Passos para execução:
1. Clonar repositório
2. Executar o seguinte comando: python main.py



Fases do Algoritmo na Implementação

1. Seleção de Validador
Cada nó tem uma probabilidade proporcional ao seu "stake" de ser escolhido como o próximo validador.
O módulo validator_selection.py utiliza um algoritmo baseado em pesos para essa escolha.
2. Proposição de Blocos
O nó escolhido propõe um novo bloco contendo transações.
A proposta é enviada para os outros nós ativos da rede.
3. Validação de Blocos
Os nós verificam se o bloco proposto é válido:
Transações devem estar presentes.
O hash anterior deve corresponder ao último bloco aceito.
Apenas blocos válidos são adicionados à blockchain.
4. Atualização da Blockchain
Após a validação bem-sucedida, o bloco é adicionado à cadeia e compartilhado com os outros nós.



Simulação de Falhas

Falhas Implementadas

Nó Inativo
Um nó pode "falhar" e tornar-se inativo, simulando problemas como perda de conexão ou falha de hardware.
Nós inativos não podem propor nem validar blocos.

Falha na Validação
Blocos inválidos são rejeitados pelos nós, simulando uma proteção contra comportamentos maliciosos.

Conflitos na Rede
Quando um bloco não atinge consenso, ele é descartado, e uma nova rodada de validação é iniciada.

Mecanismos de Recuperação

Reativação de Nós:
Nós inativos podem ser recuperados manualmente pela rede (simulado no código).

Sincronização da Blockchain:
Nós que retornam após uma falha sincronizam-se com a cadeia mais longa na rede.
