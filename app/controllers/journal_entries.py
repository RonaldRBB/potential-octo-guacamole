"""Journal Entries."""
from flask import jsonify, request

from app.models import JournalEntries as JournalEntriesModel
from config import session


class JournalEntries:
    """Journal Entries."""

    def index(self):
        """Retorna la lista de entradas de journal."""
        entries = session.query(JournalEntriesModel).all()
        return jsonify([entry.serialize() for entry in entries]), 200

    def create(self):
        """Crea una nueva entrada de journal."""
        data = request.get_json()
        entry = JournalEntriesModel(
            user_id=data["user_id"],
            title=data["title"],
            content=data["content"],
            created_at="now()",
            updated_at="now()"
        )
        session.add(entry)
        session.commit()
        session.close()
        return jsonify("anda"), 201

    def show(self, id):
        """Retorna una sola entrada de journal."""
        entry = session.query(JournalEntriesModel).get(id)
        return jsonify(entry.serialize()), 200

    def update(self, id):
        """Actualiza una sola entrada de journal."""
        data = request.get_json()
        entry = session.query(JournalEntriesModel).get(id)
        entry.title = data["title"]
        entry.content = data["content"]
        session.commit()
        session.close()
        return jsonify(entry.serialize()), 200

    def delete(self, id):
        """Elimina una sola entrada de journal."""
        entry = session.query(JournalEntriesModel).get(id)
        session.delete(entry)
        session.commit()
        session.close()
        return jsonify(entry.serialize()), 200
