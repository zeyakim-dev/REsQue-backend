from typing import List
from fastapi import APIRouter

from app.interface.api.v1.auth.auth_router import auth_router


class V1Router(APIRouter):
    def __init__(self, sub_routers=List[APIRouter]):
        super().__init__()
        self.prefix = "v1/"
        self.include_routers(sub_routers)

    def include_routers(self, sub_routers):
        for sub_router in sub_routers:
            self.include_router(sub_router)


sub_routers = [auth_router]

v1_router = V1Router(sub_routers)
