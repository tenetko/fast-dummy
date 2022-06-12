from fastapi import Response
from fastapi.responses import FileResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class Handler:
    RESPONSE_TYPES = ["recheck_1", "recheck_2", "recheck_interline_1", "recheck_interline_2"]

    def __init__(self):
        pass

    @router.get("/{response_type}")
    def return_dummy_response(self, response_type):
        if response_type in self.RESPONSE_TYPES:
            with open(f"static/{response_type}.xml", "r") as res:
                return Response(
                    content=res.read(),
                    media_type="application/xml",
                    headers={},
                    status_code=200,
                )
        else:
            return FileResponse("static/index.html", status_code=200)
