import os
import asyncio
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import TypeAsset
from utils import get_text_from_file


async def create_type_asset(type_asset: TypeAsset, session: AsyncSession = Depends(get_session)):
    session.add(type_asset)
    await session.commit()
    await session.refresh(type_asset)
    return type_asset


def main():
    breakpoint()
    path = os.getcwd() + '/jinja2_template/'
    template = get_text_from_file(path + 'painting.jinja2')
    paint = TypeAsset(description='Painting', data=template)
    session = get_session()
    session.add(paint)
    session.commit()
    session.refresh(paint)
    print(paint)


if __name__ == '__main__':
    main()
