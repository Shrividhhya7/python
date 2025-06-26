# Config File Updater

This Python program updates a configuration file (`server.conf`) using key-value pairs defined in a separate Python module (`parameter.py`). It searches for each key in the config file and updates its value. If a key does not exist, it appends the key-value pair at the end of the file.


## 📁 File Structure


├── server.conf # Target configuration file to update
├── parameter.py # Python file containing key-value parameters
├── update_config.py # Main script to apply the updates
├── README.md # This documentation file


## ✅ How to Run

python update_file.py


## 📜 License
This project is open source and free to use for educational or personal purposes.