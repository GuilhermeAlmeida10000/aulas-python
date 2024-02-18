# Definindo uma função (sub-rotina)
def saudacao(nome):
    return "Olá, " + nome + "!"

# Chamando a função
nome_usuario = input("Digite seu nome: ")
mensagem = saudacao(nome_usuario)
print(mensagem)
