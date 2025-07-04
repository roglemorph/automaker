
import os


def create_latex_document(base_template_path, output_dir, output_filename, replacements):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the base LaTeX template
    with open(base_template_path, 'r') as file:
        latex_content = file.read()
    
    # Replace placeholders in the base template
    for placeholder, value in replacements.items():
        latex_content = latex_content.replace(placeholder, value)
    
    # Define the full path for the output file
    output_path = os.path.join(output_dir, output_filename)
    
    # Write the modified LaTeX content to the new file
    with open(output_path, 'w') as file:
        file.write(latex_content)
    
    print(f"LaTeX document created at: {output_path}")

def save_settings(settings, filename='settings.txt'):
    """Save user settings to a text file."""
    with open(filename, 'w') as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")
    print(f"Settings saved to {filename}.")

def load_settings(filename='settings.txt'):
    """Load user settings from a text file."""
    settings = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                settings[key] = value
        print(f"Settings loaded from {filename}.")
        print(settings)
    except FileNotFoundError:
        print(f"No settings file found. Using default settings.")
        settings =  {
        'template_path' :'default_template.tex',
        'output_dir' :'output_folder',

        'output_filename': "USETITLE",

        'author_name': "Author"}

    return settings


print("Hello, this program will create a latex document using a template. But you should use the GUI now!")


user_settings = load_settings()
base_template_path=user_settings['template_path']
author_name=user_settings['author_name']
output_dir = user_settings['output_dir']
output_filename=user_settings['output_filename']



def setUpLatexFile(title, template, author, output, filename, sections ):
    working_sections = "\section*{} \n"
    for user_section in sections:
         working_sections += "\n\section*{" + user_section + "}\n"


    replacements = {
    '<TITLE>': title,
    '<AUTHOR>': author,
    '<SECTIONS>': working_sections
    }
    if filename == "USETITLE":
        filename = str(title) + '.tex'
    print(f"Making tex file at {output}")
    create_latex_document(template, output, filename, replacements)
