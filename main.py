from UH import UH
from tabela_simbolos import tabela_simbolos
import sys # Biblioteca para utilizar argumentos


def main():

    maquina_turing_universal = UH(sys.argv[1])
    maquina_turing_universal.__representacao_maquina__()
    print("R(M):{}\nR(w):{}".format(maquina_turing_universal.representacao_maquina, maquina_turing_universal.representacao_palavra))
    maquina_turing_universal.__imprimir_representacao_maquina__()
if __name__ == '__main__':
    main()