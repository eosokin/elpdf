import tkinter as tk
import tkinter.filedialog as fd
import os
import subprocess

# function to handle button click event
def compress_pdf():
    # open file dialog to select PDF file
    file_path = fd.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    # check if a file was selected
    if file_path:
        # get output file path from user
        output_path = fd.asksaveasfilename(defaultextension=".pdf")
        
        # check if a file name was provided
        if output_path:
            # construct the command to compress the PDF using Ghostscript
            command = f'gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/default -dNOPAUSE -dBATCH -sOutputFile="{output_path}" "{file_path}"'
            
            try:
                # run the command in a subprocess
                subprocess.run(command, shell=True, check=True)
                
                # show a message box with the output file path
                tk.messagebox.showinfo("Compression Complete", f"PDF file compressed and saved to:\n{output_path}")
            except subprocess.CalledProcessError as e:
                # show an error message box if the command failed
                tk.messagebox.showerror("Compression Error", f"Error compressing PDF file:\n{e}")
        else:
            # show an error message box if no output file name was provided
            tk.messagebox.showerror("Output Error", "Please provide a name for the compressed PDF file.")
    else:
        # show an error message box if no input file was selected
        tk.messagebox.showerror("Input Error", "Please select a PDF file to compress.")

# create a window, a label, and a button
window = tk.Tk()
window.title("ELPDF Compressor")
window.geometry("400x200")
window.configure(bg="#e6e6e6")

label = tk.Label(window, text="ELPDF Compressor", font=("Arial Bold", 20), bg="#e6e6e6")
button = tk.Button(window, text="Compress PDF", command=compress_pdf, font=("Arial Bold", 16), fg="white", bg="#4c4c4c", activebackground="#666666", activeforeground="white", borderwidth=0, padx=20, pady=10)

# add the label and button to the window and show the window
label.pack(pady=20)
button.pack()
window.mainloop()
