


def cadastro_usuario (usuarios):
    
    while True:
        nome = input('Insira seu nome completo: ').strip()
        if nome.replace(" ", "").isalpha():
            break
        print("Forma incorreta, seu nome deverá ser escrito apenas com letras.")
    while True:
        sobrenome = input("Insira seu sobrenome: ").strip()
        if sobrenome.replace(" ", "").isalpha():
            break
        print("Forma incorreta, seu sobrenome deverá ser escrito apenas com letras.")
     
    while True:
        ano_nascimento = input("Informe seu ano de nascimento (AAAA): ")
        if ano_nascimento.isdigit() and len(ano_nascimento) == 4:
            ano_nascimento = int(ano_nascimento)
            if not (1900 <= ano_nascimento <= 2025):
                print("Ano de nascimento não condizente.")
            else:
                break
        else:
            print("Informe um número que contenha 4 dígitos")
    
    while True:
        genero = input("Informe o sexo (1 - Feminino / 2 - Masculino): ").strip()

        if genero == "1":
            genero = "Feminino"
            break
        elif genero == "2":
            genero = "Masculino"
            break
        else:
            print("Número não correspondente,  digite 1 para Feminino ou 2 para Masculino.")
    
    while True:
        cpf = input("Agora, digite o seu CPF (apenas números, 11 dígitos): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("Cpf informado inválido, verifique se contém 11 dígitos.")
    while True:
        senha = input("Insira uma senha numérica de 4 dígitos: ").strip()
        if senha.isdigit() and len (senha) !=4:
            print("senha incorreta digite novamente")
        if senha.isdigit() and len(senha) == 4:
            break
    idade = 2025 - ano_nascimento    
    
    usuario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "genero": genero,
        "ano_nascimento": ano_nascimento,
        "idade": idade,
        "cpf": cpf,
        "senha" : senha
        }
    
    usuarios.append(usuario)
    salvar_dados(usuarios)
    print(f"Usuário:'{nome}' '{sobrenome}'com cpf:'{cpf}' cadastrado com sucesso!\n")

def todos_usuarios(usuarios):
    if not usuarios:
        print("nenhum usuário encontrado.\n")
        return

    print("\n🎥 Lista de usuários:")
    for f in usuarios:
        print(f"cpf: {f['cpf']} | {f['nome']} ({f['sobrenome']}) - {f['genero']} - Ano de nascimento: {f['ano_nascimento']} - Idade: {f['idade']} - Senha: {f[senha]}")
    print()

def unico_usuario(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    try:
        cpf_paciente = input("Digite o cpf do paciente: ")
        for f in usuarios:
            if f["cpf"] == cpf_paciente:
                print("\n Detalhes do paciente:")
                print(f"nome completo: {f['nome']} {f['sobrenome']}")
                print(f"Gênero: {f['genero']}")
                print(f"Ano de nascimento: {f['ano_nascimento']}")
                return
        print("paciente não encontrado.\n")
    except ValueError:
        print("cpf inválido.\n")

def atualizar_paciente(usuarios):
    todos_usuarios(usuarios)
    try:
        cpf_paciente = int(input("Digite o cpf do paciente que deseja atualizar: ")).strip()
        for f in usuarios:
            if f["cpf"] == cpf_paciente:
                while True:
                    correcao_nome = input("Agora, informe seu nome corretamente: ").strip()
                    if not correcao_nome:
                        break
                    if correcao_nome.replace(" ", "").isalpha():
                        f["nome"] = correcao_nome
                        break
                    else:
                        print("Forma inválida, permitido apenas letras")
                while True:
                    correcao_sobrenome = input("Agora, informe seu sobrenome corretamente: ").strip()
                    if not correcao_sobrenome:
                        break
                    if correcao_sobrenome.replace(" ", "").isalpha():
                        f["sobrenome"] = correcao_sobrenome
                        break
                    else:
                        print("Forma inválida, permitido apenas letras")
                while True:
                    correcao_ano = input("Novo ano de nascimento (AAAA, Enter para manter): ").strip()
                    if not novo_ano:
                        break
                    if correcao_ano.isdigit() and len(correcao_ano) == 4:
                        correcao_ano = int(correcao_ano)
                        if 1900 <= correcao_ano <= 2025:
                            f["ano_nascimento"] = correcao_ano
                            f["idade"] = date.today().year - novo_ano
                            break
                        else:
                            print("Ano não correspondente")
                    else:
                        print("Digite ano com 4 dígitos")
                while True:
                    correcao_genero = input("correcao gênero (1 - Feminino / 2 - Masculino, Enter para manter): ").strip()
                    if not correcao_genero:
                        break
                    if correcao_genero == "1":
                        f["genero"] = "Feminino"
                        break
                    elif correcao_genero == "2":
                        f["genero"] = "Masculino"
                        break
                    else:
                        print("digite 1 ou 2.")
                while True:
                    correcao_senha = input("Nova senha (4 dígitos, Enter para manter): ").strip()
                    if not correcao_senha:
                        break
                    if correcao_senha.isdigit() and len(correcao_senha) == 4:
                        f["senha"] = correcao_senha
                        break
                    else:
                        print("a senha precisa conter 4 dígitos")

                salvar_dados(usuarios)
                print("paciente atualizado com sucesso!\n")
                return
        print("paciente não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")
        

def deletar_paciente(usuarios):
    todos_usuarios(usuarios)
    cpf_paciente = input("Digite o CPF do paciente que deseja excluir: ").strip()

    for f in usuarios:
        if f["cpf"] == cpf_paciente:
            usuarios.remove(f)
            salvar_dados(usuarios)
            print(f" Usuário '{f['nome']} {f['sobrenome']}' removido com sucesso!\n")
            return

    print("Paciente não encontrado.\n")