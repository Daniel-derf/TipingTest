def checkLogin(
    user: str, password: str, DATABASE_ACCOUNTS: tuple[tuple[str, str], ...]
) -> bool:
    return (user, password) in DATABASE_ACCOUNTS


def getDatabaseAccounts() -> tuple[tuple[str, str], ...]:
    return (("Daniel", "tevo123"), ("Julia", "teo123"))


DATABASE_ACCOUNTS: tuple[tuple[str, str], ...]
DATABASE_ACCOUNTS = getDatabaseAccounts()


def loginTerminal(DATABASE_ACCOUNTS: tuple[tuple[str, str], ...]) -> None:
    user: str = input("Digite seu usuário: ")
    password: str = input("Digite sua senha: ")

    if checkLogin(user, password, DATABASE_ACCOUNTS):
        print("Logado com sucesso!")
    else:
        print("Credenciais incorretas. Tente novamente.")
        loginTerminal(DATABASE_ACCOUNTS)


loginTerminal(DATABASE_ACCOUNTS)
