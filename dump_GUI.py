import tkinter as tk

# Исходные параметры
max_water_level = 260
critical_water_level = 240
dam_height = 262
land_len = 50
max_speed = 10

water_level = 0
electricity_generated = 0
landslide_speed = 0
landslide_distance = 0
wave = 0

o_dam_h = 250
o_wat_lev = 0
o_elec = 0

first_time = True
first_time_message = "Ввести"

def update_game():
    global water_level, electricity_generated, landslide_distance, o_wat_lev, o_elec, wave, first_time, first_time_message
    water_increase = int(water_increase_entry.get())
    water_level += water_increase

    electricity_generated += water_level

    message = ""

    if water_level > critical_water_level:
        message += f"\nТРЕВОГА! Из-за повышенного уровня воды с горы начал сходить оползень\n" \
                   f"По подсчетам критический уровень воды = {critical_water_level}\n" \
                   f"Размер оползня = {land_len}" \
                   f"Сбросьте уровень ниже этого значения что-бы остановить оползень\n" \
                   f"Если оползень упадёт в воду, то спровоцирует мини-цунами"

        landslide_speed = min(water_level - critical_water_level, max_speed) + 1
        landslide_distance += landslide_speed - 1
        land_to_water = (critical_water_level + 60) - landslide_distance - water_level
        message += f"\nСкорость оползня = {landslide_speed}, пройденное расстояние = {landslide_distance}\n" \
                   f"Расстояние до воды = {land_to_water}"

        if land_to_water <= 0:
            wave = water_level + land_len
            kills = wave*2//3*4
            if wave > dam_height:
                message =f"Оползень упал в воду" \
                        f"Волна высотой {wave} разрушила дамбу и уничтожило поселение за ней, погибло {kills} ч"
            else:
                message ="Оползень упал в воду" \
                        f"Волна высотой {wave} ударилась об дамбу и сломала всё оборудование, но его можно починить"

    status_label.config(text=message, fg="red" if message else "black")

    if o_wat_lev < o_dam_h:
        o_wat_lev += 5
    o_elec += o_wat_lev

    water_level_label.config(text=f"Уровень воды: {water_level}, Выработано электроэнергии: {electricity_generated}")
    opponent_label.config(
        text=f"Уровень воды противника - {o_wat_lev}, Выработано электроэнергии противником : {o_elec}")

    start_button.config(text=first_time_message)

def on_enter_key(event):
    if event.keysym == "Return":
        start_game()

def start_game():
    update_game()


window = tk.Tk()
window.title("Плотина Вайонт sim.")

water_increase_label = tk.Label(window, text="Введите, на сколько изменить уровень воды (От -10 до 10):")
water_increase_label.pack()

water_increase_entry = tk.Entry(window)
water_increase_entry.pack()

start_button = tk.Button(window, text="Начать игру", command=start_game)
start_button.pack()

water_level_label = tk.Label(window,
                             text=f"Уровень воды: {water_level}, Выработано электроэнергии: {electricity_generated}")
water_level_label.pack()

opponent_label = tk.Label(window,
                          text=f"Уровень воды противника - {o_wat_lev}, Выработано электроэнергии противником : {o_elec}")
opponent_label.pack()

status_label = tk.Label(window, text="", fg="black")
status_label.pack()

water_increase_entry.bind("<Key>", on_enter_key)

window.mainloop()
