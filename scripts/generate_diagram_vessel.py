import os
from PIL import Image, ImageDraw, ImageFont
import math

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets', 'diagrams')
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_fonts():
    try:
        font_regular = ImageFont.truetype("arial.ttf", 15)
        font_bold = ImageFont.truetype("arialbd.ttf", 17)
        font_small = ImageFont.truetype("arial.ttf", 13)
        font_small_bold = ImageFont.truetype("arialbd.ttf", 13)
    except:
        font_regular = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_small_bold = ImageFont.load_default()
    return font_regular, font_bold, font_small, font_small_bold

def draw_arrow(draw, start, end, fill=(30, 41, 59), width=2, arrow_size=10):
    x1, y1 = start
    x2, y2 = end
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - arrow_size * math.cos(angle - math.pi / 6),
          y2 - arrow_size * math.sin(angle - math.pi / 6))
    p2 = (x2 - arrow_size * math.cos(angle + math.pi / 6),
          y2 - arrow_size * math.sin(angle + math.pi / 6))
    draw.polygon([end, p1, p2], fill=fill)

def create_vessel_state_machine():
    w, h = 1560, 560
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small, f_small_bold = get_fonts()

    # Helper to draw UML 2.5 State with upper compartment (Title) and lower compartment (Actions)
    def draw_uml_state(x, y, sw, sh, title, action=""):
        # Soft shadow
        draw.rounded_rectangle([x + 2, y + 2, x + sw + 2, y + sh + 2], radius=12, fill=(235, 240, 248))
        # Main State Box
        draw.rounded_rectangle([x, y, x + sw, y + sh], radius=12, fill=(248, 250, 253), outline=(30, 58, 138), width=2)
        # Title compartment
        title_h = 36 if action else sh
        draw.text((x + sw // 2, y + title_h // 2), title, fill=(15, 23, 42), font=f_bold, anchor="mm")
        
        if action:
            # Divider line between title and internal action compartment
            draw.line([(x + 1, y + title_h), (x + sw - 1, y + title_h)], fill=(191, 219, 254), width=1)
            # Action compartment text
            draw.text((x + sw // 2, y + title_h + (sh - title_h) // 2), action, fill=(71, 85, 105), font=f_small, anchor="mm")

    # Initial State (Solid black circle)
    start_x, start_y = 50, 240
    draw.ellipse([start_x - 13, start_y - 13, start_x + 13, start_y + 13], fill=(15, 23, 42))

    # States definition
    # 1. At Sea: x=140, y=190, w=220, h=95
    draw_uml_state(140, 190, 220, 95, "At Sea", "entry / activate_sonar")
    draw_arrow(draw, (start_x + 13, start_y), (140, start_y), fill=(15, 23, 42), width=2)
    draw.text((95, 222), "depart", fill=(30, 41, 59), font=f_small, anchor="mm")

    # 2. Waiting at Anchorage: x=530, y=45, w=280, h=95
    draw_uml_state(530, 45, 280, 95, "Waiting at Anchorage", "do / monitor_radio_channel")

    # 3. Entering Harbor: x=530, y=295, w=280, h=95
    draw_uml_state(530, 295, 280, 95, "Entering Harbor", "entry / harbor_pilot_onboard")

    # 4. Moored at Berth: x=1010, y=135, w=250, h=95
    draw_uml_state(1010, 135, 250, 95, "Moored at Berth", "entry / secure_lines")

    # 5. Cargo Operations: x=1010, y=315, w=250, h=95
    draw_uml_state(1010, 315, 250, 95, "Cargo Operations", "do / load_unload_containers")

    # Final State: bullseye at x=1420, y=182
    fin_x, fin_y = 1420, 182
    draw.ellipse([fin_x - 17, fin_y - 17, fin_x + 17, fin_y + 17], outline=(15, 23, 42), width=2, fill=(255, 255, 255))
    draw.ellipse([fin_x - 10, fin_y - 10, fin_x + 10, fin_y + 10], fill=(15, 23, 42))

    # --- TRANSITIONS ---
    # A. At Sea -> Waiting at Anchorage
    # Branch out of top of At Sea at (250, 190) -> up to y=92 -> right to (530, 92)
    draw.line([(250, 190), (250, 92), (520, 92)], fill=(30, 41, 59), width=2)
    draw_arrow(draw, (520, 92), (530, 92), fill=(30, 41, 59))
    draw.text((385, 75), "approach_port [berth_busy == true]", fill=(185, 28, 28), font=f_small, anchor="mm")

    # B. At Sea -> Entering Harbor
    # Branch out of bottom of At Sea at (250, 285) -> down to y=342 -> right to (530, 342)
    draw.line([(250, 285), (250, 342), (520, 342)], fill=(30, 41, 59), width=2)
    draw_arrow(draw, (520, 342), (530, 342), fill=(30, 41, 59))
    draw.text((385, 360), "approach_port [berth_busy == false]", fill=(13, 148, 136), font=f_small, anchor="mm")

    # C. Waiting at Anchorage -> Entering Harbor (Normal pilot clearance)
    # Straight down arrow at x=600 from y=140 to y=295
    draw_arrow(draw, (600, 140), (600, 295), fill=(2, 132, 199), width=2)
    draw.text((590, 217), "berth_cleared / assign_pilot", fill=(2, 132, 199), font=f_small, anchor="rm")

    # D. Entering Harbor -> Waiting at Anchorage (Emergency Storm Abort)
    # Straight up arrow at x=740 from y=295 to y=140 in red
    draw_arrow(draw, (740, 295), (740, 140), fill=(220, 38, 38), width=2)
    draw.text((750, 217), "storm_warning [wind > 40kn]", fill=(220, 38, 38), font=f_small, anchor="lm")

    # E. Entering Harbor -> Moored at Berth
    # Out of (810, 342) -> right to x=910 -> up to y=182 -> right to (1010, 182)
    draw.line([(810, 342), (910, 342), (910, 182), (1000, 182)], fill=(30, 41, 59), width=2)
    draw_arrow(draw, (1000, 182), (1010, 182), fill=(30, 41, 59))
    draw.text((920, 252), "pilot_docked", fill=(15, 23, 42), font=f_small, anchor="lm")
    draw.text((920, 272), "[draft <= depth]", fill=(71, 85, 105), font=f_small, anchor="lm")

    # F. Moored at Berth -> Cargo Operations
    # Straight down from (1135, 230) to (1135, 315)
    draw_arrow(draw, (1135, 230), (1135, 315), fill=(30, 41, 59), width=2)
    draw.text((1145, 272), "berth_secured", fill=(15, 23, 42), font=f_small, anchor="lm")

    # G. Cargo Operations -> At Sea (Loopback departure)
    # Routed cleanly well BELOW all state boxes at y=485 (box ends at y=410, leaving 75px clearance!)
    draw.line([(1135, 410), (1135, 485), (90, 485), (90, 260), (130, 260)], fill=(30, 41, 59), width=2)
    draw_arrow(draw, (130, 260), (140, 260), fill=(30, 41, 59))
    draw.text((560, 505), "cargo_cleared / cast_off [sea_clear == true]", fill=(13, 148, 136), font=f_small_bold, anchor="mm")

    # H. Moored at Berth -> Final State (Decommission)
    draw_arrow(draw, (1260, 182), (1402, 182), fill=(100, 116, 139), width=2)
    draw.text((1330, 162), "decommission", fill=(100, 116, 139), font=f_small, anchor="mm")

    out_path = os.path.join(ASSETS_DIR, 'predicted_vessel_statemachine.png')
    im.save(out_path, 'PNG')
    print(f"Generated clean vessel state machine diagram at {out_path} successfully!")

if __name__ == "__main__":
    create_vessel_state_machine()

