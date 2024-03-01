"""Journal Entries Tags Model."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class JournalEntriesTags(Base):
    """Journal Entries Tags Model."""
    __tablename__ = f"{DB_PREFIX}_journal_entries_tags"
    journal_entry_id: Mapped[int] = mapped_column(
        ForeignKey(f"{DB_PREFIX}_journal_entries.id"), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey(f"{DB_PREFIX}_tags.id"), primary_key=True
    )
    journal_entry = relationship("JournalEntries", back_populates="tags")
    tag = relationship("Tag", back_populates="journal_entries")

    def serialize(self):
        """Serialize."""
        return {
            "journal_entry_id": self.journal_entry_id,
            "tag_id": self.tag_id
        }
