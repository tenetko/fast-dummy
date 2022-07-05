from fastapi import Response
from fastapi.responses import FileResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class DeeplinkHandler:
    def __init__(self):
        pass

    @router.get("/sharp")
    def return_dummy_response_with_sharp(self):
        file_name = f"static/deeplink/deeplink_with_sharp.xml"
        return self.read_file(file_name)

    @router.get("/nosharp")
    def return_dummy_response_without_sharp(self):
        file_name = f"static/deeplink/deeplink_without_sharp.xml"
        return self.read_file(file_name)

    def read_file(self, file_name):
        with open(file_name, "r") as res:
            return Response(
                content=res.read(),
                media_type="application/json",
                headers={},
                status_code=200,
            )
