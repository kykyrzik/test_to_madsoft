import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column


class ModelWithMixinUUID:
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )
