from typing import List, Tuple
from fastapi import APIRouter

from app.interface.api.v1.auth.auth_router import auth_router


class V1Router(APIRouter):
    def __init__(self, v1_sub_routers: List[APIRouter]):
        super().__init__()
        self.prefix = "/v1"
        self.include_routers(v1_sub_routers)

    def include_routers(self, v1_sub_routers: List[APIRouter]):
        for router in v1_sub_routers:
            self.include_router(router)


v1_sub_routers = [auth_router]

v1_router = V1Router(v1_sub_routers)
