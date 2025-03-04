from typing import List

from sqlalchemy import  String, Text, SmallInteger, UUID, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import BaseModel, table_name_tenant, table_name_tenant_default_model


# class Tenant(BaseModel):
class Tenant(BaseModel):
    __tablename__ = table_name_tenant

    name = mapped_column('name', String, nullable=False, unique=True)
    plan = mapped_column('plan', SmallInteger)
    status = mapped_column('status', SmallInteger)
    encrypted_public_key = mapped_column('encrypted_public_key', Text)
    config = mapped_column('config', Text)

    # users = relationship("User", secondary="pivot_tenant_to_user")
    apps: Mapped[List["App"]] = relationship(back_populates="tenant")
    model_providers: Mapped[List["ModelProvider"]] = relationship(back_populates="tenant")

    def __repr__(self):
        return (
            f"<Tenant(id={self.id}, "
            f"name='{self.name}', "
            f"plan={self.plan}, "
            f"status={self.status}, "
            f"encrypted_public_key='{self.encrypted_public_key[:10]}...', "
            f"config='{self.config[:10]}...')>"
        )


class TenantDefaultModel(BaseModel):
    __tablename__ = table_name_tenant_default_model

    tenant_uuid = mapped_column('tenant_uuid', ForeignKey(table_name_tenant + '.uuid'), nullable=False)
    provider_name = mapped_column('provider_name', String(40), nullable=False)
    name = mapped_column('name', String(255), nullable=False)
    type = mapped_column('type', String(40), nullable=False)

