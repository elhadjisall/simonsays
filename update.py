"""
Update Misty SDK

This script updates the Misty Python SDK with your robot's available API endpoints.
You only need to run this ONCE before using the game for the first time.

Instructions:
1. Make sure this file is in the same directory as the mistyPy folder
2. Update the IP address below with your Misty's IP
3. Run: python update.py
"""

from mistyPy.GenerateRobot import RobotGenerator


# ============================================
# SET YOUR MISTY'S IP ADDRESS HERE
# ============================================

ROBOT_IP_ADDRESS = "142.207.50.202"  # Replace with your Misty's actual IP address

# ============================================


def main():
    print("=" * 50)
    print("UPDATING MISTY PYTHON SDK")
    print("=" * 50)
    print(f"\nConnecting to Misty at: {ROBOT_IP_ADDRESS}")
    print("This will update the SDK with your robot's API endpoints...")
    print()
    
    try:
        # Generate the robot commands based on your Misty's API
        RobotGenerator(ROBOT_IP_ADDRESS)
        
        print()
        print("=" * 50)
        print("✓ SUCCESS! SDK Updated Successfully")
        print("=" * 50)
        print("\nYou can now run the Simon Says game!")
        print("Command: python misty_simon_says.py")
        print()
        
    except Exception as e:
        print()
        print("=" * 50)
        print("✗ ERROR: Failed to update SDK")
        print("=" * 50)
        print(f"\nError message: {e}")
        print()
        print("Troubleshooting:")
        print("1. Check that Misty is powered on")
        print("2. Verify Misty is connected to WiFi")
        print("3. Ensure the IP address above is correct")
        print("4. Make sure your computer is on the same network as Misty")
        print("5. Check that the mistyPy folder is in the parent directory")
        print()


if __name__ == "__main__":
    main()

