from models.metrics import MetriquesSysteme
import tkinter as tk

from observers.cpu_display import AffichageCPU
from observers.disk_display import AffichageDisque
from observers.ram_display import AffichageRAM
from observers.logger import LoggerFichier 


metriques = MetriquesSysteme()
root = tk.Tk()


logger = LoggerFichier()
metriques.abonner(logger)

cpu = AffichageCPU(root)
metriques.abonner(cpu)

ram = AffichageRAM(root)
metriques.abonner(ram)

disk = AffichageDisque(root)
metriques.abonner(disk)



def rafraichir():
    metriques.actualiser_metriques()
    root.after(2000, rafraichir)

rafraichir()
root.mainloop()