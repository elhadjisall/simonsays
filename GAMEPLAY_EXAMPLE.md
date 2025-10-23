# Example Gameplay

Here's what a typical game looks like:

## Game Start

```
==================================================
MISTY SIMON SAYS - CLASSIC VERSION
==================================================

Rules:
- Only follow commands that start with 'Simon says'
- If Misty doesn't say 'Simon says', DON'T touch!
- Get 5 successful commands to win!
==================================================

Connecting to Misty at 192.168.1.100...
Setting up Misty Simon Says...
Misty is ready to play!
Registering sensor events...
Events registered successfully!
```

**Misty says:** "Hello! Let's play Simon Says!"
**Misty says:** "Only touch the sensor when I say Simon says first!"
**Misty says:** "If I don't say Simon says, don't touch anything!"
**Misty says:** "Get 5 correct commands to win! Let's begin!"

---

## Round 1

```
==================================================
Score: 0/5 successful commands
==================================================
```

**Misty's LED:** Turns yellow 💛
**Misty says:** "Simon says touch my head front"
**Misty's LED:** Turns cyan 🔵 (waiting for input)

*Player touches the HeadFront sensor*

**Misty's LED:** Turns green 💚
**Misty says:** "Great job! That's correct!"

```
✓ Correct! You followed Simon!
```

---

## Round 2

```
==================================================
Score: 1/5 successful commands
==================================================
```

**Misty's LED:** Turns yellow 💛
**Misty says:** "Touch my chin"  *(No "Simon says"!)*
**Misty's LED:** Turns cyan 🔵 (waiting for input)

*Player doesn't touch anything*

**Misty's LED:** Turns green 💚
**Misty says:** "Excellent! You didn't fall for my trick!"

```
✓ Correct! You didn't fall for the trick!
```

---

## Round 3

```
==================================================
Score: 2/5 successful commands
==================================================
```

**Misty's LED:** Turns yellow 💛
**Misty says:** "Simon says touch my front left bumper"
**Misty's LED:** Turns cyan 🔵 (waiting for input)

*Player presses the front left bump sensor*

**Misty's LED:** Turns green 💚
**Misty says:** "Great job! That's correct!"

```
✓ Correct! You followed Simon!
```

---

## Round 4 (WRONG - Missing Command)

```
==================================================
Score: 3/5 successful commands
==================================================
```

**Misty's LED:** Turns yellow 💛
**Misty says:** "Simon says touch my scruff"
**Misty's LED:** Turns cyan 🔵 (waiting for input)

*Player doesn't respond within 5 seconds*

**Misty's LED:** Turns orange 🟠
**Misty says:** "Oops! Simon said to touch, but you didn't!"

```
✗ Wrong! Simon said to touch, but you didn't!
```

---

## Example: Game Over (Touched Without "Simon Says")

```
==================================================
Score: 2/5 successful commands
==================================================
```

**Misty's LED:** Turns yellow 💛
**Misty says:** "Touch my head right"  *(No "Simon says"!)*
**Misty's LED:** Turns cyan 🔵 (waiting for input)

*Player accidentally touches the HeadRight sensor*

**Misty's LED:** Turns RED 🔴
**Misty says:** "Oh no! I didn't say Simon says! You're out!"

```
✗ YOU LOSE! I didn't say Simon says!

==================================================
GAME OVER - Score: 2/5
==================================================

FINAL SCORE: 2/5
==================================================
```

**Misty says:** "Good effort! You got 2 correct. Practice makes perfect!"
**Misty says:** "Thanks for playing Simon Says with me!"

---

## Example: Victory (5 Correct)

If you successfully complete 5 commands:

```
==================================================
🎉 CONGRATULATIONS! YOU WIN! 🎉
==================================================
```

**Misty's LED:** Flashes green 💚 and yellow 💛
**Misty's arms:** Wave up and down
**Misty says:** "Congratulations! You won Simon Says! You're amazing!"

```
FINAL SCORE: 5/5
==================================================
```

**Misty says:** "Thanks for playing Simon Says with me!"

---

## Game Scenarios

### Scenario 1: Success ✅
- **Command:** "Simon says touch my chin"
- **Player action:** Touches chin
- **Result:** ✓ Correct! (+1 point)

### Scenario 2: Success ✅
- **Command:** "Touch my head back" (no "Simon says")
- **Player action:** Doesn't touch
- **Result:** ✓ Correct! (+1 point)

### Scenario 3: Mistake (Can Continue) ⚠️
- **Command:** "Simon says touch my front right bumper"
- **Player action:** Doesn't touch (timeout)
- **Result:** ✗ Wrong, but game continues (no point)

### Scenario 4: Game Over ❌
- **Command:** "Touch my head left" (no "Simon says")
- **Player action:** Touches head left
- **Result:** ✗ GAME OVER! (eliminated)

---

## Tips for Playing

1. **Listen carefully** - Pay attention to every word Misty says
2. **Wait for the cyan LED** - This means she's ready for your response
3. **Don't rush** - You have 5 seconds to respond
4. **Stay calm** - Don't let Misty trick you!
5. **Know your sensors** - Familiarize yourself with sensor locations before playing

## Common Mistakes

❌ **Touching too quickly** - Make sure she said "Simon says"
❌ **Wrong sensor** - Touch the exact sensor she mentioned
❌ **Timeout** - Respond within 5 seconds
❌ **Accidental touch** - Be careful not to bump sensors accidentally

---

Have fun playing! 🤖🎮

