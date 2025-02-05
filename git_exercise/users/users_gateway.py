from git_exercise.users.user import User


class UsersGateway:
    users: list[User]
    
    def __init__(self):
        self.users = [
            User(id=1, name="Fred Derf",email="fred@gmail.com"),
            User(id=2, name="Mary Yram",email="mary@gmail.com"),
            User(id=3, name="Jane Enaj",email="jane@gmail.com"),
            User(id=4, name="John Nhoj",email="john@gmail.com"),
        ]
    
    def find(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        
        return None
    
    def list(self):
        return self.users
    
    def add_user(self, name: str, email: str) -> int:
        new_id = self.users[-1].id + 1 if self.users else 1
        new_user = User(id=new_id, name=name, email=email)
        self.users.append(new_user)
        return new_id
    
    def update_user(self, user_id: int, name: str, email: str) -> User:
        user = self.find(user_id)
        if user:
            user.name = name
            user.email = email
            return {"id": user.id, "name": user.name, "email": user.email}
        return None
