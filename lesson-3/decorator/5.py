def requires_auth(func):
    def wrapper(user):
        if user.get("is_admin"):
            return func(user)
        else:
            print("Доступ запрещен")
    return wrapper

@requires_auth
def perform_admin_action(user):
    print("Выполнение действия администратора")

user = {"username": "alice", "is_admin": False}
perform_admin_action(user)

