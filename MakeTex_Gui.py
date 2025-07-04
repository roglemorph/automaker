import tkinter as tk
from tkinter import filedialog
import makeTex

settings = makeTex.load_settings()
base_template_path=settings['template_path']
author_name=settings['author_name']
output_dir = settings['output_dir']
output_filename=settings['output_filename']


def load_settings():
    global settings
    global base_template_path
    global author_name
    global output_dir
    global output_filename
    settings = makeTex.load_settings()
    base_template_path=settings['template_path']
    author_name=settings['author_name']
    output_dir = settings['output_dir']
    output_filename=settings['output_filename']

    


def launch_gui():
    root = tk.Tk()
    root.title("LaTeX Generator")
    root.geometry("400x250")
    root.configure(bg="#2e2e2e")

    # HUD label
    hud_label = tk.Label(root, text=f'Welcome to the LaTeX Generator!', fg="white", bg="#2e2e2e", font=("Helvetica", 14))
    hud_label.pack(pady=20)

    # Buttons
    btn_generate = tk.Button(root, text="Generate", width=20, command=generate_tex_file)
    btn_generate.pack(pady=10)

    btn_settings = tk.Button(root, text="Settings", width=20, command=open_settings_window)
    btn_settings.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", width=20, command=root.quit)
    btn_exit.pack(pady=10)

    root.mainloop()

def generate_tex_file():
    print("Generate button clicked!")
    popup = tk.Toplevel()
    popup.title("Create LaTeX File")
    popup.geometry("700x500")
    popup.configure(bg="#2e2e2e")


    #  Title
    tk.Label(popup, text="Title:", fg="white", bg="#2e2e2e").pack(pady=5)
    entry_title = tk.Entry(popup, width=40)
    entry_title.pack()
    
    # Section Titles
    tk.Label(popup, text="Section Titles (comma or newline separated):", fg="white", bg="#2e2e2e").pack(pady=5)
    section_box = tk.Text(popup, width=50, height=5)
    section_box.pack()
    # Author
    tk.Label(popup, text="Author:", fg="white", bg="#2e2e2e").pack(pady=5)
    entry_author = tk.Entry(popup, width=40)
    entry_author.insert(0, author_name)
    entry_author.pack()

    #  Filename
    tk.Label(popup, text="Filename:", fg="white", bg="#2e2e2e").pack(pady=5)
    entry_filename = tk.Entry(popup, width=40)
    entry_filename.insert(0, output_filename)
    entry_filename.pack()

    # Template Path + Browse
    tk.Label(popup, text="Template Path:", fg="white", bg="#2e2e2e").pack(pady=5)
    frame_template = tk.Frame(popup, bg="#2e2e2e")
    entry_template = tk.Entry(frame_template, width=40)
    entry_template.insert(0, base_template_path)
    entry_template.pack(side=tk.LEFT, padx=2)
    tk.Button(frame_template, text="Browse", command=lambda: browse_file(entry_template)).pack(side=tk.LEFT)
    frame_template.pack()

    # Output Directory + Browse
    tk.Label(popup, text="Output Directory:", fg="white", bg="#2e2e2e").pack(pady=5)
    frame_output = tk.Frame(popup, bg="#2e2e2e")
    entry_output = tk.Entry(frame_output, width=80)
    entry_output.insert(0, output_dir)
    entry_output.pack(side=tk.LEFT, padx=2)
    tk.Button(frame_output, text="Browse", command=lambda: browse_folder(entry_output)).pack(side=tk.LEFT)
    frame_output.pack()
    

    # --- Browse Logic ---
    def browse_file(entry):
        path = filedialog.askopenfilename(filetypes=[("TeX files", "*.tex")])
        if path:
            entry.delete(0, tk.END)
            entry.insert(0, path)

    def browse_folder(entry):
        path =filedialog.askdirectory()
        if path:
            entry.delete(0, tk.END)
            entry.insert(0, path)


   # --- Submit Button Logic ---
    def submit_form():
        author = entry_author.get()
        title = entry_title.get()
        filename = entry_filename.get()
        template = entry_template.get()
        output = entry_output.get()
        section_input = section_box.get("1.0", tk.END).strip()
        import re
        sections = re.split(r'[\n,]+', section_input)
        sections = [s.strip() for s in sections if s.strip()]
        filename="USETITLE"
        print("Submitted Values:")
        print("Author:", author)
        print("Title:", title)
        print("Template:", template)
        print("Output Directory:", output)
        makeTex.setUpLatexFile(title, template, author, output, filename, sections)
        popup.destroy()
 
    # --- Submit + Close Buttons ---
    tk.Button(popup, text="Submit", command=submit_form).pack(pady=10)
    tk.Button(popup, text="Cancel", command=popup.destroy).pack()

def open_settings_window():
    popup = tk.Toplevel()
    popup.title("Settings")
    popup.geometry("450x400")
    popup.configure(bg="#2e2e2e")

    tk.Label(popup, text="Edit Default Settings", fg="white", bg="#2e2e2e", font=("Helvetica", 12)).pack(pady=10)

    # --- Entry Fields ---

    # Author
    tk.Label(popup, text="Default Author:", fg="white", bg="#2e2e2e").pack()
    entry_author = tk.Entry(popup, width=50)
    entry_author.insert(0, author_name)
    entry_author.pack()
    
    #Title
    tk.Label(popup, text="Default Title:", fg="white", bg="#2e2e2e").pack()
    entry_title = tk.Entry(popup, width=50)
    entry_title.insert(0, "None (unimplemented)")
    entry_title.pack()

    # Filename
    tk.Label(popup, text="Default Filename:", fg="white", bg="#2e2e2e").pack()
    entry_filename = tk.Entry(popup, width=50)
    entry_filename.insert(0, output_filename)
    entry_filename.pack()

    # Template Path + Browse
    tk.Label(popup, text="Default Template Path:", fg="white", bg="#2e2e2e").pack()
    frame_template = tk.Frame(popup, bg="#2e2e2e")
    entry_template = tk.Entry(frame_template, width=40)
    entry_template.insert(0, base_template_path)
    entry_template.pack(side=tk.LEFT, padx=2)
    tk.Button(frame_template, text="Browse", command=lambda: browse_file(entry_template)).pack(side=tk.LEFT)
    frame_template.pack()

    # Output Directory + Browse
    tk.Label(popup, text="Default Output Directory:", fg="white", bg="#2e2e2e").pack()
    frame_output = tk.Frame(popup, bg="#2e2e2e")
    entry_output = tk.Entry(frame_output, width=40)
    entry_output.insert(0, output_dir)
    entry_output.pack(side=tk.LEFT, padx=2)
    tk.Button(frame_output, text="Browse", command=lambda: browse_folder(entry_output)).pack(side=tk.LEFT)
    frame_output.pack()

    def browse_file(entry):
        path = tk.filedialog.askopenfilename(filetypes=[("TeX files", "*.tex")])
        if path:
            entry.delete(0, tk.END)
            entry.insert(0, path)

    def browse_folder(entry):
        path = tk.filedialog.askdirectory()
        if path:
            entry.delete(0, tk.END)
            entry.insert(0, path)

    def save_settings_and_close():
        default_author = entry_author.get()
        default_filename = entry_filename.get()
        default_template = entry_template.get()
        default_output = entry_output.get()
        new_settings =  {
        'template_path' :default_template,
        'output_dir' :default_output,
        'output_filename': default_filename,
        'author_name':default_author}

        makeTex.save_settings(new_settings)
        load_settings()
        print("Settings updated.")
        popup.destroy()

    # Buttons
    tk.Button(popup, text="Save", command=save_settings_and_close).pack(pady=10)
    tk.Button(popup, text="Cancel", command=popup.destroy).pack()



launch_gui()
