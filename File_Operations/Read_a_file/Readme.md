# 🔍 Log File Reader

This Python script reads a log file and prints all lines that contain a specific keyword (e.g., "ERROR"). The keyword is defined in a separate `parameter.py` file for easy reuse and configuration.


## 📁 File Structure

├── sample.log # Sample log file with mixed log levels
├── parameter.py # Stores the search keyword (e.g., "ERROR")
├── log_reader.py # Main script that reads and filters the log
├── README.md # Project documentation


## 🧾 parameter.py

This file defines the keyword to search for in the log file.

# parameter.py

search_key = "ERROR"

## ▶️ How to Run

python read_file.py

## 📜 License
This project is open source and free to use for educational or personal purposes.