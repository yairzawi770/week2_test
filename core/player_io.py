def ask_player_action() -> str:
    user = input("enter S or H:")
    while user!="S" and user!="H":
        user = input("enter S or H:")
    return user
print(ask_player_action())
