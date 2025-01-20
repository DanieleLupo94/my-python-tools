# Calcolatore Bolletta Elettrica 🔌

Un'applicazione Python con interfaccia grafica per calcolare tariffe elettriche e consumi energetici dei dispositivi elettronici.

## Funzionalità

L'applicazione offre due funzionalità principali:

1. **Calcolo Tariffa Elettrica**
   - Calcola la tariffa per kWh partendo dall'importo della bolletta e dal consumo
   - Visualizza il risultato in €/kWh

2. **Calcolo Consumo Dispositivi**
   - Calcola il consumo energetico di un dispositivo basato su:
     - Potenza in Watt
     - Ore di utilizzo giornaliero
     - Tariffa elettrica (si aggiorna automaticamente dopo il calcolo della tariffa)
   - Mostra:
     - Consumo giornaliero in kWh
     - Costo giornaliero
     - Stima del costo mensile

## Requisiti di Sistema

### Per l'esecuzione del codice Python:
- Python 3.x
- tkinter (generalmente incluso nell'installazione standard di Python)

### Per la compilazione in eseguibile:
- PyInstaller (`pip install pyinstaller`)

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/tuoutente/calcolatore-bolletta.git
cd calcolatore-bolletta
```

2. Verifica che Python sia installato:
```bash
python --version
```

3. Verifica che tkinter sia installato aprendo Python e digitando:
```python
import tkinter
```
Se non ricevi errori, tkinter è installato correttamente.

## Utilizzo

### Esecuzione del codice Python:
```bash
python calcolatore_bolletta.py
```

### Compilazione in eseguibile Windows (EXE):

1. Installa PyInstaller se non l'hai già fatto:
```bash
pip install pyinstaller
```

2. Compila l'applicazione:
```bash
pyinstaller calcolatore_bolletta.spec
```

3. L'eseguibile verrà creato nella cartella `dist`

Nota: Se vuoi aggiungere un'icona personalizzata all'eseguibile:
1. Aggiungi il file `icon.ico` nella stessa cartella del progetto
2. Il file spec è già configurato per utilizzarla

## Come Usare l'Applicazione

1. Calcolo della tariffa:
   - Inserisci l'importo della bolletta in €
   - Inserisci il consumo in kWh
   - Clicca su "Calcola Tariffa"
   - La tariffa calcolata verrà automaticamente inserita nel campo tariffa della sezione successiva

2. Calcolo del consumo dispositivo:
   - Inserisci la potenza del dispositivo in Watt
   - Inserisci le ore di utilizzo giornaliero
   - La tariffa sarà già impostata dal calcolo precedente
   - Clicca su "Calcola Consumo"

## Note di Utilizzo

- Puoi utilizzare sia la virgola che il punto per i numeri decimali
- Tutti i campi devono contenere valori numerici maggiori di zero
- La stima mensile è calcolata su base 30 giorni

## Risoluzione Problemi

Se ricevi un errore durante l'avvio dell'applicazione:

1. Verifica che Python sia installato correttamente
2. Controlla che tkinter sia disponibile
3. Assicurati di essere nella directory corretta quando esegui il programma

Se ricevi errori durante la compilazione:
1. Assicurati che PyInstaller sia installato correttamente
2. Verifica che tutti i file necessari siano nella stessa directory
3. Controlla che il file spec sia configurato correttamente

Se ricevi un errore durante l'uso:
- Verifica che tutti i campi contengano numeri validi
- Assicurati che i valori inseriti siano maggiori di zero

## Contribuire

Sei interessato a contribuire? Ecco come puoi farlo:

1. Fai un fork del repository
2. Crea un branch per la tua modifica
3. Fai commit delle tue modifiche
4. Invia una pull request

## Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file LICENSE per maggiori dettagli.