''' Estacionamento
# Professor: Ariel Guareschi
# Aluno: Camila Queli Sockenski Thome
# Data: 17/06/2024
'''
carros = { # biblioteca "carros" responsável por armazenar os dados
    "CST-2006": { # meu veículo
        "marca": "Dodge",
        "modelo": "Charger srt",
        "cor": "Preto",
        "proprietario": "Milinha"
    }
}


def menu():  # mostra quais opções o usuário pode escolher
    print('1 - Estacionar veículo')
    print('2 - Remover veículo')
    print('3 - Veículos estacionados')
    print('4 - Está estacionado?')
    print('0 - Sair')
    try:
        opt = int(input('Digite uma opção: '))  # usuario escolhe a opção
        return opt  # programa retorna a opção
    except Exception as e:
        # caso a opção seja invalida o programa retorna as opções que podem ser escolhidas
        print(f'Opção inválida: {e}')
    return None


def add_veiculo():  # função que vai ser responsável pelo processo de inclusão dos carros na lista de estacionados
    try:
        # recebe a placa do veículo
        placa = input('Digite a placa do veículo: ')
        # recebe a marca do veículo
        marca = input('Digite a marca do veículo: ')
        # recebe o modelo do veículo
        modelo = input('Digite o modelo do veículo: ')
        cor = input('Digite a cor do veículo: ')  # recebe a cor do veículo
        # recebe o nome do proprietário do veículo
        proprietario = input('Digite o nome do proprietário: ')
        # contem todos os dados que foram recebidos acima
        dados = {"marca": marca, "modelo": modelo,
                 "cor": cor, "proprietario": proprietario}
        carros[placa] = dados  # adiciona todos os dados a biblioteca
        print('Veículo adicionado com sucesso!')
    except Exception as e:
        print(f'Alguma coisa foi digitada errada: {e}')


def remover_veiculo():  # opção para remover o veículo do estacionamento
    # pede que o usuário digite a placa
    placa = input('Digite a placa do veículo: ')
    if placa in carros:  # encontra a placa na biblioteca
        print(f'O carro de placa {placa} foi removido')
        del carros[placa]  # "del" serve para deletar o item da biblioteca
    else:
        # caso a placa digitada esteja incorreta ou não exista
        print('Veículo não encontrado')
    input('Pressione qualquer tecla para continuar')


def veiculos_estacionados():  # mostra os veículos estacionados
    if carros:
        for placa, dados in carros.items():  # encontra a placa na biblioteca
            print(f'Placa: {placa} - Marca: {dados["marca"]} - Modelo: {dados["modelo"]} - Cor: {dados["cor"]} - Proprietário: {
                  dados["proprietario"]}')
    else:
        # caso não haja veículos estacionados
        print('Nenhum veículo estacionado')
    input('Pressione qualquer tecla para continuar')


def esta_estacionado():  # mostra se o veículo está esstacionado, utilizando a placa como dado principal para encontráa-lo
    # recebe a placa para pesquisar na biblioteca
    placa = input('Digite a placa do veículo: ')
    if placa in carros:
        dados = carros[placa]  # encontra a placa
        print(f'Placa: {placa} - Marca: {dados["marca"]} - Modelo: {dados["modelo"]} - Cor: {
              dados["cor"]} - Proprietário: {dados["proprietario"]}')  
    else:
        # printa caso o veículo não seja encontrado
        print('Veículo não encontrado')
    input('Pressione qualquer tecla para continuar')


if __name__ == "__main__": #  # Verifica se este arquivo está sendo executado diretamente
    while True: # garante que seja executado em loop infinito até que seja digitado o "0"
        match menu(): # direciona para qual função deve ser executada
            case 1:
                add_veiculo() # opçãao do menu 
            case 2:
                remover_veiculo() # opçãao do menu 
            case 3:
                veiculos_estacionados() # opçãao do menu 
            case 4:
                esta_estacionado() # opçãao do menu 
            case 0: # opçãao do menu 
                break
