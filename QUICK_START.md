# Quick Start Guide

Get up and running with Misty Simon Says in 5 minutes!

## ⚡ Fast Setup

### 1. Prerequisites Check
- [ ] Misty II Robot (powered on and connected to WiFi)
- [ ] Python 3.8+ installed
- [ ] Same WiFi network as Misty

### 2. Download Misty Python SDK
```bash
# Download from GitHub
# https://github.com/MistyCommunity/Python-SDK
# Extract to a folder, e.g., MistySDK/
```

### 3. Get Your Project Files
```bash
# Place the misty-simon-says folder in the same directory as MistySDK/
# Your structure should be:
# MistySDK/
#   ├── mistyPy/
#   └── misty-simon-says/
#       ├── misty_simon_says.py
#       ├── requirements.txt
#       └── README.md
```

### 4. Install Dependencies
```bash
cd MistySDK
pip install requests>=2.25.1
pip install websocket-client<=0.57.0
pip install yapf>=0.30.0
```

### 5. Update Robot Commands (First Time Only)
Create `update.py` in the MistySDK folder:
```python
from mistyPy.GenerateRobot import RobotGenerator
RobotGenerator("YOUR_MISTY_IP_ADDRESS")  # e.g., "192.168.1.100"
```

Run it once:
```bash
python update.py
```

### 6. Find Misty's IP Address
- Open the Misty app on your phone
- Connect to your Misty
- Note the IP address (e.g., 192.168.1.100)

### 7. Run the Game!
```bash
cd misty-simon-says
python misty_simon_says.py
```

When prompted, enter Misty's IP address, and you're ready to play!

---

## 🎮 How to Play

1. **Listen** to Misty's command
2. **Check** if she said "Simon says"
3. **Touch** the sensor ONLY if she said "Simon says"
4. **Win** by getting 5 correct commands!

### Commands You'll Hear:
- ✅ "**Simon says** touch my head front" → Touch it!
- ❌ "Touch my chin" → Don't touch!

### What the LED Colors Mean:
- 💛 **Yellow** - Giving command
- 🔵 **Cyan** - Waiting for your response
- 💚 **Green** - Correct!
- 🟠 **Orange** - Wrong (missed)
- 🔴 **Red** - Game Over!

---

## 🚨 Quick Troubleshooting

**Can't connect to Misty?**
- Check Misty is on and WiFi connected
- Verify IP address is correct
- Ensure you're on the same network

**Import errors?**
```bash
# Make sure you're in the right directory
cd MistySDK
pip install -r misty-simon-says/requirements.txt
```

**Sensors not responding?**
- Touch sensors need skin contact (capacitive)
- Bump sensors need a firm press
- Wait for cyan LED before touching

---

## 🎯 Game Rules

### Win Conditions ✅
1. "Simon says" + You touch correct sensor = +1 point
2. No "Simon says" + You don't touch = +1 point
3. Get 5 points = YOU WIN! 🎉

### Lose Conditions ❌
- Touch a sensor when she didn't say "Simon says" = GAME OVER

### Mistakes (Can Continue) ⚠️
- "Simon says" + You don't touch = No point, but game continues

---

## 📍 Sensor Locations

### Touch Sensors (Capacitive - use your finger)
```
        [HeadBack]
    [HeadLeft]👁️[HeadRight]
        [HeadFront]
         [Chin]
        [Scruff]
```

### Bump Sensors (Physical buttons on base)
```
Front:  [bfl]  [bfr]
Back:   [brl]  [brr]
```

---

## 💡 Pro Tips

1. **Listen carefully** - Misty might trick you!
2. **Don't rush** - You have 5 seconds per command
3. **Stay focused** - One wrong move = game over
4. **Practice** - Learn sensor locations before playing

---

## 🔧 Customization

Want to make it easier/harder?

**Easier (90% "Simon says" commands):**
```python
# Line 216 in misty_simon_says.py
use_simon_says = random.random() < 0.9  # Changed from 0.7
```

**Harder (50% "Simon says" commands):**
```python
# Line 216 in misty_simon_says.py
use_simon_says = random.random() < 0.5  # Changed from 0.7
```

**More time to respond:**
```python
# Line 26 in misty_simon_says.py
self.command_timeout = 10  # Changed from 5 seconds
```

**Need more points to win:**
```python
# Line 210 in misty_simon_says.py
while self.game_active and self.successful_commands < 10:  # Changed from 5
```

---

## 📚 More Resources

- **Full README**: See `README.md` for detailed documentation
- **Gameplay Example**: See `GAMEPLAY_EXAMPLE.md` for a sample game walkthrough
- **Misty Documentation**: https://docs.mistyrobotics.com/
- **Python SDK**: https://github.com/MistyCommunity/Python-SDK

---

## 🎉 You're Ready!

Have fun playing Simon Says with Misty! 🤖

Remember: Only follow commands that start with "Simon says"! 😉


