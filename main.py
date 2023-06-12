from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session

# Import from models the corrsponding Database Classes
from models import Owner, TypeAsset, Asset

app = FastAPI()

# Define the routes for the app

@app.get('/')
def index():
    return {'data': {'message': 'This is the index page'}}


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get('/owners', response_model=list[Owner])
def get_owners(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Owner))
    owners = result.scalars().all()
    return [Owner(id=owner.id, name=owner.name, assets=owner.assets) for owner in owners]


@app.post("/owners")
async def add_DataModel(owner: Owner, session: AsyncSession = Depends(get_session)):
    owner = Owner(name=owner.name)
    session.add(owner)
    await session.commit()
    await session.refresh(owner)
    return owner







@app.post('/owners')
def create_owner(owner: Owner):
    session.add


@app.get('/type_assets')
def get_type_assets():
    """Get all type assets."""
    return session.query(TypeAsset).all()


@app.post("/type_assets")
def create_type_asset(type_asset: TypeAsset):
    """Create a new type asset."""
    session.add(type_asset)
    session.commit()
    return type_asset


@app.get("/assets")
def get_assets():
    """Get all assets."""
    return session.query(Asset).all()


@app.post("/assets")
def create_asset(asset: Asset):
    """Create a new asset."""
    session.add(asset)
    session.commit()
    return asset
