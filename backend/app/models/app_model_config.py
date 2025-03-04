from typing import List

from sqlalchemy import UUID, Text, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import BaseModel, table_name_app_model_config, table_name_model_provider, table_name_app


class AppModelConfig(BaseModel):
    __tablename__ = table_name_app_model_config

    app_uuid = mapped_column(UUID(as_uuid=True), ForeignKey(table_name_app + '.uuid'))
    model_provider_uuid = mapped_column(UUID(as_uuid=True), ForeignKey(table_name_model_provider + '.uuid'))
    configs = mapped_column(Text, nullable=True)
    persona_prompt = mapped_column(Text)

    app: Mapped["App"] = relationship(back_populates="app_model_configs", foreign_keys=[app_uuid])
    current_selected_app: Mapped["App"] = relationship(back_populates="app_model_configs",
                                                       foreign_keys="[App.app_model_config_uuid]",
                                                       uselist=False)
    model_provider: Mapped["ModelProvider"] = relationship(back_populates="app_model_config",
                                                           foreign_keys=[model_provider_uuid])
