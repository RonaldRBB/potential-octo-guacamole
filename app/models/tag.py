from datetime import datetime
from typing import List

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base

from .user import User


class Tag(Base):
    """Tag Model."""
    __tablename__ = f"{DB_PREFIX}_tags"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    _user_id: Mapped[int] = mapped_column("user_id", ForeignKey(User.id))
    _name: Mapped[str] = mapped_column("name", String(100), nullable=False)
    _created_at: Mapped[datetime] = mapped_column(
        "created_at", DateTime, nullable=False, default=None)
    _updated_at: Mapped[datetime] = mapped_column(
        "updated_at", DateTime, nullable=False, default=None)
    journal_entries: Mapped[List["JournalEntriesTags"]] = relationship(
        back_populates="tag")
    user = relationship("User", back_populates="tags")

    def serialize(self):
        """Serialize."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set name."""
        self._name = value

    @property
    def created_at(self) -> datetime:
        """Get created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        """Set created_at."""
        self._created_at = value

    @property
    def updated_at(self) -> datetime:
        """Get updated_at."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value: datetime) -> None:
        """Set updated_at."""
        self._updated_at = value
