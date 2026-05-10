from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str

    def to_dict(self):
        return {
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "level": self.level,
            "message": self.message
        }