Algoritmo "semnome"

Var
//
   primeira_nota: inteiro
   segunda_nota: inteiro
   terceira_nota: inteiro
   soma: real
   media: real
   Resultado: caractere
Inicio

  escreva("Digite a primeira nota: ")
  leia(primeira_nota)
  
  escreva("Digite a segunda nota: ")
  leia(segunda_nota)
  
  escreva("Digite a terceira nota: ")
  leia(terceira_nota)
  
  soma <- primeira_nota + segunda_nota + terceira_nota
  media <- soma / 2
  
  se media >=7 entao
     Resultado <- "Aprovado"
     
  senao
       Resultado <- "Reprovado"
    fimse
    
    
   escreval
   escreval("primeira_nota: ", primeira_nota)
   escreval("segunda_nota: ", segunda_nota)
   escreval("terceira_nota: ", terceira_nota)
   escreval("resultado: ", resultado)
    
    
    
    
Fimalgoritmo