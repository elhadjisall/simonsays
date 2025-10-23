# Configuration Guide

## Setting Misty's IP Address for Testing

When you're ready to test with your actual robot tomorrow, you have two options:

### Option 1: Set IP in the File (Fastest for Testing) ⚡

Open `misty_simon_says.py` and change **line 22**:

```python
# Before (asks you every time):
MISTY_IP_ADDRESS = None

# After (uses your IP automatically):
MISTY_IP_ADDRESS = "192.168.1.100"  # Replace with your Misty's actual IP
```

**Benefits:**
- ✅ No need to type IP every time you run the game
- ✅ Perfect for repeated testing
- ✅ Just run `python misty_simon_says.py` and go!

---

### Option 2: Enter IP When Prompted (Default)

If `MISTY_IP_ADDRESS = None`, the program will ask you:

```
Enter Misty's IP address (or press Enter for 192.168.1.100):
```

Just type your Misty's IP and press Enter.

---

## Finding Your Misty's IP Address

1. **Open the Misty mobile app** on your phone
2. **Connect to your Misty**
3. **Look for the IP address** displayed on the connection screen
   - It will look like: `192.168.1.100` or similar
4. **Write it down** or remember it for tomorrow!

---

## Other Quick Settings

All settings are at the **top of `misty_simon_says.py`** (lines 16-28):

### Change How Many Commands to Win
```python
WIN_SCORE = 5  # Change to 3 for easier, 10 for harder
```

### Change Response Time
```python
COMMAND_TIMEOUT = 5  # Change to 10 for more time, 3 for harder
```

### Change Difficulty (How Often "Simon Says" Appears)
```python
# Current (Medium):
SIMON_SAYS_PROBABILITY = 0.7  # 70% of commands include "Simon says"

# Easy (more "Simon says"):
SIMON_SAYS_PROBABILITY = 0.9  # 90% of commands include "Simon says"

# Hard (fewer "Simon says"):
SIMON_SAYS_PROBABILITY = 0.5  # 50% of commands include "Simon says"
```

---

## Example Setup for Tomorrow

Here's what your configuration section might look like when you're ready to test:

```python
# ============================================
# CONFIGURATION - Change these settings
# ============================================

# Set your Misty's IP address here for quick testing
MISTY_IP_ADDRESS = "192.168.1.100"  # Your actual Misty IP

# Game settings
WIN_SCORE = 5  # Keep at 5 for standard game
COMMAND_TIMEOUT = 5  # 5 seconds to respond
SIMON_SAYS_PROBABILITY = 0.7  # 70% include "Simon says"

# ============================================
```

Then just run:
```bash
python misty_simon_says.py
```

And it will automatically connect to your Misty! 🤖

---

## Sensor Information (From Documentation)

Your code correctly uses these event parameters:

### Touch Sensors (Capacitive)
```python
# In touched_callback (line 103):
sensor_touched = data["message"]["sensorPosition"]

# Possible values:
# - "HeadFront"
# - "HeadLeft"
# - "HeadRight"
# - "HeadBack"
# - "Chin"
# - "Scruff"
```

### Bump Sensors
```python
# In bumped_callback (line 113):
sensor_bumped = data["message"]["sensorId"]

# Possible values:
# - "bfr" (Front Right)
# - "bfl" (Front Left)
# - "brr" (Back Right)
# - "brl" (Back Left)
```

These match the **official Misty documentation** you provided! ✓

---

## Testing Checklist for Tomorrow

- [ ] Find Misty's IP address using the mobile app
- [ ] Set `MISTY_IP_ADDRESS` in line 22 of `misty_simon_says.py`
- [ ] Make sure Misty is powered on and connected to WiFi
- [ ] Ensure your computer is on the same network as Misty
- [ ] Run `python misty_simon_says.py`
- [ ] Have fun! 🎮

---

**Pro Tip:** Start with easy settings first to make sure everything works:
```python
WIN_SCORE = 3  # Only 3 commands to win
COMMAND_TIMEOUT = 10  # 10 seconds to respond
SIMON_SAYS_PROBABILITY = 0.9  # 90% say "Simon says"
```

Once you confirm it works, you can make it harder! 😊


