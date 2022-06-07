from fastapi import Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class Handler:
    def __init__(self):
        pass

    @router.get("/")
    def return_dummy_response(self):
        with open("static/response.xml", "r") as res:
            return Response(
                content=res.read(),
                media_type="application/xml",
                headers={},
                status_code=200,
            )
