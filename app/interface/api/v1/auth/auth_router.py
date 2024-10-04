from fastapi import APIRouter


class AuthRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "/auth"
        self.tags = ["Authentication"]
        self.add_api_routes()

    def add_api_routes(self):
        @self.post("/login")
        async def login():
            return {"message": "로그인 성공"}

        @self.post("/register")
        async def register():
            return {"message": "회원가입 성공"}


auth_router = AuthRouter()
