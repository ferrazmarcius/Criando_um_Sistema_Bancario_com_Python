# Sistema Bancário Simples em Python

Este projeto é um sistema bancário simples desenvolvido em Python, concebido como um desafio de programação para consolidar conceitos fundamentais e aplicar boas práticas de desenvolvimento de software.

## Funcionalidades Principais

O sistema oferece as seguintes operações:

* **Depósito:** Permite adicionar fundos à conta.
* **Saque:** Realiza saques com validações de saldo, limite por operação e número máximo de saques diários.
* **Extrato:** Exibe o histórico de todas as transações (depósitos e saques) e o saldo atual.
* **Criação de Usuário:** Permite o cadastro de novos usuários com informações como CPF, nome, data de nascimento e endereço.
* **Criação de Conta:** Associa novas contas bancárias a usuários existentes através do CPF.
* **Listagem de Contas:** Exibe todas as contas cadastradas no sistema.

## Melhorias e Otimizações Implementadas

Este projeto passou por diversas fases de otimização para aprimorar sua estrutura e lógica:

* **Simulação de Cédulas (Saque Aprimorado):** Uma validação crucial foi implementada para permitir saques apenas com valores positivos e que sejam **múltiplos de R$ 5,00**. Isso simula de forma mais realista a disponibilidade de cédulas de dinheiro, garantindo que o usuário só possa sacar valores que podem ser entregues em notas (5, 10, 20, 50, etc.).
* **Modularização com Funções:** O código foi refatorado para separar cada operação bancária e de gerenciamento em **funções dedicadas** (ex: `depositar()`, `sacar()`, `criar_usuario()`, `criar_conta()`). Essa abordagem melhora significativamente:
    * **Organização:** O código fica mais limpo e fácil de navegar.
    * **Legibilidade:** Cada função tem uma responsabilidade clara.
    * **Reutilização:** Partes do código podem ser facilmente reutilizadas.
    * **Manutenção:** Correções e novas funcionalidades são mais simples de implementar sem afetar outras áreas.
* **Gerenciamento de Entidades:** A separação de usuários e contas em estruturas de dados distintas (listas de dicionários) permite um controle mais granular e flexível do sistema.
* **Tratamento de Erros:** Mensagens claras foram adicionadas para guiar o usuário em caso de operações inválidas ou falhas.

##  Tecnologias Utilizadas

* **Python 3.x**

## Desenvolvedor

* **Marcius Silva Ferraz Filho**
* **Meu LinkedIn:** [linkedin.com/in/marcius-ferraz](https://www.linkedin.com/in/marcius-ferraz)
* **Meu perfil na DIO:** [dio.me/users/mferraz_xml](https://www.dio.me/users/mferraz_xml)

---

**Nota:** Este projeto foi desenvolvido como parte de um desafio de Python3 no bootcamp da DIO em parceria com a Santander Open Academy. E serve como demonstração de habilidades em Python.
