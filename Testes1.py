# lista = ['bil', 'bow', 'be', 'gnis']
#
# for b in lista:
#     show = "my name is: " + b
#     print(show)

# def somarAte(limite):
#     '''função para somar até o limite, que é passado no parâmetro limite'''
#
#
#     soma = 0
#     for number in range(limite+1):
#         soma = soma + number
#
#     return soma
#
# print(somarAte(4))
#


# def somarAte(limite):
#     '''função para somar até o limite, que é passado no parânetro "limite"'''
#
#
#     somar = 0
#     numero = 1
#     while numero <= limite:
#         somar = somar + numero
#         numero = numero + 1
#
#     return somar
#
# print(somarAte(4))
#
#
# def sequeciaTresNMaisUm(n):
#     '''........'''
#
#
#     while n != 1:
#         if n % 2 == 0:
#             n = n//2
#             print(n)
#         else:
#             n = 3*n + 1
#             print(n)
#
#     resposta = 'laço finalizado'
#     print(resposta)
#
#
# print(sequeciaTresNMaisUm(10))
#
# print("x", '\t    ', "x + 1")
# print("---", '\t', "-----")
#
# for i in range(10):
#     print(i, '\t    ', i+1)

# def reverseName(nome):
#     ''' function that reverses name'''
#
#
#     nameSent = nome
#     nameReverse = ""
#     i = 1
#     while i < len(nameSent)+1:
#         nameReverse = nameReverse + nameSent[-i]
#         print(nameReverse)
#         i = i+1
#
#     print(nameReverse)
#
# nameInsert = "Julio"
# reverseName(nameInsert)


# codigo = "Eu quero MUITO ficar bom em Python, essa é a minha meta!!!1"
# print(codigo.find("A"))
# print(codigo.count("o"))
# print(codigo.upper())
# print(codigo.lower())
# print(codigo.index("quero"))
# print(codigo.split(" "))
# print(codigo.split(" "))
# print(codigo[:])
#
# print(ord("A"))
#
# conversa = "Hello Dear!"
# novaConversa = "Y" + conversa[1:]
# print(novaConversa)

# reverseBilbor = ""
# aluno = "bilbowbegnins"
# for inx in range(len(aluno)-1, -1, -1): #no start, mesmo que esteja passando o mesmo caractere do stop, por estar passando
#                                         #via len() é como se ele entedesse que é outro índice, e mesmo que tenda a ir a
#                                         #indice zero pelo fato do step ser -1, a condição de stop -1 ocorrerá porque
#                                         #após o valor descrescer até 0, ele retorna até a posição -1.
#     reverseBilbor = reverseBilbor + aluno[inx]
#
# print(reverseBilbor)

# nomes = ['julio', 'marco', 'forest', 'gump']
#
# alturas = [1.72, [1.76, 1.88], 1.92]
#
# nova_lista = nomes + alturas
#
# print(nova_lista)
# print(type(nova_lista))
# print(1.76 in alturas[1])
# print(id(alturas))
# print(id(nomes))
# print(id(nova_lista))
#
# jogos_play_2 = ['bom de guerra', 'grande tráfico de carros', 'mario bros', 'will smith o retorno do will']
# print(jogos_play_2)
# jogos_play_2[2:4] = ['O Hobbit', 'senhor dos aneis']
# print(jogos_play_2)
# del jogos_play_2[1]
# print(jogos_play_2)
#
# julio = ["21 anos", "1.72m", "março"]
# pedro = ["21 anos", "1.72m", "março"]
#
# print(julio == pedro)
# print(julio is pedro)
#
# print(id(julio))
# print(id(pedro))
#
# julio = pedro
#
# print(julio == pedro)
# print(julio is pedro)
#
# print(id(julio))
# print(id(pedro))
#
# print(julio)
# print(pedro)
#
# julio[0] = "exemplo"
#
# print(pedro)
#
# a = [1,2,8,7,9]
# a = [1,2,8,7,9]
# a.pop(2)
# print(a)


def primo(n):
    return (n%n == 0 and n%1==0) and (n%(n*2-1)!=0 and n%(n*2)!= 0)

def primes_ate(n):

    lista_primos = [num for num in range(2,n) if primo(num)]
    return lista_primos

print(primes_ate(55))