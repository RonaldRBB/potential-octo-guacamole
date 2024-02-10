"""Routes."""
from flask import jsonify
from app.controllers import JournalEntries


def hello_world():
    """Hello world."""
    return jsonify({"message": "Hello World!"}), 404


def setup_routes(app):
    """Setups routes."""
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])

    app.add_url_rule("/journal_entries", "journal_entries", JournalEntries().index, methods=["GET"])
    app.add_url_rule("/journal_entry", "journal_entrie_create", JournalEntries().create, methods=["POST"])
    app.add_url_rule("/journal_entry/<int:id>", "journal_entrie_show", JournalEntries().show, methods=["GET"])
    app.add_url_rule("/journal_entry/<int:id>", "journal_entrie_update", JournalEntries().update, methods=["PUT"])
    app.add_url_rule("/journal_entry/<int:id>", "journal_entrie_delete", JournalEntries().delete, methods=["DELETE"])