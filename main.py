"""
Uma empresa deseja cadastrar em seu banco de dados os nomes de candidatos a vagas de trabalho.
Os nomes são recebidos dos usuários e é necessário adotar um padrão.
Foi decidido que os nomes estariam todos em letras maiúsculas e sem espaços no início e no final.
Também é desejado que o primeiro nome, nome do meio e sobrenome seja gravado de forma separada.
"""


class FormatarNome:
    def __init__(self, nome_completo):
        """

        :param nome_completo: recebe uma str de um nome
        """
        self.nome = nome_completo

    def primeiro_nome(self):
        """

        :return: retorna o primeiro nome em uppercase
        """
        nome = self.nome.split(' ')[0]
        nome = nome.upper()
        return nome

    def nome_do_meio(self):
        """

        :return: retorna os nomes do meio em uppercase
        """
        nome = self.nome.split(' ')[1:-1]
        nome = " ".join(nome)
        nome = nome.upper()
        return nome

    def ultimo_nome(self):
        """

        :return: retorna o ultimo nome em uppercase
        """
        nome = self.nome.split(' ')[-1]
        nome = nome.upper()
        return nome


a = FormatarNome('José Antunes da  Silva')

print(f'Primeiro Nome: {a.primeiro_nome()}')
print(f'Nome do meio: {a.nome_do_meio()}')
print(f'Sobrenome {a.ultimo_nome()}')
