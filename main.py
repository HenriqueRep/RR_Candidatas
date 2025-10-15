from database import inicializar_bd, inserir_candidata_db, listar_candidatas_db

def entrada_dados():
    print("\n--- INSERIR NOVA CANDIDATA ---")

    nome = input("Digite o Nome da Candidata: ").strip()
    clube = input("Digite o Clube da Candidata: ").strip()

    if not nome or not clube:
        print("Nome e Clube são obrigatórios. Operação cancelada.")
        return

    candidata_id = inserir_candidata_db(nome, clube) 

    if candidata_id:
        print(f"\nCandidata '{nome}' cadastrada com sucesso! ID: {candidata_id}")
    else:
        print("Não foi possivel cadastrar candidata.")


def exibir_listagem():
    candidatas = listar_candidatas_db() 
    
    print("\n--- LISTA DE CANDIDATAS REGISTRADAS ---")

    if not candidatas:
        print("Não há candidatas registradas no banco de dados!")
        return

    for id, nome, clube in candidatas:
        print("-" * 35)
        print(f"ID: {id}")
        print(f"Nome: {nome}")
        print(f"Clube: {clube}")
    print("-" * 35)

def menu_principal(): 
    
    inicializar_bd() 
    
    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE CADASTRO (PYTHON MODULAR)   ")
        print("=" * 40)
        print("1. Inserir Nova Candidata")
        print("2. Listar Todas as Candidatas")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == '1':
            entrada_dados()
        elif escolha == '2':
            exibir_listagem()
        elif escolha == '3':
            print("Sair")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 3.")


if __name__ == "__main__":
    menu_principal()
