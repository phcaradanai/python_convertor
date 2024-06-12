import pandas as pd
from tkinter import *
from tkinter import Tk, Button,Label, filedialog, messagebox
from PIL import Image

class FileConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter")

        # CSV to XLSX section
        self.csv_label = Label(root, text="CSV to XLSX Converter:",bg="blue")
        self.csv_label.pack(pady=10)
        
        self.csv_button = Button(root, text="Upload CSV", command=self.upload_csv)
        self.csv_button.pack(pady=10)
        
        self.csv_file_label = Label(root, text="")
        self.csv_file_label.pack(pady=5)
        
        self.csv_progress = Label(root, text="")
        self.csv_progress.pack(pady=5)
        
        self.csv_next_button = Button(root, text="Next CSV File", command=self.reset_csv, state='disabled')
        self.csv_next_button.pack(pady=5)

        # PNG to JPG and JPG to PNG section
        self.image_label = Label(root, text="Image Converter (PNG <-> JPG):",bg="blue")
        self.image_label.pack(pady=20)
        
        self.image_button = Button(root, text="Upload Image", command=self.upload_image)
        self.image_button.pack(pady=10)
        
        self.image_file_label = Label(root, text="",)
        self.image_file_label.pack(pady=5)
        
        self.image_progress = Label(root, text="",)
        self.image_progress.pack(pady=5)
        
        self.image_next_button = Button(root, text="Next Image File", command=self.reset_image, state='disabled')
        self.image_next_button.pack(pady=5)

    def upload_csv(self):
        print("Uploading CSV...")
        csv_file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        print("CSV file selected:", csv_file_path)
        if not csv_file_path:
            self.csv_progress.config(text="No file selected.")
            return
        
        self.csv_file_label.config(text=f"Selected file: {csv_file_path}")
        print("Selected CSV file label:", self.csv_file_label.cget("text"))
        self.csv_file_label.pack()  # Fix: Added pack()

        xlsx_file_path = filedialog.asksaveasfilename(
            title="Save XLSX File As",
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        print("XLSX file selected:", xlsx_file_path)
        if not xlsx_file_path:
            self.csv_progress.config(text="No save location selected.")
            return
        
        self.csv_progress.config(text=f"Processing file: {csv_file_path}")
        
        try:
            df = pd.read_csv(csv_file_path)
            df.to_excel(xlsx_file_path, index=False)
            self.csv_progress.config(text=f"File saved successfully as: {xlsx_file_path}")
            self.csv_next_button.config(state='normal')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.csv_progress.config(text="")

    def reset_csv(self):
        self.csv_file_label.config(text="")
        self.csv_progress.config(text="")
        self.csv_next_button.config(state='disabled')
        self.upload_csv()

    def upload_image(self):
        print("Uploading image...")
        image_file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")]
        )
        print("Image file selected:", image_file_path)
        if not image_file_path:
            self.image_progress.config(text="No file selected.")
            return
        
        self.image_file_label.config(text=f"Selected file: {image_file_path}")
        print("Selected image file label:", self.image_file_label.cget("text"))
        self.image_file_label.pack()  # Fix: Added pack()

        output_extension = '.jpg' if image_file_path.lower().endswith('.png') else '.png'
        
        output_file_path = filedialog.asksaveasfilename(
            title=f"Save Image File As ({output_extension})",
            defaultextension=output_extension,
            filetypes=[("Image Files", f"*{output_extension}")]
        )
        print("Output file selected:", output_file_path)
        if not output_file_path:
            self.image_progress.config(text="No save location selected.")
            return
        
        self.image_progress.config(text=f"Processing file: {image_file_path}")
        
        try:
            with Image.open(image_file_path) as img:
                rgb_img = img.convert('RGB') if output_extension == '.jpg' else img
                rgb_img.save(output_file_path)
            self.image_progress.config(text=f"File saved successfully as: {output_file_path}")
            self.image_next_button.config(state='normal')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.image_progress.config(text="")

    def reset_image(self):
        self.image_file_label.config(text="")
        self.image_progress.config(text="")
        self.image_next_button.config(state='disabled')
        self.upload_image()

if __name__ == "__main__":
    root = Tk()
    app = FileConverter(root)
    root.mainloop()
