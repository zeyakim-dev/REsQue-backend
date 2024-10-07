from fastapi import APIRouter


class AuthRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "auth/"
        self.add_api_route("/login", self.login, methods=["POST"])
        self.add_api_route("/register", self.register, methods=["POST"])

    async def login(self):
        # 로그인 로직
        pass

    async def register(self):
        # 회원가입 로직
        pass


auth_router = AuthRouter()
