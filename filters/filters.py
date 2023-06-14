from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsDigitCallBackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return isinstance(callback.data, str) and callback.data.isdigit()


class IsDelBookmarkCallBackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return isinstance(callback.data, str) and 'del' in callback.data and callback.data[:-3].isdigit()
