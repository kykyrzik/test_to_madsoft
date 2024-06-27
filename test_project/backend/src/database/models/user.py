from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import BIGINT

from test_project.backend.src.database.models.base.base import Base
from test_project.backend.src.database.models.base import ModelWithMixinUUID, ModelWithTimeMixin


class User(Base, ModelWithMixinUUID, ModelWithTimeMixin):
    tg_id: Mapped[int] = mapped_column(BIGINT, nullable=True, index=True)
    username: Mapped[str] = mapped_column(nullable=True)