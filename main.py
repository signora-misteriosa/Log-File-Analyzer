import argparse
from log_analyzer import LogAnalyzer


def main():
    parser = argparse.ArgumentParser(
        description="Log File Analyzer"
    )

    parser.add_argument(
        "file",
        help="Path to log file"
    )

    parser.add_argument(
        "--search",
        help="Search logs by keyword"
    )

    parser.add_argument(
        "--date",
        help="Filter logs by date (YYYY-MM-DD)"
    )

    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Show log visualization"
    )

    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file)
    analyzer.parse_logs()

    print("\n SUMMARY REPORT ")

    summary = analyzer.summary_report()

    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n LOG COUNTS ")

    counts = analyzer.count_by_level()

    for level, count in counts.items():
        print(f"{level}: {count}")

    analyzer.save_to_json()

    if args.search:
        print("\n SEARCH RESULTS ")

        results = analyzer.search_keyword(args.search)

        if results:
            for log in results:
                print(log)
        else:
            print("No matching logs found.")

    if args.date:
        print("\n DATE FILTER RESULTS ")

        results = analyzer.filter_by_date(args.date)

        if results:
            for log in results:
                print(log)
        else:
            print("No logs found for this date.")

    if args.visualize:
        analyzer.visualize()


if __name__ == "__main__":
    main()