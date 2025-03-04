import uuid
from typing import Tuple, List

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, UUID, desc

from app.schemas.base import Pagination, ResponsePagination
from app.schemas.robot_chat.conversation import ConversationSchema

from app.service.base import paginate_query
from app.service.conversation.create import transform_conversation_to_reply

from app.models.robot_chat.conversation import Conversation


def transform_conversations_to_reply(conversations: [Conversation]) -> List[ConversationSchema]:
    data = [transform_conversation_to_reply(resource) for resource in conversations]
    # print(data)
    return data


async def get_conversation_list(
        db: AsyncSession,
        pagination: Pagination,
        app_uuid: str | None = None
) -> Tuple[List[ConversationSchema] | None, ResponsePagination | None, SQLAlchemyError | None]:
    stmt = (
        select(Conversation).
        where(Conversation.deleted_at.is_(None)).
        where(Conversation.app_uuid == app_uuid).
        order_by(desc(Conversation.updated_at))
    )
    # print(stmt)
    res, pg, exception = await paginate_query(db, stmt, Conversation, pagination, True)
    # print(res, pg, exception)
    if exception:
        return None, None, exception

    return transform_conversations_to_reply(res), pg, None
