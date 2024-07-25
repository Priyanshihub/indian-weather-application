from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import os

def data_get():
    city = com.get()
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2db015bd7f43e255365d77b9020bb571").json()
    forecast_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=2db015bd7f43e255365d77b9020bb571").json()
  
    w_label1.config(text=weather_data["weather"][0]["main"])
    wb_label1.config(text=weather_data["weather"][0]["description"])
    temp_label1.config(text=f"{weather_data['main']['temp'] - 273.15:.2f} °C")
    per_label1.config(text=f"{weather_data['main']['pressure']} mBar")

    # Determine the image based on weather condition
    condition = weather_data["weather"][0]["main"].lower()
    img_path = os.path.join('C:\\Users\\Lenovo\\Desktop\\imageee', f'{condition}.png')
    if not os.path.isfile(img_path):
        img_path = os.path.join('C:\\Users\\Lenovo\\Desktop\\imageee', 'default.png')
        
    weather_img = ImageTk.PhotoImage(Image.open(img_path).resize((150, 150)))

    
    # Update the image label
    weather_image_label.config(image=weather_img)
    weather_image_label.image = weather_img

    # Update forecast labels
    for i in range(5):
        forecast_index = i * 8  # 3-hour forecast * 8 = 24-hour intervals
        if forecast_index < len(forecast_data['list']):
            forecast = forecast_data['list'][forecast_index]
            date = forecast['dt_txt'].split()[0]
            condition = forecast['weather'][0]['main']
            temp = f"{forecast['main']['temp'] - 273.15:.2f} °C"
            forecast_labels[i][0].config(text=date)
            forecast_labels[i][1].config(text=condition)
            forecast_labels[i][2].config(text=temp)

# Create the main window
win = Tk()
win.title("Weather App")
win.config(bg="light blue")
win.geometry("500x900")  # Adjusted the height to accommodate all labels and image

# Choose a cool font
cool_font = ("Helvetica", 15, "bold")

# Create and place the label
name_label = Label(win, text="Indian Weather App", font=("Helvetica", 30, "bold"), bg="black", fg="white")
name_label.place(x=25, y=30, height=50, width=450)

# List of state names
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
    "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
    "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
    "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]

city_name = StringVar()
# Create and place the combobox
com = ttk.Combobox(win, values=list_name, font=cool_font, textvariable=city_name)
com.place(x=25, y=100, height=50, width=300)
com.set("Uttarakhand")
# Create and place the "Done" button
done_button = Button(win, text="search", font=cool_font, command=data_get)
done_button.place(x=350, y=100, height=50, width=100)

# Create and place the weather image label
weather_image_label = Label(win)
weather_image_label.place(x=175, y=180, height=150, width=150)

# Create and place weather labels below the image
w_label = Label(win, text="Weather Climate", font=cool_font)
w_label.place(x=25, y=340, height=50, width=210)

w_label1 = Label(win, text="", font=cool_font)
w_label1.place(x=250, y=340, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=cool_font)
wb_label.place(x=25, y=410, height=50, width=210)

wb_label1 = Label(win, text="", font=cool_font)
wb_label1.place(x=250, y=410, height=50, width=210)

temp_label = Label(win, text="Temperature", font=cool_font)
temp_label.place(x=25, y=480, height=50, width=210)

temp_label1 = Label(win, text="", font=cool_font)
temp_label1.place(x=250, y=480, height=50, width=210)

per_label = Label(win, text="Pressure", font=cool_font)
per_label.place(x=25, y=550, height=50, width=210)

per_label1 = Label(win, text="", font=cool_font)
per_label1.place(x=250, y=550, height=50, width=210)

# Create and place the forecast section label
forecast_label = Label(win, text="5-Day Forecast", font=cool_font)
forecast_label.place(x=25, y=620, height=50, width=450)

# Create a canvas and scrollbar for the forecast section
canvas = Canvas(win, bg="light blue")
scrollbar = Scrollbar(win, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas, bg="light blue")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Place the canvas and scrollbar
canvas.place(x=25, y=680, width=450, height=200)
scrollbar.place(x=475, y=680, height=200)

# Create and place forecast labels inside the scrollable frame
forecast_labels = []
for i in range(5):
    forecast_date = Label(scrollable_frame, text="", font=cool_font, bg="light blue")
    forecast_date.grid(row=i, column=0, padx=10, pady=5)
    
    forecast_condition = Label(scrollable_frame, text="", font=cool_font, bg="light blue")
    forecast_condition.grid(row=i, column=1, padx=10, pady=5)
    
    forecast_temp = Label(scrollable_frame, text="", font=cool_font, bg="light blue")
    forecast_temp.grid(row=i, column=2, padx=10, pady=5)
    
    forecast_labels.append((forecast_date, forecast_condition, forecast_temp))

# Run the main loop
win.mainloop()
