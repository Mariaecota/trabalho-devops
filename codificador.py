
def codificar(senha):
    # inverte a palavra e depois move 2 casas pra frente
    return "".join([chr(ord(c)+2) for c in senha[::-1]])

def decodificar(token):
    # revertendo o processo
    return "".join([chr(ord(c)-2) for c in token])[::-1]

def main():
    while True:
        print("\n1 - Codificar senha")
        print("2 - Decodificar senha")
        print("3 - Sair")
        opc = input("Escolha uma opção: ")
        
        if opc == "1":
            senha = input("Digite a senha: ")
            token = codificar(senha)
            print("Senha codificada:", token)
        elif opc == "2":
            token = input("Digite o token: ")
            senha = decodificar(token)
            print("Senha decodificada:", senha)
        elif opc == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
