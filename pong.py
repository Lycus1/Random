import tkinter as tk
import random

# Game constants
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 20
CEILING_OFFSET = 40  # Top boundary to account for the macOS menu/task bar

# --- Setup Main Window and Canvas ---
root = tk.Tk()
root.title("Pong Game")

# Get full screen dimensions
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
WINDOW_WIDTH = SCREEN_WIDTH
WINDOW_HEIGHT = SCREEN_HEIGHT - 200
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")

# Set the window to be borderless and always on top
root.overrideredirect(True)
root.attributes('-topmost', True)

# Set the game background color (using black now that transparentcolor is removed)
GAME_BG_COLOR = 'black'

# Create the Canvas for all game drawing
canvas = tk.Canvas(root, bg=GAME_BG_COLOR, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Give focus to the main window for immediate key press handling
root.focus_force()

# --- Draw Game Objects on the Canvas ---

# Function to draw a paddle (returns the Canvas Item ID)
def draw_paddle(x, y, width, height, color):
    return canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="")

# Initial positions
left_x = 50
right_x = WINDOW_WIDTH - 50 - PADDLE_WIDTH
center_y = WINDOW_HEIGHT // 2

# Create paddles and ball
left_paddle_id = draw_paddle(left_x, center_y - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, "red")
right_paddle_id = draw_paddle(right_x, center_y - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, "blue")
ball_id = canvas.create_oval(WINDOW_WIDTH // 2 - BALL_SIZE // 2, center_y - BALL_SIZE // 2,
                             WINDOW_WIDTH // 2 + BALL_SIZE // 2, center_y + BALL_SIZE // 2,
                             fill="white", outline="") # Changed ball color to white for visibility

# Initialize ball velocity
ball_dx = 5 * random.choice((1, -1))
ball_dy = 5 * random.choice((1, -1))

# --- Functions to move paddles ---
def move_paddle(paddle_id, dy):
    # Get current coordinates (x1, y1, x2, y2)
    coords = canvas.coords(paddle_id)
    y1 = coords[1]
    
    # Calculate new y position, clamping it between the ceiling and the bottom boundary
    new_y1 = max(CEILING_OFFSET, min(WINDOW_HEIGHT - PADDLE_HEIGHT, y1 + dy))
    new_y2 = new_y1 + PADDLE_HEIGHT
    
    # Update position on the canvas (x1 and x2 stay the same)
    canvas.coords(paddle_id, coords[0], new_y1, coords[2], new_y2)

def move_left_up(event): move_paddle(left_paddle_id, -PADDLE_SPEED)
def move_left_down(event): move_paddle(left_paddle_id, PADDLE_SPEED)
def move_right_up(event): move_paddle(right_paddle_id, -PADDLE_SPEED)
def move_right_down(event): move_paddle(right_paddle_id, PADDLE_SPEED)

# --- Bind key events to the root window (The fix for focus issues) ---
root.bind("<KeyPress-w>", move_left_up)
root.bind("<KeyPress-s>", move_left_down)
root.bind("<KeyPress-Up>", move_right_up)
root.bind("<KeyPress-Down>", move_right_down)

# --- Collision check ---
def check_collision(ball_coords, paddle_coords):
    # Ball coords: (bx1, by1, bx2, by2), Paddle coords: (px1, py1, px2, py2)
    bx1, by1, bx2, by2 = ball_coords
    px1, py1, px2, py2 = paddle_coords
    
    # Standard AABB (Axis-Aligned Bounding Box) collision detection
    return (bx1 < px2 and bx2 > px1 and
            by1 < py2 and by2 > py1)

# --- Main game loop ---
def update_game():
    global ball_dx, ball_dy
    
    ball_coords = canvas.coords(ball_id)
    x1, y1, x2, y2 = ball_coords
    
    # Calculate potential new position
    new_x1 = x1 + ball_dx
    new_y1 = y1 + ball_dy
    
    ball_width = x2 - x1

    # 1. Bounce off top and bottom boundaries
    if new_y1 <= CEILING_OFFSET or new_y1 >= WINDOW_HEIGHT - BALL_SIZE:
        ball_dy *= -1
        # Recalculate y position after bounce
        new_y1 = y1 + ball_dy 

    # 2. Get paddle coordinates for collision checking
    left_coords = canvas.coords(left_paddle_id)
    right_coords = canvas.coords(right_paddle_id)

    # 3. Bounce off paddles
    if check_collision((new_x1, new_y1, new_x1 + ball_width, new_y1 + BALL_SIZE), left_coords) or \
       check_collision((new_x1, new_y1, new_x1 + ball_width, new_y1 + BALL_SIZE), right_coords):
        ball_dx *= -1
        # Prevent the ball from sticking to the paddle edge
        new_x1 = x1 + ball_dx * 2

    # 4. Reset if ball leaves screen horizontally (Scoring opportunity)
    if new_x1 <= 0 or new_x1 >= WINDOW_WIDTH - ball_width:
        # Reset ball to center
        new_x1 = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        new_y1 = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = 5 * random.choice((1, -1))
        ball_dy = 5 * random.choice((1, -1))

    # 5. Move ball on canvas to the final calculated position
    canvas.coords(ball_id, new_x1, new_y1, new_x1 + ball_width, new_y1 + BALL_SIZE)

    # Loop the game at 10ms intervals
    root.after(15, update_game)

# --- Start Game ---
update_game()
root.mainloop()