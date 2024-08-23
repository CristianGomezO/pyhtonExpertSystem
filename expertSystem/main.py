import tkinter as tk

def show_recommendation():
    soil = soil_entry.get()
    climate = climate_entry.get()
    recommendation.set(f'Recommendation for {soil} and {climate}')

window = tk.Tk()
window.title('Crop Advisor')

tk.Label(window, text="Soil Type:").grid(row=0)
soil_entry = tk.Entry(window)
soil_entry.grid(row=0, column=1)

tk.Label(window, text="Climate:").grid(row=1)
climate_entry = tk.Entry(window)
climate_entry.grid(row=1, column=1)

recommendation = tk.StringVar()
tk.Label(window, textvariable=recommendation).grid(row=2, columnspan=2)

tk.Button(window, text="Recommend", command=show_recommendation).grid(row=3, columnspan=2)

window.mainloop()