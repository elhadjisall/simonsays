"""
Misty Simon Says Game

A classic Simon Says game where Misty gives commands like "Simon says touch this sensor".
Players should only follow commands that start with "Simon says". 
If they follow a command without "Simon says", they lose!
Win by successfully completing 5 "Simon says" commands.
"""

from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time
import random


# ============================================
# CONFIGURATION - Change these settings
# ============================================

# Set your Misty's IP address here for quick testing
# Leave as None to be prompted each time you run the game
MISTY_IP_ADDRESS = "142.207.50.202"  # Example: "192.168.1.100"

# Game settings
WIN_SCORE = 5  # Number of successful commands needed to win
COMMAND_TIMEOUT = 10  # Seconds player has to respond
SIMON_SAYS_PROBABILITY = 0.7  # Probability that command includes "Simon says" (0.0-1.0)
                                # 0.7 = 70% chance, 0.9 = 90% chance (easier), 0.5 = 50% chance (harder)

# ============================================


class MistySimonSays:
    def __init__(self, robot_ip):
        """Initialize the Misty Simon Says game."""
        self.misty = Robot(robot_ip)
        self.successful_commands = 0  # Track successful completions
        self.game_active = False
        self.waiting_for_touch = False
        self.should_touch = False  # True if "Simon says" was used
        self.player_touched = False
        self.current_sensor = None
        self.command_timeout = COMMAND_TIMEOUT  # seconds to respond
        
        # Define available sensors for commands (Touch sensors only)
        self.touch_sensors = {
            'HeadFront': 'head front',
            'HeadLeft': 'head left', 
            'HeadRight': 'head right',
            'HeadBack': 'head back',
            'Chin': 'chin',
            'Scruff': 'scruff'
        }
        
        # Use only touch sensors
        self.all_sensors = self.touch_sensors
        
    def setup_game(self):
        """Set up Misty for the game."""
        print("\n" + "="*50)
        print("MISTY SIMON SAYS - TOUCH SENSORS ONLY")
        print("="*50)
        print("\nRules:")
        print("- Only follow commands that start with 'Simon says'")
        print("- If Misty doesn't say 'Simon says', DON'T touch!")
        print("- Use TOUCH SENSORS only (Head, Chin, Scruff)")
        print("- Get 5 successful commands to win!")
        print("="*50 + "\n")
        
        # Reset Misty's position
        self.misty.halt()
        self.misty.move_head(0, 0, 0, velocity=100)
        self.misty.move_arms(70, 70)
        self.misty.change_led(255, 255, 255)  # White LED
        
        # Set volume to maximum
        self.misty.set_default_volume(100)
        print("Volume set to maximum (100)")
        
        time.sleep(1)
        
        # Welcome message
        self.misty.display_image("e_Joy.jpg", 1)
        self.misty.speak("Hello! Let's play Simon Says!", flush=True)
        time.sleep(2)
        
        self.misty.speak("Only touch the sensor when I say Simon says first!", flush=True)
        time.sleep(3)
        
        self.misty.speak("If I don't say Simon says, don't touch anything!", flush=True)
        time.sleep(3)
        
        self.misty.speak(f"Get {WIN_SCORE} correct commands to win! Let's begin!", flush=True)
        time.sleep(2)
        
        print("Misty is ready to play!")
        
    def touched_callback(self, data):
        """Callback when a touch sensor is triggered."""
        try:
            print(f"🔔 Touch event received! Raw data: {data}")
            
            # Try multiple ways to get the sensor position
            sensor_touched = None
            
            if isinstance(data, dict):
                if "message" in data:
                    if isinstance(data["message"], dict) and "sensorPosition" in data["message"]:
                        sensor_touched = data["message"]["sensorPosition"]
                    elif isinstance(data["message"], str):
                        sensor_touched = data["message"]
                elif "sensorPosition" in data:
                    sensor_touched = data["sensorPosition"]
            
            if not sensor_touched:
                print(f"⚠️ Could not find sensor position in data")
                return
            
            print(f"👆 Touch detected: {sensor_touched}")
            
            # Check if correct sensor was touched
            if sensor_touched == self.current_sensor:
                self.player_touched = True
                print(f"✅ Correct sensor touched!")
                # Instantly respond with "Good!" and joy face
                if self.waiting_for_touch and self.should_touch:
                    self.misty.change_led(0, 255, 0)  # Green LED
                    self.misty.display_image("e_Joy.jpg", 1)  # Happy face instantly!
                    self.misty.speak("Good!", flush=False)
            else:
                print(f"ℹ️ Wrong sensor touched. Expected: {self.current_sensor}, Got: {sensor_touched}")
                
        except Exception as e:
            print(f"❌ Error in touch callback: {e}")
            import traceback
            traceback.print_exc()
                
    def give_command(self, use_simon_says):
        """Give a command to the player."""
        # Choose a random sensor
        sensor_id = random.choice(list(self.all_sensors.keys()))
        sensor_name = self.all_sensors[sensor_id]
        
        self.current_sensor = sensor_id
        self.should_touch = use_simon_says
        self.player_touched = False
        
        # Create the command
        if use_simon_says:
            command = f"Simon says touch my {sensor_name}"
            print(f"\n✓ SIMON SAYS: Touch {sensor_name}")
        else:
            command = f"Touch my {sensor_name}"
            print(f"\n✗ NO SIMON SAYS: Touch {sensor_name} (DON'T DO IT!)")
        
        # Misty speaks the command
        self.misty.change_led(255, 255, 0)  # Yellow while giving command
        self.misty.display_image("e_ContentLeft.jpg", 1)
        self.misty.speak(command, flush=True)
        time.sleep(1)
        
    def wait_for_response(self):
        """Wait for player to respond (or not respond)."""
        self.waiting_for_touch = True
        self.misty.change_led(0, 255, 255)  # Cyan while waiting
        
        print(f"Waiting for response... (timeout in {self.command_timeout} seconds)")
        
        # Wait for timeout period
        start_time = time.time()
        while (time.time() - start_time) < self.command_timeout:
            time.sleep(0.1)
            if self.player_touched:
                break
                
        self.waiting_for_touch = False
        
    def check_response(self):
        """Check if the player's response was correct."""
        # Case 1: Simon says touch, and player touched
        if self.should_touch and self.player_touched:
            print("✓ Correct! You followed Simon!")
            self.misty.change_led(0, 255, 0)  # Green for success
            self.misty.display_image("e_Joy.jpg", 1)  # Happy face!
            self.misty.speak("Great job! That's correct!", flush=True)
            self.successful_commands += 1
            time.sleep(2)
            return True
            
        # Case 2: Simon says touch, but player didn't touch
        elif self.should_touch and not self.player_touched:
            print("✗ Wrong! Simon said to touch, but you didn't!")
            self.misty.change_led(255, 165, 0)  # Orange for wrong
            self.misty.display_image("e_Sadness.jpg", 1)  # Sad face
            self.misty.speak("Oops! Simon said to touch, but you didn't!", flush=True)
            time.sleep(2)
            return False
            
        # Case 3: No Simon says, and player didn't touch
        elif not self.should_touch and not self.player_touched:
            print("✓ Correct! You didn't fall for the trick!")
            self.misty.change_led(0, 255, 0)  # Green for success
            self.misty.display_image("e_Joy.jpg", 1)
            self.misty.speak("Excellent! You didn't fall for my trick!", flush=True)
            self.successful_commands += 1
            time.sleep(2)
            return True
            
        # Case 4: No Simon says, but player touched (GAME OVER!)
        elif not self.should_touch and self.player_touched:
            print("✗ YOU LOSE! I didn't say Simon says!")
            self.misty.change_led(255, 0, 0)  # Red for game over
            self.misty.display_image("e_Sadness.jpg", 1)  # Sad face for losing
            self.misty.speak("Oh no! I didn't say Simon says! You're out!", flush=True)
            time.sleep(2)
            return False


    def play_game(self):
        """Main game loop."""
        self.setup_game()
        self.game_active = True
        
        try:
            # Register event listener for touch sensors only
            print("Registering touch sensor events...")
            self.misty.register_event(
                event_name='touch_event',
                event_type=Events.TouchSensor,
                callback_function=lambda data: self.touched_callback(data),
                keep_alive=True
            )
            
            time.sleep(1)
            print("Events registered successfully!\n")
            
            # Main game loop - continue until WIN_SCORE successes or a failure
            while self.game_active and self.successful_commands < WIN_SCORE:
                print(f"\n{'='*50}")
                print(f"Score: {self.successful_commands}/{WIN_SCORE} successful commands")
                print(f"{'='*50}")
                
                # Decide whether to use "Simon says" or not
                use_simon_says = random.random() < SIMON_SAYS_PROBABILITY
                
                # Give the command
                self.give_command(use_simon_says)
                
                # Wait for player response
                self.wait_for_response()
                
                # Check if response was correct
                if not self.check_response():
                    # Player made a mistake - game over
                    self.game_active = False
                    break
                
                # Brief pause before next command
                time.sleep(1)
            
            # Check if player won
            if self.successful_commands >= WIN_SCORE:
                self.handle_victory()
            else:
                self.handle_game_over()
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted by user.")
            self.misty.speak("Game cancelled. Goodbye!", flush=True)
        except Exception as e:
            print(f"\nError during game: {e}")
            import traceback
            traceback.print_exc()
        finally:
            # Unregister events
            print("\nCleaning up...")
            try:
                self.misty.unregister_all_events()
            except:
                pass
            self.end_game()
            
    def handle_victory(self):
        """Celebrate the player's victory!"""
        print("\n" + "="*50)
        print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
        print("="*50)
        
        self.misty.display_image("e_Amazement.jpg", 1)  # Amazement face for winning!
        self.misty.speak("Congratulations! You won Simon Says! You're amazing!", flush=True)
        
        # Victory celebration animation
        for _ in range(5):
            self.misty.change_led(0, 255, 0)  # Green
            self.misty.move_arms(90, 90)
            self.misty.display_image("e_Joy.jpg", 1)  # Alternate joy
            time.sleep(0.3)
            self.misty.change_led(255, 255, 0)  # Yellow
            self.misty.move_arms(50, 50)
            self.misty.display_image("e_Amazement.jpg", 1)  # Back to amazement
            time.sleep(0.3)
            
        time.sleep(1)
        
    def handle_game_over(self):
        """Handle game over."""
        print("\n" + "="*50)
        print(f"GAME OVER - Score: {self.successful_commands}/{WIN_SCORE}")
        print("="*50)
        
        self.misty.display_image("e_Sadness.jpg", 1)  # Sad face for game over
        
        if self.successful_commands == 0:
            self.misty.speak("Nice try! Want to play again?", flush=True)
        elif self.successful_commands < (WIN_SCORE // 2):
            self.misty.speak(f"Good effort! You got {self.successful_commands} correct. Practice makes perfect!", flush=True)
        else:
            self.misty.speak(f"So close! You got {self.successful_commands} out of {WIN_SCORE}! Try again!", flush=True)
            
    def end_game(self):
        """Clean up and end the game."""
        print("\n" + "="*50)
        print(f"FINAL SCORE: {self.successful_commands}/{WIN_SCORE}")
        print("="*50)
        
        # Reset Misty
        self.misty.change_led(255, 255, 255)
        self.misty.display_image("e_DefaultContent.jpg", 1)
        self.misty.move_head(0, 0, 0, velocity=100)
        self.misty.move_arms(70, 70)
        
        self.misty.speak("Thanks for playing Simon Says with me!", flush=True)
        time.sleep(2)
        
        self.game_active = False


def main():
    """Main function to run the Simon Says game."""
    print("\n" + "=" * 50)
    print("MISTY SIMON SAYS - TOUCH SENSORS ONLY")
    print("=" * 50)
    print("\nHow to play:")
    print("1. Misty will give you commands")
    print("2. Only follow commands that start with 'Simon says'")
    print("3. If she doesn't say 'Simon says', DON'T touch!")
    print("4. Use TOUCH SENSORS only (Head, Chin, Scruff)")
    print(f"5. Get {WIN_SCORE} correct to win!")
    print("=" * 50)
    
    # Get robot IP address
    if MISTY_IP_ADDRESS:
        ip_address = MISTY_IP_ADDRESS
        print(f"\nUsing configured IP address: {ip_address}")
        print("(Change MISTY_IP_ADDRESS at the top of the file to use a different IP)")
    else:
        ip_address = input("\nEnter Misty's IP address (or press Enter for 192.168.1.100): ").strip()
        if not ip_address:
            ip_address = "192.168.1.100"  # Default IP
        
    print(f"\nConnecting to Misty at {ip_address}...")
    
    try:
        # Create game instance
        game = MistySimonSays(ip_address)
        
        # Start the game
        game.play_game()
        
    except Exception as e:
        print(f"\nError: {e}")
        print("Make sure Misty is powered on and connected to your network.")
        import traceback
        traceback.print_exc()
    
    print("\nGoodbye! 👋")


if __name__ == "__main__":
    main()

