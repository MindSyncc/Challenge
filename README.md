# Simulador de Corrida - Versão 1.0.8

**Equipe MindSync:**
- **Fernando Carlos Colque Huaranca** - RM558095
- **Heloísa Fleury Jardim** - RM556378
- **Juan Fuentes Rufino** - RM557673
- **Julia Carolina Ferreira Silva** - RM558896
- **Pedro Batista** - RM558137

## Descrição do Projeto

Este projeto é um simulador de corrida inspirado em parâmetros aproximados da Fórmula E. Ele inclui funcionalidades como gerenciamento de usuários, simulação de corridas, cálculo de pontuações e um menu interativo. A versão atual (1.0.8) também traz melhorias nas funcionalidades de votação de pilotos e no sistema de login, além de otimizações no código para melhor desempenho.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- **menu.py:** Gerencia o menu principal do simulador, oferecendo opções como iniciar a corrida, visualizar estrtura da corrida e votar. Integra-se ao sistema de pontuação dos pilotos.
- **corrida.py:** Contém a lógica da simulação de corrida, calculando as velocidades dos pilotos e atualizando suas posições com base em fatores aleatórios.
- **pontos.py:** Gerencia o sistema de pontuação dos pilotos, distribuindo pontos conforme o desempenho de cada piloto nas corridas.
- **banco_de_dados.py:** Armazena dados dos usuários, como login, pontuação e outras informações, utilizando um arquivo de texto para persistência dos dados.
- **votacao.py:** Implementa o sistema de votação, permitindo que os usuários escolham e votem em seus pilotos preferidos antes da corrida.
- **login.py:** O arquivo login.py é responsável pela autenticação dos usuários. Ele gerencia a entrada no sistema, verificando se os dados de login fornecidos pelo usuário correspondem aos registrados no sistema. Essa verificação garante que apenas usuários cadastrados possam acessar as funcionalidades do simulador. Além disso, o login.py também cuida do processo de logout, permitindo que os usuários finalizem suas sessões.

## Funcionalidades

- **Simulação de corrida:** A corrida é simulada com base em dados gerados aleatoriamente, considerando diferentes trechos da pista que afetam a velocidade dos pilotos.
- **Sistema de votação:** Os usuários podem votar em seus pilotos favoritos antes da corrida, com o resultado armazenado e validado corretamente.
- **Gerenciamento de usuários:** O sistema permite que os usuários façam login, armazenando seus pontos e outras informações relevantes.
- **Cálculo de pontuação:** Os pilotos recebem pontos com base em suas posições finais na corrida.
- **Menu interativo:** O menu oferece opções para iniciar corridas, votar e visualizar informações sobre pilotos e pontuações.

## Versão Atual: 1.0.8

A versão 1.0.8 traz uma série de melhorias no código, incluindo:

- Adição de login e usuário e um pequeno banco de dados, onde será armazenado os pontos de cada participante.
- Melhorias no sistema de votação de pilotos, com validação mais robusta e integração com o banco de dados de usuários.
- Otimização da simulação de corrida para melhor desempenho e eficiência no uso dos dados.
- Reorganização de funções para garantir que os dados da corrida sejam processados de forma mais eficiente, especialmente na criação da tupla com informações da pista.
- Além de um menu interativo convidativo.

## Futuras Melhorias

- **Simulação mais realista:** Integração de dados reais da Fórmula E para tornar a simulação mais precisa e imersiva.
- **Condições dinâmicas de corrida:** Implementação de variáveis como mudanças climáticas e "attack mode", que influenciam diretamente o desempenho dos pilotos.
- **Melhorias no sistema de votação:** Ampliar as opções de interação dos usuários com o sistema de votação, trazendo mais variáveis de escolha.
- **Adição de mais pilotos e equipes:** Serão adicionados mais pilotos e equipes para que possam ser escolhidas para que seja mais abrangente as escolhas do usuário.

## Como Executar o Projeto

1. Clone este repositório.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o arquivo `menu.py` para iniciar o simulador de corrida.
4. Navegue pelas opções do menu para iniciar corridas, votar em pilotos e visualizar a pontuação.

## Conclusão

O **Simulador de Corrida** versão 1.0.8 oferece uma base sólida para a simulação de corridas, com sistemas de pontuação e votação funcionais e interativos. O projeto está em evolução, com futuras versões planejadas para trazer mais realismo e funcionalidades adicionais.
