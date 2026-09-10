import os
from PIL import Image, ImageDraw, ImageFont
import math

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets', 'diagrams')
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_fonts(size=16, bold_size=18):
    try:
        font_regular = ImageFont.truetype("arial.ttf", size)
        font_bold = ImageFont.truetype("arialbd.ttf", bold_size)
        font_small = ImageFont.truetype("arial.ttf", int(size * 0.85))
    except:
        font_regular = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_small = ImageFont.load_default()
    return font_regular, font_bold, font_small

def draw_arrow(draw, start, end, fill=(0, 0, 0), width=2, arrow_size=10):
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
    w, h = 1520, 520
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(16, 18)

    # Initial State
    start_x, start_y = 50, 237
    draw.ellipse([start_x - 14, start_y - 14, start_x + 14, start_y + 14], fill=(0, 0, 0))

    def draw_state(x, y, sw, sh, title, subtext=""):
        draw.rounded_rectangle([x + 3, y + 3, x + sw + 3, y + sh + 3], radius=14, fill=(225, 230, 238))
        draw.rounded_rectangle([x, y, x + sw, y + sh], radius=14, fill=(245, 248, 255), outline=(30, 58, 138), width=2)
        draw.text((x + sw // 2, y + (16 if subtext else sh // 2 - 10)), title, fill=(15, 23, 42), font=f_bold, anchor="mt" if subtext else "mm")
        if subtext:
            draw.text((x + sw // 2, y + 42), subtext, fill=(71, 85, 105), font=f_small, anchor="mt")

    # States
    # 1. At Sea: (140, 190, 210, 95)
    draw_state(140, 190, 210, 95, "At Sea", "entry / activate_sonar")
    draw_arrow(draw, (start_x + 14, start_y), (140, start_y))
    draw.text((95, 216), "depart", fill=(0, 0, 0), font=f_small, anchor="mm")

    # 2. Waiting at Anchorage: (520, 60, 260, 95)
    draw_state(520, 60, 260, 95, "Waiting at Anchorage", "do / monitor_radio_channel")

    # 3. Entering Harbor Channel: (520, 320, 260, 95)
    draw_state(520, 320, 260, 95, "Entering Harbor", "entry / harbor_pilot_onboard")

    # 4. Moored at Berth: (980, 150, 240, 95)
    draw_state(980, 150, 240, 95, "Moored at Berth", "entry / secure_lines")

    # 5. Cargo Operations: (980, 330, 240, 95)
    draw_state(980, 330, 240, 95, "Cargo Operations", "do / load_unload_containers")

    # Final State: (1360, 197)
    fin_x, fin_y = 1360, 197
    draw.ellipse([fin_x - 18, fin_y - 18, fin_x + 18, fin_y + 18], outline=(0, 0, 0), width=2, fill=(255, 255, 255))
    draw.ellipse([fin_x - 11, fin_y - 11, fin_x + 11, fin_y + 11], fill=(0, 0, 0))

    # Transitions
    # A. At Sea -> Waiting at Anchorage
    draw.line([(245, 190), (245, 107), (520, 107)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (510, 107), (520, 107))
    draw.text((380, 88), "approach_port [berth_busy == true]", fill=(185, 28, 28), font=f_small, anchor="mm")

    # B. At Sea -> Entering Harbor
    draw.line([(245, 285), (245, 367), (520, 367)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (510, 367), (520, 367))
    draw.text((380, 385), "approach_port [berth_busy == false]", fill=(15, 118, 110), font=f_small, anchor="mm")

    # C. Waiting at Anchorage -> Entering Harbor (Downwards, Left arrow at x=590)
    draw_arrow(draw, (590, 155), (590, 320))
    draw.text((580, 237), "berth_cleared / assign_pilot", fill=(2, 132, 199), font=f_small, anchor="rm")

    # D. Emergency abort: Entering Harbor -> Waiting at Anchorage (Upwards, Right arrow at x=710)
    draw.line([(710, 320), (710, 155)], fill=(185, 28, 28), width=2)
    draw_arrow(draw, (710, 165), (710, 155), fill=(185, 28, 28))
    draw.text((720, 237), "storm_warning [wind > 40kn]", fill=(185, 28, 28), font=f_small, anchor="lm")

    # E. Entering Harbor -> Moored at Berth
    draw.line([(780, 367), (880, 367), (880, 197), (980, 197)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (970, 197), (980, 197))
    draw.text((890, 280), "pilot_docked\n[draft <= depth]", fill=(15, 23, 42), font=f_small, anchor="lm")

    # F. Moored at Berth -> Cargo Operations
    draw_arrow(draw, (1100, 245), (1100, 330))
    draw.text((1110, 287), "berth_secured", fill=(0, 0, 0), font=f_small, anchor="lm")

    # G. Cargo Operations -> At Sea (Loop back via bottom)
    draw.line([(980, 400), (90, 400), (90, 255), (140, 255)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (130, 255), (140, 255))
    draw.text((500, 418), "cargo_cleared / cast_off [sea_clear == true]", fill=(15, 118, 110), font=f_small, anchor="mm")

    # H. Moored at Berth -> Final State (Decommission)
    draw_arrow(draw, (1220, 197), (1342, 197))
    draw.text((1281, 178), "decommission", fill=(100, 116, 139), font=f_small, anchor="mm")

    out_path = os.path.join(ASSETS_DIR, 'predicted_vessel_statemachine.png')
    im.save(out_path, 'PNG')
    print(f"Generated clean vessel state machine diagram at {out_path} successfully!")

if __name__ == "__main__":
    create_vessel_state_machine()
