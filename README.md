# 💡 Auto Gifts Buyer for Telegram 💡

Bot for automatic purchase of Telegram gifts

## 😏 How bot works

📖 Every 5 seconds, the program checks for gifts in Telegram based on the criteria you specify in config.json and
automatically purchases ALL gifts found that match the criteria. (if there are 2 gifts worth 300 stars and the settings
specify start and end 300, it will purchase both gifts, regardless of the specified purchase cycles)

📘 After completing the purchase cycles, the program goes into “sleep” mode for an hour, and you will need to restart 
it if you want to resume operation.

## 🍋Stack
- **Python 3.9**
- **Telethon 1.40**

## 🔌Install & Setup

### 1. ⚙️ Config your settings ⚙️
- 1.1 Go to [official telegram guide to create web apps](https://core.telegram.org/api/obtaining_api_id#:~:text=Obtaining%20api_id&text=Log%20in%20to%20your%20Telegram,one%20api_id%20connected%20to%20it.)
- 1.2 In config/manager.py put your __api_id__ and __api_hash_id__
- 1.3 Write your telegram username/id  in __receiver__



**P.S. To buy on the channel use **channel id without** the `-100` prefix.  
  *(example: use `1234567890` instead of `-1001234567890`)***

- **hide** — controls whether the sender information is shown:  
  `True` — anonymous,  
  `False` — show sender info.

- **cycles** — number of purchase cycles to run.

- **start** — minimum purchase price of a gift.

- **end** — maximum purchase price of a gift.

- **max_supply** — sets the maximum supply of gifts the bot can purchase.  
  *(the bot will only buy gifts where `supply <= max_supply`)*

- **reverse** — order of purchase by price (true if you want from expensive to cheap and false if from cheap to expensive)

### 2. Create and activate virtual environment

```bash
python -m venv venv
```
**For Windows**
```bash
venv\Scripts\activate
```
**For Linux/MacOS**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run ___main.py___

```bash
python main.py
```

### 5. Input your phone number and verification code from your telegram account or bot token

## 💰 Usage

- Just run ***main.py*** and enjoy