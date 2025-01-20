import tkinter as tk
from tkinter import ttk, messagebox

class CalcolatoreBolletta:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatore Bolletta Elettrica")
        
        # Frame principale
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Sezione calcolo tariffa
        ttk.Label(main_frame, text="Calcolo Tariffa", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(main_frame, text="Importo bolletta (€):").grid(row=1, column=0, padx=5, pady=5)
        self.importo = ttk.Entry(main_frame)
        self.importo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Consumo (kWh):").grid(row=2, column=0, padx=5, pady=5)
        self.consumo = ttk.Entry(main_frame)
        self.consumo.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(main_frame, text="Calcola Tariffa", command=self.calcola_tariffa).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.risultato_tariffa = ttk.Label(main_frame, text="")
        self.risultato_tariffa.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Separatore
        ttk.Separator(main_frame, orient='horizontal').grid(row=5, column=0, columnspan=2, sticky='ew', pady=10)
        
        # Sezione calcolo consumo dispositivo
        ttk.Label(main_frame, text="Calcolo Consumo Dispositivo", font=('Helvetica', 10, 'bold')).grid(row=6, column=0, columnspan=2, pady=10)
        
        ttk.Label(main_frame, text="Potenza dispositivo (Watt):").grid(row=7, column=0, padx=5, pady=5)
        self.potenza = ttk.Entry(main_frame)
        self.potenza.grid(row=7, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Ore di utilizzo al giorno:").grid(row=8, column=0, padx=5, pady=5)
        self.ore = ttk.Entry(main_frame)
        self.ore.grid(row=8, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Tariffa (€/kWh):").grid(row=9, column=0, padx=5, pady=5)
        self.tariffa = ttk.Entry(main_frame)
        self.tariffa.grid(row=9, column=1, padx=5, pady=5)
        
        ttk.Button(main_frame, text="Calcola Consumo", command=self.calcola_consumo).grid(row=10, column=0, columnspan=2, pady=10)
        
        self.risultato_consumo = ttk.Label(main_frame, text="")
        self.risultato_consumo.grid(row=11, column=0, columnspan=2, pady=5)
        
        # Aggiungo un po' di padding a tutti i widget
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5)
    
    def calcola_tariffa(self):
        try:
            importo = float(self.importo.get().replace(',', '.'))
            consumo = float(self.consumo.get().replace(',', '.'))
            
            if importo <= 0 or consumo <= 0:
                raise ValueError("I valori devono essere maggiori di zero")
            
            tariffa = importo / consumo
            self.risultato_tariffa.config(
                text=f"La tariffa è di {tariffa:.3f} €/kWh"
            )
            # Imposto automaticamente la tariffa calcolata nel campo per il calcolo del consumo
            self.tariffa.delete(0, tk.END)
            self.tariffa.insert(0, f"{tariffa:.3f}")
            
        except ValueError as e:
            messagebox.showerror("Errore", "Inserisci valori numerici validi maggiori di zero")
    
    def calcola_consumo(self):
        try:
            potenza = float(self.potenza.get().replace(',', '.'))
            ore = float(self.ore.get().replace(',', '.'))
            tariffa = float(self.tariffa.get().replace(',', '.'))
            
            if potenza <= 0 or ore <= 0 or tariffa <= 0:
                raise ValueError("I valori devono essere maggiori di zero")
            
            # Calcolo kWh giornalieri
            consumo_kwh = (potenza * ore) / 1000
            # Calcolo costo giornaliero
            costo = consumo_kwh * tariffa
            
            self.risultato_consumo.config(
                text=f"Consumo giornaliero: {consumo_kwh:.2f} kWh\n"
                     f"Costo giornaliero: {costo:.2f} €\n"
                     f"Costo mensile stimato: {costo * 30:.2f} €"
            )
        except ValueError:
            messagebox.showerror("Errore", "Inserisci valori numerici validi maggiori di zero")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalcolatoreBolletta(root)
    root.mainloop()