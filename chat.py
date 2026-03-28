import requests
import datetime
import random
import ollama
print("🤖 Chatbot Ready! (Type 'bye' to exit)\n")

#jokes list
jokes = [
    "Why don’t programmers like nature? It has too many bugs! 😂",
    "Python developers don’t wear glasses… because they can C#. 😄",
    "I told my computer I needed a break… now it won’t stop sending me KitKat ads. 🤣"
]
#model generation
def llm_reply(query):
    response = ollama.generate(model="gemma3:4b", prompt=query)
    return response["response"]

#weather function
def get_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        return "City nahi mili!"

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    data = requests.get(weather_url).json()
    w = data.get("current_weather", {})

    if not w:
        return " Weather fetch nahi hua."

    return (
        f"🌤 Weather in {city.title()}:\n"
        f"🌡 Temp: {w['temperature']}°C\n"
        f"💨 Wind: {w['windspeed']} km/h"
    )
#conditional statements for chatbot
while True:
    msg = input("You: ").lower()

    if msg in ["hi", "hello", "hey"]:
        print("Bot:", llm_reply("Greet the user in english"))
    
    elif msg == "bye":
        print("Bot: Bye! Apna dhyaan rakhna 😊")
        break

    elif "name" in msg:
        print("Bot:", llm_reply("Tell your name creatively in english"))
    
    elif "time" in msg:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Time:", now)

    elif "date" in msg:
        print("Bot: Aaj ki date:", datetime.date.today())

    elif "joke" in msg:
        print("Bot:", random.choice(jokes))

    elif "weather" in msg:
        print("Bot: Kaun si city ka weather chahiye?")
        city = input("You (city): ")
        print("Bot:", get_weather(city))

    else:
        print("Bot:", llm_reply(msg))