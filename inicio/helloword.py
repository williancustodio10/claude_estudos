nome = input("Digite seu nome: ")
idade = int(input("Quantos anos você tem? "))
print("Olá, ", nome, "tudo bem com você? Seja bem-vindo(a) ao mundo da programação em Python!")
print("Você tem", idade, "anos. Parabéns por estar aprendendo a programar!")

if idade < 18:
    print("Você é menor de idade. Ainda não pode programar sozinho, ein!")
else:
    print("Você é maior de idade. Agora pode programar sozinho, mas não se esqueça de estudar bastante!")
    