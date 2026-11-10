import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for bib in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(bib.nome))

        generi = self._model.get_generi()
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for gen in generi:
            if gen:
                self._view.dd_genere.options.append(ft.dropdown.Option(gen))

        self._view.update()

    # CALLBACKS DROPDOWN
    def leggi_biblioteca(self, e):
        self.biblioteca_selezionata = e.control.value

    def leggi_genere(self, e):
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        self._view.list_view_libri.controls.clear()
        bib = self.biblioteca_selezionata if self.biblioteca_selezionata else "Nessun filtro"
        gen = self.genere_selezionato if self.genere_selezionato else "Nessun filtro"

        libri = self._model.get_libri_filtrati(bib, gen)

        if not libri:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio indicati!")
        else:
            for libro in libri:
                self._view.list_view_libri.controls.append(
                    ft.Text(f"[{libro.id}] {libro.titolo} - {libro.autore} ({libro.genere}) - Anno: {libro.anno}")
                )

        self._view.update()
