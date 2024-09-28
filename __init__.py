from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

HUH = os.getenv("HUH")

print(HUH)
