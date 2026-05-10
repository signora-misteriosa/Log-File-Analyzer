import re
import json
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

from log_entry import LogEntry


class LogAnalyzer:
    LOG_PATTERN = re.compile(
        r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(INFO|ERROR|WARNING)\] (.+)'
    )

    def __init__(self, file_path):
        self.file_path = file_path
        self.logs = []

    def parse_logs(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                match = self.LOG_PATTERN.match(line.strip())

                if match:
                    timestamp = datetime.strptime(
                        match.group(1),
                        "%Y-%m-%d %H:%M:%S"
                    )

                    level = match.group(2)
                    message = match.group(3)

                    self.logs.append(
                        LogEntry(timestamp, level, message)
                    )
                else:
                    print("Malformed line skipped:", line.strip())

    def count_by_level(self):
        return Counter(log.level for log in self.logs)

    def save_to_json(self, filename="results.json"):
        data = [log.to_dict() for log in self.logs]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Saved to", filename)

    def search_keyword(self, keyword):
        return [
            log for log in self.logs
            if keyword.lower() in log.message.lower()
        ]

    def filter_by_date(self, date_string):
        target = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        ).date()

        return [
            log for log in self.logs
            if log.timestamp.date() == target
        ]

    def summary_report(self):
        if not self.logs:
            return "No logs found."

        errors = [
            log.message
            for log in self.logs
            if log.level == "ERROR"
        ]

        common_error = (
            Counter(errors).most_common(1)[0][0]
            if errors else "None"
        )

        report = {
            "Total Entries": len(self.logs),
            "First Log": self.logs[0].timestamp,
            "Last Log": self.logs[-1].timestamp,
            "Most Common Error": common_error
        }

        return report

    def visualize(self):
        counts = self.count_by_level()

        plt.bar(
            counts.keys(),
            counts.values()
        )

        plt.title("Log Frequency")
        plt.xlabel("Log Level")
        plt.ylabel("Count")
        plt.show()