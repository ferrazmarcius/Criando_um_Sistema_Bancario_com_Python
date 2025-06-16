# Criando_um_Sistema_Bancario_com_Python
Projeto de sistema bancário em Python para estudos (Desafio DIO Santander Open Academy (Aula Criando um Sistema Bancário com Python))


Este projeto é um sistema bancário simples desenvolvido em Python, concebido como um desafio de programação para consolidar conceitos fundamentais.

Principais funcionalidades e melhorias implementadas:

Operações Essenciais: Suporta operações básicas de depósito, saque e consulta de extrato.
Controle de Saldo e Limite: Gerencia o saldo da conta, com limite diário por saque e um número máximo de saques permitidos por período.
Simulação de Cédulas (Saque Aprimorado): Implementei uma validação crucial que permite realizar saques apenas com valores positivos e que sejam múltiplos de R$ 5,00. Isso simula de forma mais realista a disponibilidade de cédulas de dinheiro, garantindo que o usuário só possa sacar valores que podem ser entregues em notas de 5, 10, 20, 50, etc.
Modularização com Funções: Refatorei o código para separar cada operação (depositar, sacar, extrato) em funções dedicadas (depositar(), sacar(), exibir_extrato()). Essa otimização melhora significativamente a organização do código, a legibilidade, a reutilização e a facilidade de manutenção, tornando o projeto mais robusto e escalável para futuras expansões.
Este projeto demonstra a aplicação prática de estruturas de controle, manipulação de dados e, especialmente, os princípios de modularidade através de funções, essenciais no desenvolvimento de sistemas.
