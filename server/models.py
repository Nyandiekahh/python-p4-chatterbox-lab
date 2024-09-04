from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Automatically set to current time on creation

    def __init__(self, body, username):
        self.body = body
        self.username = username

    def __repr__(self):
        return f'<Message {self.body}, {self.username}>'

    def to_dict(self):
        """Convert the Message object to a dictionary."""
        return {
            'id': self.id,
            'body': self.body,
            'username': self.username,
            'created_at': self.created_at.isoformat()  # Convert datetime to ISO 8601 format
        }
