from observers.observers import Observateur

from datetime import datetime
import psutil

class LoggerFichier(Observateur):
    def __init__(self):
          self.log_active = True
        
    def actualiser(self, sujet) -> None:

        # Appeler get.donnees
        donnees_metriques = sujet.get_donnees()
        cpu = donnees_metriques["cpu"]
        ram = donnees_metriques["ram"]
        disque = donnees_metriques["disque"]
        # Obtenir la date
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Écrire dans le fichier monitoring.log
        ligne = (
                    f"{horodatage} | "
                    f"CPU: {cpu:.1f}% | "
                    f"RAM: {ram:.1f}% | "
                    f"Disque: {disque:.1f}%\n"
                )
       
        with open("monitoring.log", 'a') as f:
             f.write(ligne)
        
        print(ligne)