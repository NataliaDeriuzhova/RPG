def show_state(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"Ваши жизни: {arg.hp}")
        res = func(*args, **kwargs)
        for arg in args:
            print(f"Ваши жизни: {arg.hp}")
        return res

    return wrapper
