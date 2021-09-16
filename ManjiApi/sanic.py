from sanic.app import Sanic
from types import SimpleNamespace

from ManjiApi.request.base import BaseRequest
from ManjiApi.request.yoshimitsu_gallery import YoshiGallRequest
from ManjiApi.request.frame_data import FrameDataRequest


class ManjiApiContext(SimpleNamespace):
    base_request: BaseRequest
    yoshigall_request: YoshiGallRequest
    framedata_request: FrameDataRequest


class ManjiApi(Sanic):
    ctx: ManjiApiContext