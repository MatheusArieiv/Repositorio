# *** SISTEMA CLÍNICA VIDA+ ***
# Autor: Matheus Vieira Ponte Lima
# Projeto Integrado - Inovação ADS 2025.2
# Descrição: Sistem simples para cadastro e estatísticas de pacientes

# Lista para armazenar os dados dos pacientes.
# Cada paciente é um dicionário com 'nome', 'idade' e 'telefone'.
pacientes = []

def cadastro_de_pacientes():
    '''
    Cadastra um novo paciente na lista
    '''
    print('\nCADASTRO DE PACIENTES')
    nome = input('Nome do paciente:').strip() # '.strip()' remove espaços extras.

    # Valida para que 'idade' seja um número inteiro.
    try:
        idade = int(input('Idade do paciente:'))
    except ValueError:
        print('Idade inválida. Utilize apenas números inteiros.')
        return
    
    telefone = input('Telefone:').strip()

    # Cria dicionário com os dados e adiciona na lista.
    paciente = {'nome': nome, 'idade': idade, 'telefone': telefone}
    pacientes.append(paciente) # Adiona o novo registro na lista.

    print(f"Paciente {nome} cadastrado com sucesso!")

def estatisticas():
    '''
    Mostra estatísticas dos pacientes cadastrados
    '''
    if not pacientes:
        print('Nenhum paciente cadastrado.')
        return
    
    total = len(pacientes) # Conta quantos pacientes tem na lista.
    idades = [p['idade'] for p in pacientes] # Cria uma lista só com as idades.
    media_idade = sum(idades) / total # Soma tudo e divide.
    mais_novo = min(pacientes, key=lambda p: p['idade'])  # ||
    mais_velho = max(pacientes, key=lambda p: p['idade']) # Localizam o mais novo e o mais velho utilizando lambda para comparar idades.

    print('\nESTATÍSTICAS DA CLÍNICA')
    print(f"Total de pacientes: {total}.")
    print(f"Idade média de pacientes: {media_idade:.1f} anos.")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']}) anos.")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']}) anos.")

def buscar_paciente():
    '''
    Busca paciente pelo nome.
    '''
    busca_nome = input("\n Digite o nome do paciente que deseja buscar: ").strip().lower() # '.lower' tranforma o input em letras minusculas.
    encontrados = [p for p in pacientes if busca_nome in p['nome'].lower()]

    if encontrados:
        print('\n RESULATADO DA BUSCA')
        for p in encontrados:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
            print('Nenhum paciente encontrado com esse nome.')

def listagem_pacientes():
    '''
    Lista todos os pacientes
    '''
    if not pacientes:
        print('\n Nenhum paciente cadastrado.')
        return
    
    print('\n LISTA DE PACIENTES')
    for i, p in enumerate(pacientes, start=1): #'enumerate' enumera os pacientes.
        print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")

def menu():
    '''
    Menu principal do sistema
    '''
    while True:
        print('\n=== SISTEMA CLÍNICA VIDA+ ===')
        print('1. Cadastrar paciente')
        print('2. Ver estatísticas')
        print('3. Buscar paciente')
        print('4. Listar todos os pacientes')
        print('5. Sair')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cadastro_de_pacientes()
        elif opcao == '2':
            estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listagem_pacientes()
        elif opcao == '5':
            print('Saindo do sistema......')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    menu()



