import sqlite3 as DB
from  Models.Pessoa import Pessoa

def ConectAndRun(command):
    try:
    
        connect = DB.connect("./banco.db")
        cursor = connect.cursor()
        
       
        response = cursor.execute(command)
        
        connect.commit()
        
        return response
    
    except  DB.DatabaseError as Err:
        print("Erro banco", Err)
    
    finally:
        if connect:
            cursor.close()
            connect.close()
    
    


def CadastraAluno():
    print("==== Cadastro de Alunos ====")
    while opc_aluno != "0":
        matricula_al = input("Digite a matricula do Aluno")
        nome_al = input("Qual o nome do Aluno")
        email_al = input("Qual o email")
        
        command = "Select matricula from Aluno where matricula ={matricula_al}"
        result = ConectAndRun(command)
        
        
        
        
        
        
    
    
    
    
def CadastraMateria():
def CadastraNota():

def main():
    while opc != '0':
        print ("O que deseja fazer hoje?")
        print(" 0 - Sair")
        print(" 1 - Cadastrar Aluno")
        print(" 2 - Cadastrar Materias")
        print(" 3 -  Cadastrar Nota")
        
        opc = input("O que deseja fazer hoje?")
        match opc:
            case"1":
                CadastraAluno()
            case "2":
                CadastraMateria()
            case "3":
                CadastraNota()
            case _:
                print("Digite uma opção Valida")
    print("Saindo do programa")