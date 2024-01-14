import tkinter as tk

# Definuje funkci on_submit, která se volá při stisknutí tlačítka "Odeslat"
def on_submit():
    # Získá hodnotu z vstupního pole pro jméno a uloží ji do proměnné name
    name = name_entry.get()
    # Získá hodnotu z vstupního pole pro věk a uloží ji do proměnné age
    age = age_entry.get()
    
    # Nastaví text výsledného popisku s použitím získaných informací o jménu a věku
    result_label.config(text=f"Jméno: {name}, Věk: {age}")

# Vytvoří hlavní okno aplikace
root = tk.Tk()
# Nastaví název hlavního okna
root.title("Vstup uživatelských informací")

# Vytvoří popisek s instrukcí pro vstup jména
name_label = tk.Label(root, text="Zadejte své jméno:")
# Zobrazí popisek v okně
name_label.pack()

# Vytvoří vstupní pole pro zadání jména
name_entry = tk.Entry(root)
# Zobrazí vstupní pole v okně
name_entry.pack()

# Vytvoří popisek s instrukcí pro zadání věku
age_label = tk.Label(root, text="Zadejte svůj věk:")
# Zobrazí popisek v okně
age_label.pack()

# Vytvoří vstupní pole pro zadání věku
age_entry = tk.Entry(root)
# Zobrazí vstupní pole v okně
age_entry.pack()

# Vytvoří tlačítko s nápisem "Odeslat" a propojí ho s funkcí on_submit
submit_button = tk.Button(root, text="Odeslat", command=on_submit)
# Zobrazí tlačítko v okně
submit_button.pack()

# Vytvoří popisek pro zobrazení výsledku
result_label = tk.Label(root, text="")
# Zobrazí popisek v okně
result_label.pack()

root.mainloop()
