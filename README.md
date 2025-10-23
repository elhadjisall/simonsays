# Misty Simon Says Game

A classic Simon Says game for the Misty II robot! Misty will give you commands like "Simon says touch my head" or just "Touch my chin". You should only follow commands that start with "Simon says"!

## How It Works

1. **Misty says "Let's play Simon Says!"** and explains the rules
2. **Misty gives commands** like "Simon says touch my head front" or "Touch my chin"
3. **Follow ONLY if she says "Simon says"** - if she doesn't, DON'T touch!
4. **If you touch when she doesn't say "Simon says"** - YOU LOSE! 
5. **Get 5 successful commands to WIN the game!**

## Features

- 👆 **Touch & Bump Sensors**: Uses Misty's capacitive touch and bump sensors
- 🤖 **Visual Feedback**: LED colors change based on game state
- 🗣️ **Voice Commands**: Misty speaks all commands clearly
- 🎯 **Classic Rules**: Only follow commands with "Simon says"
- 🎉 **Win Celebration**: Special animation when you get 5 correct!
- 🎭 **Expressive**: Misty shows emotions through her screen
- ⏱️ **Timeout System**: 5 seconds to respond to each command
- 🎲 **Random Commands**: Mix of touch and bump sensor commands

## Prerequisites

1. **Misty II Robot** - Connected to your WiFi network
2. **Python 3.8+** installed on your computer
3. **Misty Python SDK** - Download from [MistyCommunity/Python-SDK](https://github.com/MistyCommunity/Python-SDK)

## Setup Instructions

### Step 1: Download Misty Python SDK

1. Download the Misty Python SDK from: https://github.com/MistyCommunity/Python-SDK
2. Extract the ZIP file to a folder (e.g., `C:\Users\YourName\Desktop\MistySDK`)

### Step 2: Place Your Project

Copy the `misty-simon-says` folder into the same directory as the Misty SDK so your structure looks like:

```
MistySDK/
├── mistyPy/
│   ├── __init__.py
│   ├── Robot.py
│   ├── Events.py
│   ├── EventFilters.py
│   └── GenerateRobot.py
└── misty-simon-says/
    ├── misty_simon_says.py
    ├── requirements.txt
    └── README.md
```

### Step 3: Install Dependencies

Open a terminal/command prompt in the SDK directory and run:

```bash
pip install -r misty-simon-says/requirements.txt
```

Or install individually:
```bash
pip install requests>=2.25.1
pip install websocket-client<=0.57.0
pip install yapf>=0.30.0
```

### Step 4: Update Robot Commands (First Time Only)

Create a file called `update.py` in the SDK directory with:

```python
from mistyPy.GenerateRobot import RobotGenerator
RobotGenerator("YOUR_MISTY_IP_ADDRESS")
```

Run it once:
```bash
python update.py
```

This updates the SDK with your robot's available commands.

### Step 5: Find Your Misty's IP Address

1. Open the **Misty App** on your phone
2. Connect to your Misty
3. Look for the IP address (e.g., `192.168.1.100`)

## Running the Game

1. Make sure Misty is powered on and connected to WiFi
2. Navigate to the misty-simon-says directory:
   ```bash
   cd misty-simon-says
   ```
3. Run the game:
   ```bash
   python misty_simon_says.py
   ```
4. Enter Misty's IP address when prompted
5. Follow the on-screen instructions!

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

### Bump Sensors
| Sensor ID | Location | Command Example |
|-----------|----------|-----------------|
| bfr | Front right bumper | "Simon says touch my front right bumper" |
| bfl | Front left bumper | "Touch my front left bumper" |
| brr | Back right bumper | "Simon says touch my back right bumper" |
| brl | Back left bumper | "Touch my back left bumper" |

## Game Controls

- **Touch Sensors**: Use your finger to touch Misty's capacitive sensors
- **Bump Sensors**: Press the physical bump sensors on her base
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
- Bump sensors require a firm press
- Wait for the cyan LED (Misty is ready for input)

### Import Errors
- Make sure the `mistyPy` folder is in the parent directory
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that you've run the `update.py` script at least once

### Robot Not Responding
- Check network connection
- Try restarting Misty
- Verify the IP address is correct

## Customization Ideas

### Easy Modifications:
1. **Change win condition**: Modify the `5` in line 210 to require more/fewer successes
2. **Adjust response time**: Change `command_timeout` (line 26) for more/less time
3. **Change difficulty**: Modify the probability on line 216 (currently 70% chance of "Simon says")
4. **Add more sensors**: Extend the sensor dictionaries with additional sensors

### Advanced Features:
1. **Difficulty levels**: 
   - Easy: 90% "Simon says" commands
   - Medium: 70% "Simon says" commands (current)
   - Hard: 50% "Simon says" commands
2. **Time pressure mode**: Reduce timeout as game progresses
3. **High score system**: Track longest winning streaks
4. **Multiplayer mode**: Players take turns
5. **Sound effects**: Add fun sounds for correct/wrong responses
6. **Combo system**: Bonus points for consecutive correct responses

## Code Structure

```
MistySimonSays
├── __init__()            # Initialize game settings and sensor mappings
├── setup_game()          # Prepare Misty and explain rules
├── touched_callback()    # Handle touch sensor events
├── bumped_callback()     # Handle bump sensor events  
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

## Future Enhancements

- [ ] Add difficulty selection (Easy/Medium/Hard)
- [ ] Implement high score tracking system
- [ ] Add sound effects for correct/wrong responses
- [ ] Create leaderboard for multiple players
- [ ] Speed mode (faster timeout as you progress)
- [ ] Add more sensor combinations
- [ ] Display score on Misty's screen
- [ ] Add "practice mode" with no elimination
- [ ] Combo multiplier for consecutive successes
- [ ] Add voice recognition for "I give up" to quit gracefully

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

