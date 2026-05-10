import tkinter as tk
from tkinter import filedialog
from log_analyzer import LogAnalyzer


def open_file():
    path = filedialog.askopenfilename(
        filetypes=[("Log files", "*.log")]
    )

    if not path:
        return

    analyzer = LogAnalyzer(path)
    analyzer.parse_logs()

    result.delete("1.0", tk.END)
    result.insert(
        tk.END,
        str(analyzer.summary_report())
    )


root = tk.Tk()
root.title("Log File Analyzer")
root.geometry("500x400")

button = tk.Button(
    root,
    text="Open Log File",
    command=open_file
)

button.pack(pady=20)

result = tk.Text(root)
result.pack(fill="both", expand=True)

root.mainloop()