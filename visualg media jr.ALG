Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis 
   nome: caracter
   idade: inteiro
   primeira_nota: real
   segunda_nota: real
   soma: real
   media: real
   resultado: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   // entrada de dadsos
   escreva("Digite o nome de usuario:")
   leia(nome)
   
   escreva("Digite a sua idade: ")
   leia(idade)

   escreva("Digite a primeira nota: ")
   leia(primeira_nota)
   
   escreva("Digite a segunda nota: ")
   leia(segunda_nota)

   soma <- primeira_nota + segunda_nota
   media <- soma / 2


   se media >=7 entao
      resultado <- "Aprovado"
   senao
        resultado <- "Reprovado"
   fimse



   //SAÍDA
   escreval
   escreval("nome: ", nome)
   escreval("idade: ", idade)
   escreval("media: ", media)
   escreval("resultado: ", resultado)
   

Fimalgoritmo