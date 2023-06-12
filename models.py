from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Owner(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    assets: Optional[List['Asset']] = Relationship(back_populates='owner')


class TypeAsset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    data: str

    assets: Optional[List['Asset']] = Relationship(back_populates='type_asset')


class Asset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    price: float
    purchase_date: datetime
    data: str

    type_asset_id: Optional[int] = Field(default=None, foreign_key='typeasset.id')
    type_asset: Optional[TypeAsset] = Relationship(back_populates='assets')
    owner_id: Optional[int] = Field(default=None, foreign_key='owner.id')
    owner: Optional[Owner] = Relationship(back_populates='assets')
