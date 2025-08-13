# 💡Auto Gifts Buyer for Telegram💡

## 🔌Install🔌

1. Clone repo with
```
git clone https://github.com/alexeusdefire/autobuytest.git
```
    
2. ⚙️ Open config/manager.py and do settings to your criteria ⚙️

   2.1 Go to [official telegram guide to create web apps](https://core.telegram.org/api/obtaining_api_id#:~:text=Obtaining%20api_id&text=Log%20in%20to%20your%20Telegram,one%20api_id%20connected%20to%20it.)

   2.2 In config/manager.py put your __api_id__ and __api_hash_id__ from https://my.telegram.org/apps

   2.3 Write your telegram username/id in __receiver__

   2.4 ⭐If you want to buy new limited gifts - write __True__ in __limited__ ⭐

   2.5 __Blacklist__ is list for unwanted gifts id's

   2.6 __Hide__ this is a setting for information about the sender of the gift (__True__ if anon, __False__ to not)

   2.7 __Cycles__ cycles is the number of purchase cycles

   2.8 __Start__ is a start range price

   2.9 __End__ is a end range price


3. Create and activate virtual environment

```
python -m venv .venv
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run ___main.py___


6. Input your phone number and verification code from your telegram account


## 😏 How bot works

### 📖 Every 30 seconds, the program checks for gifts in Telegram based on the criteria you specify in config.json and automatically purchases ALL gifts found that match the criteria. (if there are 2 gifts worth 300 stars and the settings specify start and end 300, it will purchase both gifts, regardless of the specified purchase cycles)
### 📘 After completing the purchase cycles, the program goes into “sleep” mode for an hour, and you will need to restart it to resume operation.
### 📕 Enjoyable use