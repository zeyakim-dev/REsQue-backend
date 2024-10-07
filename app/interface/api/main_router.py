from typing import List
from fastapi import APIRouter

from app.interface.api.v1.v1_router import v1_router


class MainRouter(APIRouter):
    def __init__(self, sub_routers=List[APIRouter]):
        super().__init__()
        self.prefix = "api/"
        self.include_routers(sub_routers)

    def include_routers(self, sub_routers):
        for sub_router in sub_routers:
            self.include_router(sub_router)


sub_routers = [v1_router]

main_router = MainRouter(sub_routers)
