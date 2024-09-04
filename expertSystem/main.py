import collections
import collections.abc
collections.Mapping = collections.abc.Mapping

import tkinter as tk
from tkinter import StringVar, OptionMenu, font
from experta import *

class CropFact(Fact):
    def __repr__(self):
        return f"Condiciones(Soil={self['soil']}, Climate={self['climate']})"

class RecommendationFact(Fact):
    def __repr__(self):
        return f"Recomendación({self['recommendation']})"

class CropExpert(KnowledgeEngine):
    
    @Rule(CropFact(soil='Arenoso', climate='Tropical'))
    def recommend_coconuts(self):
        self.declare(RecommendationFact(recommendation="Plantar cocos"))
        self.display_rule("Regla Activada: Recomendar Plantar Cocos")
    
    @Rule(CropFact(soil='Franco', climate='Templado'))
    def recommend_wheat(self):
        self.declare(RecommendationFact(recommendation="Plantar trigo"))
        self.display_rule("Regla Activada: Recomendar Plantar Trigo")
    
    @Rule(CropFact(soil='Arcilloso', climate='Seco'))
    def recommend_cactus(self):
        self.declare(RecommendationFact(recommendation="Plantar cactus o suculentas"))
        self.display_rule("Regla Activada: Recomendar Plantar Cactus o Suculentas")
    
    @Rule(CropFact(soil='Limoso', climate='Humedo'))
    def recommend_rice(self):
        self.declare(RecommendationFact(recommendation="Plantar arroz"))
        self.display_rule("Regla Activada: Recomendar Plantar Arroz")
    
    @Rule(CropFact(soil='Pedregoso', climate='Montañoso'))
    def recommend_grapes(self):
        self.declare(RecommendationFact(recommendation="Plantar uvas"))
        self.display_rule("Regla Activada: Recomendar Plantar Uvas")
    
    @Rule(RecommendationFact(recommendation=MATCH.rec))
    def show_recommendation(self, rec):
        global recommendation_text
        recommendation_text = rec

    def display_rule(self, rule_description):
        global rules_text
        rules_text.insert(tk.END, f"{rule_description}\n")

window = tk.Tk()
window.title('Asesor de Cultivos')

soil_options = ['Arenoso', 'Franco', 'Arcilloso', 'Limoso', 'Pedregoso']
climate_options = ['Tropical', 'Templado', 'Seco', 'HUmedo', 'Montañoso']

soil_var = StringVar(window)
climate_var = StringVar(window)

soil_var.set(soil_options[0])
climate_var.set(climate_options[0])

tk.Label(window, text="Tipo de Suelo:").grid(row=0)
soil_select = OptionMenu(window, soil_var, *soil_options)
soil_select.grid(row=0, column=1)

tk.Label(window, text="Clima:").grid(row=1)
climate_select = OptionMenu(window, climate_var, *climate_options)
climate_select.grid(row=1, column=1)

recommendation = StringVar()
bold_font = font.Font(window, weight="bold")
tk.Label(window, text="Recomendación:").grid(row=2)
tk.Label(window, textvariable=recommendation, font=bold_font).grid(row=2, column=1)

facts_text = tk.Text(window, height=10, width=40)
facts_text.grid(row=4, columnspan=2)

rules_text = tk.Text(window, height=5, width=40)
rules_text.grid(row=5, columnspan=2)

def run_expert_system():
    global recommendation_text
    recommendation_text = "No hay recomendación disponible."
    
    facts_text.delete('1.0', tk.END)
    rules_text.delete('1.0', tk.END)

    engine = CropExpert()
    engine.reset()

    engine.declare(CropFact(soil=soil_var.get(), climate=climate_var.get()))

    engine.run()

    recommendation.set(recommendation_text)
    
    for fact_id, fact in engine.facts.items():
        facts_text.insert(tk.END, f"Hecho {fact_id}: {fact}\n")

tk.Button(window, text="Obtener Recomendación", command=run_expert_system).grid(row=3, columnspan=2)

window.mainloop()