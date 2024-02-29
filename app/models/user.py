"""User Model."""
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class User(Base):
    """User Model."""

    __tablename__ = f"{DB_PREFIX}_user"
    id: Mapped[int] = mapped_column(primary_key=True)
    _username: Mapped[str] = mapped_column(
        "username", String(50), nullable=False, unique=True)
    _firstname: Mapped[str] = mapped_column(
        "firstname", String(50), nullable=False)
    _lastname: Mapped[str] = mapped_column(
        "lastname", String(50), nullable=False)
    _email: Mapped[str] = mapped_column(
        "email", String(100), nullable=False, unique=True)
    _password: Mapped[str] = mapped_column(
        "password", String(255), nullable=False)
    _created_at: Mapped[datetime] = mapped_column(
        "created_at", DateTime, nullable=False, default=None)
    _updated_at: Mapped[datetime] = mapped_column(
        "updated_at", DateTime, nullable=False, default=None)
    journal_entries = relationship("JournalEntries", back_populates="user")

    def serialize(self):
        """Serialize."""
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @property
    def username(self) -> str:
        """Get username."""
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        """Set username."""
        self._username = value

    @property
    def firstname(self) -> str:
        """Get firstname."""
        return self._firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        """Set firstname."""
        self._firstname = value

    @property
    def lastname(self) -> str:
        """Get lastname."""
        return self._lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        """Set lastname."""
        self._lastname = value

    @property
    def email(self) -> str:
        """Get email."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """Set email."""
        self._email = value

    @property
    def password(self) -> str:
        """Get password."""
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        """Set password."""
        self._password = value

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
