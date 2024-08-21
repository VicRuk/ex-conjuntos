import os

def validar_formato_arquivo(linhas):
    # 1. Primeira Linha
    try:
        num_operacoes = int(linhas[0].strip())
    except ValueError:
        print("Erro: A primeira linha deve conter um número inteiro representando o número de operações.")
        return False
    
    # 1.1 Primeira Linha precisa bater com os números de linhas
    if len(linhas) != 1 + 3 * num_operacoes:
        print("Erro: O número de linhas no arquivo não corresponde ao número de operações esperado.")
        return False

    # 2. Linhas
    linha = 1 
    for i in range(num_operacoes):
        # 2.1 Verificador se a linha bate
        if linha >= len(linhas):
            print("Erro: Formato do arquivo inválido. Faltam linhas para completar a operação.")
            return False

        # 2.2 Operador (U, I, D, C)
        oper = linhas[linha].strip()
        if oper not in ['U', 'I', 'D', 'C']:
            print(f"Erro: Código de operação inválido: {oper}. Deve ser U, I, D, ou C.")
            return False
        
        # 2.3 Declarar os Conjuntos
        conjunto1 = linhas[linha + 1].strip()
        conjunto2 = linhas[linha + 2].strip()

        if not conjunto1 or not conjunto2:
            print("Erro: Um dos conjuntos está vazio ou mal formatado.")
            return False
        
        # Cada conta são usadas 3 linhas
        linha += 3
    return True

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    diretorio_entrada = 'entradas'
    diretorio_resultado = 'resultado'
    
    if not os.path.exists(diretorio_resultado):
        os.makedirs(diretorio_resultado)

    arquivos = [f for f in os.listdir(diretorio_entrada) if f.endswith('.txt')]
    if not arquivos:
        print("Nenhum arquivo .txt encontrado na pasta.")
        return

    for nome_arquivo in arquivos:
        caminho_entrada = os.path.join(diretorio_entrada, nome_arquivo)
        caminho_saida = os.path.join(diretorio_resultado, os.path.splitext(nome_arquivo)[0] + ' - resultado.txt')
        
        with open(caminho_entrada, 'r', encoding='utf-8') as arquivo_entrada:
            linhas = arquivo_entrada.readlines()

        if not validar_formato_arquivo(linhas):
            continue

        num_operacoes = int(linhas[0].strip())
        linha = 1

        with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
            for i in range(num_operacoes):
                tipo_operacao = linhas[linha].strip()
                conjunto1 = set(linhas[linha + 1].strip().split(', '))
                conjunto2 = set(linhas[linha + 2].strip().split(', '))

                if tipo_operacao == 'U':
                    # União
                    nome_operacao = 'União'
                    resultado = sorted(list(conjunto1.union(conjunto2)))
                elif tipo_operacao == 'I':
                    # Interseção: Comuns nos conjuntos
                    nome_operacao = 'Interseção'
                    resultado = sorted(list(conjunto1.intersection(conjunto2)))
                elif tipo_operacao == 'D':
                    # Diferença: Conjunto1 que não está em Conjunto2
                    nome_operacao = 'Diferença'
                    resultado = sorted(list(conjunto1.difference(conjunto2)))
                elif tipo_operacao == 'C':
                    # Produto Cartesiano: pares ordenados
                    nome_operacao = 'Produto cartesiano'
                    resultado = sorted([f"({a}, {b})" for a in conjunto1 for b in conjunto2])
                else:
                    nome_operacao = ''
                    resultado = []

                conjunto1 = ', '.join(sorted(conjunto1))
                conjunto2 = ', '.join(sorted(conjunto2))
                resultado = ', '.join(resultado)

                linha_saida = f"{nome_operacao}: conjunto 1: {{{conjunto1}}}, conjunto 2: {{{conjunto2}}}. Resultado: {{{resultado}}}\n"
                print(linha_saida.strip())
                arquivo_saida.write(linha_saida)

                linha += 3

if __name__ == '__main__':
    main()