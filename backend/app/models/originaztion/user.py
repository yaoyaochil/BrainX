from enum import Enum
from typing import List, Optional, Dict, Union, Any

from sqlalchemy import Column, String, UUID, BigInteger, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.base import BaseModel, table_name_user



class UserMetadataKeysEnum(str, Enum):
    """
    Enum for the keys of the metadata map for a document
    """
    SEC_DOCUMENT = "sec_user"


DocumentMetadataMap = Dict[Union[UserMetadataKeysEnum, str], Any]


class User(BaseModel):
    __tablename__ = table_name_user

    account = mapped_column(String, unique=True, nullable=False)
    name = mapped_column(String)
    nick_name = mapped_column(String)
    desc = mapped_column(String)
    position_id = mapped_column(Integer)
    job_title = mapped_column(String)
    department_id = mapped_column(Integer)
    mobile_phone = mapped_column(String)
    gender = mapped_column(String)
    email = mapped_column(String)
    external_email = mapped_column(String)
    avatar = mapped_column(String)
    password = mapped_column(String)
    status = mapped_column(String)
    is_reserved = mapped_column(Boolean, default=False)
    is_activated = mapped_column(Boolean, default=False)
    we_work_user_id = mapped_column(String)

    # tenants: Mapped[List[Tenant]] = relationship(secondary="pivot_tenant_to_user")

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f"account='{self.account}', "
            f"name='{self.name}', "
            f"nick_name='{self.nick_name}', "
            f"desc='{self.desc[:10]}...', "
            f"position_id={self.position_id}, "
            f"job_title='{self.job_title}', "
            f"department_id={self.department_id}, "
            f"mobile_phone='{self.mobile_phone}', "
            f"gender='{self.gender}', "
            f"email='{self.email}', "
            f"external_email='{self.external_email}', "
            f"avatar='{self.avatar}', "
            f"password='{self.password[:10]}...', "
            f"status='{self.status}', "
            f"is_reserved={self.is_reserved}, "
            f"is_activated={self.is_activated}, "
            f"we_work_user_id='{self.we_work_user_id}')>"
        )
