"""Journal Entries Model."""

from datetime import datetime

from sqlalchemy import DateTime, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from config import DB_PREFIX, Base

from .user import User


class JournalEntries(Base):
    """Journal Entries Model."""

    __tablename__ = f"{DB_PREFIX}_journal_entries"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column("user_id", ForeignKey(User.id))
    _title: Mapped[str] = mapped_column("title", String(255), nullable=False)
    _content: Mapped[str] = mapped_column("content", Text, nullable=False)
    _created_at: Mapped[datetime] = mapped_column(
        "created_at", DateTime, nullable=False, default=None)
    _updated_at: Mapped[datetime] = mapped_column(
        "updated_at", DateTime, nullable=False, default=None)

    @property
    def user_id(self) -> int:
        """Get user_id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        """Set user_id."""
        self._user_id = value

    @property
    def title(self) -> str:
        """Get title."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set title."""
        self._title = value

    @property
    def content(self) -> str:
        """Get content."""
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        """Set content."""
        self._content = value

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
