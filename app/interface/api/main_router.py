from typing import List
from fastapi import APIRouter

from app.interface.api.v1.v1_router import v1_router


class MainRouter(APIRouter):
    def __init__(self, version_routers: List[APIRouter]):
        super().__init__()
        self.prefix = "/api"
        self.include_routers(version_routers)

    def include_routers(self, version_routers: List[APIRouter]):
        for router in version_routers:
            self.include_router(router)


version_routers = [v1_router]

main_router = MainRouter(version_routers)
