from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from app.models.tenant import TenantDefaultModel
from typing import List, Tuple
from app.schemas.tenant import TenantDefaultModelSchema


class TenantDefaultModelDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_tenant_default_model(self, model_data: TenantDefaultModelSchema) -> Tuple[
        TenantDefaultModel | None, Exception|None]:
        try:
            tenant_default_model = TenantDefaultModel(**model_data.dict())
            self.db.add(tenant_default_model)
            await self.db.commit()
            return tenant_default_model, None
        except SQLAlchemyError as e:
            await self.db.rollback()
            return None, e

    async def get_tenant_default_model_by_uuid(self, tenant_uuid: str) -> Tuple[
        List[TenantDefaultModel] | None, Exception | None]:
        try:
            stmt = select(TenantDefaultModel).filter(TenantDefaultModel.tenant_uuid == tenant_uuid)
            result = await self.db.execute(stmt)
            tenant_default_models = result.scalars().all()
            return tenant_default_models, None
        except SQLAlchemyError as e:
            return None, e

    async def delete_tenant_default_model(self, tenant_uuid: str, provider_name: str, model_name: str) -> Tuple[
        bool, Exception | None]:
        try:
            stmt = delete(TenantDefaultModel).where(
                TenantDefaultModel.tenant_uuid == tenant_uuid,
                TenantDefaultModel.provider_name == provider_name,
                TenantDefaultModel.name == model_name
            )
            await self.db.execute(stmt)
            await self.db.commit()
            return True, None
        except SQLAlchemyError as e:
            await self.db.rollback()
            return False, e
