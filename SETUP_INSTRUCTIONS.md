# Complete Setup Instructions

Follow these steps to set up and run Misty Simon Says on your actual robot.

## 📋 Prerequisites

Before you begin, make sure you have:

- ✅ Misty II Robot (powered on and connected to WiFi)
- ✅ Python 3.8 or higher installed
- ✅ Misty Python SDK downloaded from [GitHub](https://github.com/MistyCommunity/Python-SDK)
- ✅ Your computer on the same WiFi network as Misty

---

## 🚀 Step-by-Step Setup

### Step 1: Download and Extract Misty Python SDK

1. Go to: https://github.com/MistyCommunity/Python-SDK
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file to a location (e.g., `Desktop/MistySDK/`)

Your folder structure should look like:
```
MistySDK/
├── mistyPy/
│   ├── __init__.py
│   ├── Robot.py
│   ├── Events.py
│   ├── EventFilters.py
│   └── GenerateRobot.py
├── Examples/
└── other files...
```

---

### Step 2: Place Your Simon Says Project

Copy or move the `misty-simon-says` folder **into the same directory** as the SDK:

```
MistySDK/
├── mistyPy/          ← SDK folder
└── misty-simon-says/ ← Your game folder
    ├── misty_simon_says.py
    ├── update.py
    ├── requirements.txt
    └── README.md
```

---

### Step 3: Install Python Dependencies

Open a terminal/command prompt and navigate to the SDK directory:

```bash
cd Desktop/MistySDK  # Or wherever you extracted the SDK
```

Install the required packages:

```bash
pip install requests>=2.25.1
pip install websocket-client<=0.57.0
pip install yapf>=0.30.0
```

Or use the requirements file:

```bash
pip install -r misty-simon-says/requirements.txt
```

---

### Step 4: Find Your Misty's IP Address

1. **Open the Misty mobile app** on your phone
2. **Connect to your Misty**
3. **Look for the IP address** - it will look like:
   - `192.168.1.100`
   - `192.168.0.50`
   - `10.0.0.25`
   - etc.
4. **Write it down!** You'll need it for the next steps.

---

### Step 5: Update the SDK (FIRST TIME ONLY)

This step tells the SDK about your specific Misty's API endpoints.

1. **Open the `update.py` file** (in the `misty-simon-says` folder)

2. **Change line 18** to your Misty's IP:
   ```python
   ROBOT_IP_ADDRESS = "192.168.1.100"  # Put your actual IP here
   ```

3. **Save the file**

4. **Run the update script:**
   ```bash
   cd misty-simon-says
   python update.py
   ```

5. **You should see:**
   ```
   ==================================================
   UPDATING MISTY PYTHON SDK
   ==================================================
   
   Connecting to Misty at: 192.168.1.100
   This will update the SDK with your robot's API endpoints...
   
   ==================================================
   ✓ SUCCESS! SDK Updated Successfully
   ==================================================
   ```

**Note:** You only need to run `update.py` once (or when you switch to a different Misty robot).

---

### Step 6: Configure the Game

Open `misty_simon_says.py` and set your IP address at **line 22**:

```python
# Before:
MISTY_IP_ADDRESS = None

# After:
MISTY_IP_ADDRESS = "192.168.1.100"  # Your Misty's IP
```

This way you won't have to type the IP every time you run the game.

**Optional:** Adjust game difficulty (lines 25-28):
```python
WIN_SCORE = 5                    # Commands needed to win
COMMAND_TIMEOUT = 5              # Seconds to respond
SIMON_SAYS_PROBABILITY = 0.7     # How often "Simon says" appears (0.7 = 70%)
```

---

### Step 7: Run the Game! 🎮

```bash
python misty_simon_says.py
```

You should see:

```
==================================================
MISTY SIMON SAYS - CLASSIC VERSION
==================================================

How to play:
1. Misty will give you commands
2. Only follow commands that start with 'Simon says'
3. If she doesn't say 'Simon says', DON'T touch!
4. Get 5 correct to win!
==================================================

Using configured IP address: 192.168.1.100
Connecting to Misty at 192.168.1.100...
```

Misty will then speak and the game will begin!

---

## 🎯 How to Play

### The Rules:
1. **Listen** to Misty's commands
2. **Only touch** if she says "Simon says" first
3. **Don't touch** if she doesn't say "Simon says"
4. **Win** by getting 5 correct responses

### Example Commands:

| Misty Says | What You Should Do |
|------------|-------------------|
| "**Simon says** touch my head front" | ✅ Touch the head front sensor |
| "Touch my chin" | ❌ DON'T touch anything! |
| "**Simon says** touch my front left bumper" | ✅ Press the front left bumper |
| "Touch my scruff" | ❌ DON'T touch anything! |

### LED Colors:

| Color | Meaning |
|-------|---------|
| 💛 Yellow | Misty is giving a command |
| 🔵 Cyan | Waiting for your response (5 seconds) |
| 💚 Green | Correct! |
| 🟠 Orange | Wrong (missed a command) |
| 🔴 Red | Game Over (you touched without "Simon says") |

---

## 📍 Sensor Locations

### Touch Sensors (Capacitive - use your finger)

```
         [HeadBack]
            ↓
    [HeadLeft] 👁️ [HeadRight]
         ↓
    [HeadFront]
         ↓
      [Chin]
         ↓
     [Scruff]
```

### Bump Sensors (Physical buttons on base)

```
      FRONT
  [bfl]  [bfr]
     🤖
  [brl]  [brr]
      BACK
```

---

## 🐛 Troubleshooting

### "Cannot connect to Misty"
- ✓ Check Misty is powered on (green light on back)
- ✓ Verify WiFi connection (check in Misty app)
- ✓ Confirm IP address is correct
- ✓ Make sure your computer is on the same network

### "ImportError: No module named mistyPy"
- ✓ Make sure you're running the script from the correct directory
- ✓ Verify `mistyPy` folder is in the parent directory
- ✓ Check your folder structure matches Step 2

### "ModuleNotFoundError: No module named 'requests'"
- ✓ Install dependencies: `pip install -r requirements.txt`

### Sensors not responding
- ✓ Touch sensors need **skin contact** (capacitive)
- ✓ Bump sensors need a **firm press**
- ✓ Wait for the **cyan LED** before touching
- ✓ Make sure you're touching the **correct sensor** Misty mentioned

### "update.py" fails to connect
- ✓ Verify Misty is on and connected to WiFi
- ✓ Double-check the IP address in `update.py`
- ✓ Try pinging Misty: `ping 192.168.1.100` (use your IP)
- ✓ Make sure `mistyPy` folder exists in parent directory

---

## 🎮 Quick Test

Once everything is set up, here's a quick test sequence:

1. **Run the game:**
   ```bash
   python misty_simon_says.py
   ```

2. **Misty should:**
   - Say "Hello! Let's play Simon Says!"
   - Explain the rules
   - Give you a command

3. **Touch a sensor** when she says "Simon says"

4. **Don't touch** when she doesn't say "Simon says"

5. **Watch the LED colors** change as you play

If all of this works, you're good to go! 🎉

---

## 📚 Additional Resources

- **CONFIG_EXAMPLE.md** - Detailed configuration guide
- **QUICK_START.md** - Fast 5-minute setup
- **GAMEPLAY_EXAMPLE.md** - See what a full game looks like
- **README.md** - Complete documentation

---

## ✅ Final Checklist

Before testing tomorrow:

- [ ] Misty Python SDK downloaded and extracted
- [ ] `misty-simon-says` folder placed in SDK directory
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Misty's IP address found (using mobile app)
- [ ] `update.py` configured with IP and run successfully
- [ ] `misty_simon_says.py` configured with IP (line 22)
- [ ] Misty is powered on and connected to WiFi
- [ ] Computer is on same network as Misty

---

## 🎉 You're Ready!

Run this command and have fun:

```bash
python misty_simon_says.py
```

**Remember:** Only touch when Misty says "Simon says"! 😊🤖

---

**Need help?** Check the troubleshooting section above or review the documentation files.

Good luck and enjoy playing Simon Says with Misty! 🎮


