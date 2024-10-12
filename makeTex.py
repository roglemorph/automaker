
import os
import string


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
        #print(f"Settings loaded from {filename}.")
    except FileNotFoundError:
        print(f"No settings file found. Using default settings.")
        settings =  {
        'template_path' :'default_template.tex',
        'output_dir' :'output_folder',

        'output_filename': "USETITLE",

        'author_name': "Author"}

    return settings


#default settings


print("Hello, this program will create a latex document using a template.")


global user_settings

def main_loop(reloadSettings=True):
    global user_settings
    if reloadSettings:
        user_settings = load_settings()

    base_template_path=user_settings['template_path']
    author_name=user_settings['author_name']
    output_dir=user_settings['output_dir']
    output_filename=user_settings['output_filename']

    print(f'Settings:\n    Name: {author_name}\n    template path: {base_template_path}\n    target directory: {output_dir}\n    filename: {output_filename}\n')
    print("Commands:\n    mkfile {title}\n    change {A:author_name O:output_dir F:output_filename, T:template_path} {value}\n    default\n    exit\n")
    
    user_input = input("Enter command: ")
    user_input = user_input.split(" ")
    #for i in range(len(user_input)):
        #user_input[i]=user_input[i].replace('_',' ')


      
    #print(user_input)
    match(user_input[0]):

        case "mkfile":
            if len(user_input) > 1:
                title=""
                for string in user_input[1:]:
                    title += string + " "
                user_input[1]=title
                if output_filename != "USETITLE":
                    filename = output_filename
                else: 
                    filename = str(user_input[1]) + '.tex'

            print(f"Making tex file at {output_dir}")
            replacements = {
                '<TITLE>': user_input[1],
                '<AUTHOR>': author_name,
            }
            if len(user_input) > 1:
                if output_filename != "USETITLE":
                    filename = output_filename
                else: 
                    filename = str(user_input[1]) + '.tex'

            create_latex_document(base_template_path, output_dir, filename, replacements)
            return main_loop(False)

        case "change":
            #print("Change parameter command dectected")
            if len(user_input) >= 3:
                if len(user_input) > 3:
                    removeSpace=""
                    for string in user_input[2:]:
                        removeSpace += string + " "
                    user_input[2]=removeSpace
                match(user_input[1]):
                    case 'A':
                        author_name = user_input[2]
                    case 'O':
                        output_dir = user_input[2]
                    case 'F':
                        output_filename = user_input[2]
                    case 'T':
                        base_template_path=user_input[2]
                    case _:
                        print("Invalid selection!")
                        return main_loop(False)
                if output_filename != "USETITLE":
                    if (not output_filename.endswith('.tex')):
                        output_filename+= '.tex'           
                save_settings({
                'template_path' :base_template_path,
                'output_dir' :output_dir,
                'output_filename':output_filename,
                'author_name': author_name
                })
                return main_loop(True)
            if len(user_input) == 2:
                print("No value provided!")
                return main_loop(False)



        case "default":
            save_settings({
            'template_path' :'default_template.tex',
            'output_dir' :'Output folder',
            'output_filename': "USETITLE",
            'author_name': "Author"})
            return main_loop(True)

        case "exit":
            quit()



              

       
    input("No valid command dectected, press enter to continue.")
    main_loop(False)

main_loop()