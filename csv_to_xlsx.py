import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class CSVtoXLSXConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV to XLSX Converter")
        
        # Create and pack widgets
        self.label = tk.Label(root, text="Select a CSV file to convert:")
        self.label.pack(pady=10)
        
        self.upload_button = tk.Button(root, text="Upload CSV", command=self.upload_file)
        self.upload_button.pack(pady=10)
        
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next File", command=self.reset, state=tk.DISABLED)
        self.next_button.pack(pady=10)

    def upload_file(self):
        csv_file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        if not csv_file_path:
            self.progress_label.config(text="No file selected.")
            return
        
        self.progress_label.config(text=f"Selected file: {csv_file_path}")
        
        xlsx_file_path = filedialog.asksaveasfilename(
            title="Save XLSX File As",
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not xlsx_file_path:
            self.progress_label.config(text="No save location selected.")
            return
        
        self.progress_label.config(text=f"Processing file: {csv_file_path}")
        
        try:
            df = pd.read_csv(csv_file_path)
            df.to_excel(xlsx_file_path, index=False)
            self.progress_label.config(text=f"File saved successfully as: {xlsx_file_path}")
            self.next_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.progress_label.config(text="")

    def reset(self):
        self.progress_label.config(text="")
        self.next_button.config(state=tk.DISABLED)
        self.upload_file()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVtoXLSXConverter(root)
    root.mainloop()
