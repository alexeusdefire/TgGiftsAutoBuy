# 💡 Auto Gifts Buyer for Telegram 💡

Bot for automatic purchase of Telegram gifts

## 😏 How bot works

📖 Every 30 seconds, the program checks for gifts in Telegram based on the criteria you specify in config.json and
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
- 1.3 Write your telegram username/id in __receiver__

#### **P.S**

**If you want to buy gifts for the channel, use the ID without -100 (for example: NOT -1002970474649, but 2970474649)**
- 1.4 ⭐If you want to buy new limited gifts - write __True__ in __limited__ ⭐
- 1.5 __Blacklist__ is list for unwanted gifts id's
- 1.6 __Hide__ this is a setting for information about the sender of the gift (__True__ if anon, __False__ to not)
- 1.7 __Cycles__ cycles is the number of purchase cycles
- 1.8 __Start__ is a start range price
- 1.9 __End__ is a end range price



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

- Just run ___main.py___ and enjoy