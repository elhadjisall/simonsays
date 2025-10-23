# Misty Simon Says Game

A classic Simon Says game for the Misty II robot! Misty will give you commands like "Simon says touch my head" or just "Touch my chin". You should only follow commands that start with "Simon says"!

## Quick Start

Want to play right now? Follow these steps:

### 1. Clone the Repository
```bash
git clone git@github.com:elhadjisall/simonsays.git
cd simonsays
```

### 2. Install Misty SDK
```bash
pip install git+https://github.com/MistyCommunity/Python-SDK.git
```

### 3. Install Game Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your Misty's IP Address

**First, find your Misty's IP:**
- Open the Misty App on your phone
- Connect to your Misty
- Note the IP address shown (e.g., 192.168.1.100)

**Then set it in both files:**

1. Open `update.py` and edit line 20:
```python
ROBOT_IP_ADDRESS = "YOUR_MISTY_IP"  # e.g., "192.168.1.100"
```

2. Open `misty_simon_says.py` and edit line 22:
```python
MISTY_IP_ADDRESS = "YOUR_MISTY_IP"  # Use the same IP as above
```

### 5. Update SDK (First Time Only)
Run this once to update the SDK with your robot's API endpoints:
```bash
python update.py
```

You only need to do this the first time you set up the game.

### 6. Run the Game!
```bash
python misty_simon_says.py
```

That's it! Misty will start explaining the rules and the game begins! 🎮

---

## How It Works

1. **Misty says "Let's play Simon Says!"** and explains the rules
2. **Misty gives commands** like "Simon says touch my head front" or "Touch my chin"
3. **Follow ONLY if she says "Simon says"** - if she doesn't, DON'T touch!
4. **If you touch when she doesn't say "Simon says"** - YOU LOSE! 
5. **Get 5 successful commands to WIN the game!**

## Features

- 👆 **Touch Sensors**: Uses Misty's capacitive touch sensors
- 🤖 **Visual Feedback**: LED colors change based on game state
- 🗣️ **Voice Commands**: Misty speaks all commands clearly
- 🎯 **Classic Rules**: Only follow commands with "Simon says"
- 🎉 **Win Celebration**: Special animation when you get 5 correct!
- 🎭 **Expressive**: Misty shows emotions through her screen
- ⏱️ **Timeout System**: 5 seconds to respond to each command
- 🎲 **Random Commands**: Variety of touch sensor commands

## Prerequisites

1. **Misty II Robot** - Connected to your WiFi network
2. **Python 3.8+** installed on your computer
3. **pip** (Python package manager) - Usually comes with Python

## Setup Instructions

### Step 1: Install Misty Python SDK

Install the Misty Python SDK directly from GitHub:

```bash
pip install git+https://github.com/MistyCommunity/Python-SDK.git
```

Or if you've already downloaded it locally:
```bash
cd Python-SDK
pip install -e .
```

### Step 2: Install Game Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- requests>=2.25.1
- websocket-client<=0.57.0
- yapf>=0.30.0

### Step 3: Find Your Misty's IP Address

1. Open the **Misty App** on your phone
2. Connect to your Misty
3. Look for the IP address (e.g., `192.168.1.100`)

## Running the Game

1. Make sure Misty is powered on and connected to WiFi
2. Run the game:
   ```bash
   python misty_simon_says.py
   ```
3. Enter Misty's IP address when prompted (or set it in the code on line 22)
4. Follow the on-screen instructions and have fun!

## How to Play

1. **Listen Carefully**: Misty will give you a command
2. **Check for "Simon Says"**: Did she say "Simon says" before the command?
3. **Follow or Don't**: 
   - ✅ If she said "Simon says" → Touch the sensor she mentioned
   - ❌ If she didn't say "Simon says" → DON'T touch anything!
4. **Win Condition**: Successfully complete 5 "Simon says" commands
5. **Lose Condition**: Touch a sensor when she didn't say "Simon says"

## Sensors Used

### Touch Sensors (Capacitive)
| Sensor ID | Location | Command Example |
|-----------|----------|-----------------|
| HeadFront | Front of head | "Simon says touch my head front" |
| HeadLeft  | Left side of head | "Touch my head left" |
| HeadRight | Right side of head | "Simon says touch my head right" |
| HeadBack  | Back of head | "Touch my head back" |
| Chin      | Under the head | "Simon says touch my chin" |
| Scruff    | Back of neck | "Touch my scruff" |

## Game Controls

- **Touch Sensors**: Use your finger to touch Misty's capacitive sensors
- **Quit Game**: Press `Ctrl+C` at any time

## LED Color Guide

| Color | Meaning |
|-------|---------|
| White | Neutral/Ready |
| Yellow | Giving command |
| Cyan | Waiting for response |
| Green | Correct! |
| Orange | Wrong (missed command) |
| Red | Game Over (touched without "Simon says") |

## Troubleshooting

### Connection Issues
- Ensure Misty is powered on and connected to WiFi
- Verify you're using the correct IP address
- Check that your computer is on the same network as Misty

### Sensor Detection Issues
- Make sure you're touching the correct sensor that Misty mentions
- Touch sensors require skin contact (capacitive)
- Wait for the cyan LED (Misty is ready for input)

### Import Errors
- Make sure the Misty SDK is installed: `pip install git+https://github.com/MistyCommunity/Python-SDK.git`
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Try reinstalling: `pip uninstall Misty-SDK` then reinstall

### Robot Not Responding
- Check network connection
- Try restarting Misty
- Verify the IP address is correct

## Code Structure

```
MistySimonSays
├── __init__()            # Initialize game settings and sensor mappings
├── setup_game()          # Prepare Misty and explain rules
├── touched_callback()    # Handle touch sensor events
├── give_command()        # Generate and speak a command
├── wait_for_response()   # Wait for player to touch (or not)
├── check_response()      # Verify if player was correct
├── play_game()           # Main game loop with event registration
├── handle_victory()      # Celebrate winning (5 correct)
├── handle_game_over()    # Handle losing
└── end_game()            # Cleanup and reset Misty
```

## Game Logic

The game follows these rules:

1. **Command Types**:
   - 70% chance: "Simon says touch [sensor]" (player SHOULD touch)
   - 30% chance: "Touch [sensor]" (player should NOT touch)

2. **Success Conditions**:
   - "Simon says" + player touches correct sensor = SUCCESS ✓
   - No "Simon says" + player doesn't touch = SUCCESS ✓

3. **Failure Conditions**:
   - "Simon says" + player doesn't touch = MISTAKE (can continue)
   - No "Simon says" + player touches = GAME OVER ✗

4. **Win**: 5 successful commands
5. **Lose**: Touch when "Simon says" wasn't used

## License

This project is open source and available for educational purposes.

## Credits

Built using the Misty II Robot and the [Misty Python SDK](https://github.com/MistyCommunity/Python-SDK).

## Support

For issues with:
- **This game**: Check the troubleshooting section above
- **Misty Python SDK**: Visit https://github.com/MistyCommunity/Python-SDK
- **Misty Robot**: Visit https://docs.mistyrobotics.com/

---

**Happy Playing! 🤖🎮**

