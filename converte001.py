import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Import for image processing

# Define color scheme
primary_color = "#007bff"  # Blue
secondary_color = "#6c757d"  # Gray
text_color = "#fff"  # White

# Define font styles
heading_font = ("Arial", 16, "bold")
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Define image path
image_path = "icon.png"  # Replace with your image path

# Initialize main window
root = tk.Tk()
root.title("Calculadora de Porcentagem do Dia")
root.geometry("450x350")  # Adjust window size as needed

# Configure window icon
if image_path:
    try:
        # Load and resize icon
        image = Image.open(image_path)
        image = image.resize((32, 32))
        photo = ImageTk.PhotoImage(image)
        root.iconphoto(True, photo)
    except FileNotFoundError:
        print(f"Erro: Arquivo de imagem não encontrado: {image_path}")

# Configure styles
style = ttk.Style()
style.configure(
    "TLabel",
    background=secondary_color,
    foreground=text_color,
    font=label_font,
    padding=10,
)
style.configure(
    "TEntry",
    background=text_color,
    foreground=primary_color,
    font=entry_font,
    padding=5,
)
style.configure(
    "TButton",
    background=primary_color,
    foreground=text_color,
    font=button_font,
    padding=10,
    relief="raised",
)

# Define main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Add application logo (optional)
if image_path:
    logo_image = ttk.Label(main_frame, image=photo)
    logo_image.pack(pady=10)

# Add time label
time_label = ttk.Label(main_frame, text="Insira o tempo no formato HH:MM", style="TLabel")
time_label.pack()

# Add time entry field
time_entry = ttk.Entry(main_frame, font=entry_font)
time_entry.pack(pady=10)

# Add calculate button
calculate_button = ttk.Button(
    main_frame, text="Calcular", command=calculate_percentage, style="TButton"
)
calculate_button.pack(pady=10)

# Add result label
result_label = ttk.Label(main_frame, text="", style="TLabel")
result_label.pack(pady=10)


def time_to_percentage(time):
    """Converts time in HH:MM format to a percentage of the day.

    Args:
        time (str): Time in HH:MM format.

    Returns:
        float: Percentage of the day as a decimal (rounded to two places),
               or None if the time format is invalid.
    """

    try:
        hours, minutes = map(int, time.split(":"))
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            total_minutes = hours * 60 + minutes
            percentage = (total_minutes / (24 * 60)) * 100
            return round(percentage, 2)
        else:
            raise ValueError
    except ValueError:
        return None


def calculate_percentage(event=None):
    """Calculates and displays the percentage of the day for the entered time.

    Handles empty input and invalid time formats.
    """

    time = time_entry.get()
    if not time:
        messagebox.showerror("Erro", "Por favor, insira o tempo.")
    else:
        percentage = time_to_percentage(time)
        if percentage is not None:
            result_label.config(
                text=f"A porcentagem do dia para o tempo {time} é: {percentage}%"
            )