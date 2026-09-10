import os
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets', 'diagrams')
os.makedirs(ASSETS_DIR, exist_ok=True)

# Helper to get font
def get_fonts(size=20, bold_size=22):
    try:
        # Standard Windows fonts
        font_regular = ImageFont.truetype("arial.ttf", size)
        font_bold = ImageFont.truetype("arialbd.ttf", bold_size)
        font_small = ImageFont.truetype("arial.ttf", int(size * 0.85))
    except:
        font_regular = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_small = ImageFont.load_default()
    return font_regular, font_bold, font_small

# -------------------------------------------------------------
# 1. Q18: UML Class Diagram (Customer - Order - OrderItem - Product)
# -------------------------------------------------------------
def create_class_diagram():
    w, h = 1400, 420
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(20, 22)

    # Class 1: Customer (left: 80, top: 100, w: 240, h: 200)
    # Class 2: Order (left: 460, top: 100, w: 240, h: 200)
    # Class 3: OrderItem (left: 840, top: 100, w: 240, h: 200)
    # Class 4: Product (left: 1140, top: 100, w: 200, h: 200)

    classes = [
        ("Customer", ["id: String", "name: String", "email: String"], 80, 100, 240, 200),
        ("Order", ["orderNumber: String", "date: Date", "totalAmount: Decimal"], 460, 100, 280, 200),
        ("OrderItem", ["quantity: Integer", "unitPrice: Decimal"], 870, 100, 240, 200),
        ("Product", ["productCode: String", "title: String", "stock: Integer"], 1180, 100, 200, 200),
    ]

    for title, attrs, x, y, cw, ch in classes:
        # Shadow
        draw.rectangle([x+4, y+4, x+cw+4, y+ch+4], fill=(225, 225, 225))
        # Card body
        draw.rectangle([x, y, x+cw, y+ch], fill=(254, 243, 226), outline=(0, 0, 0), width=2)
        # Header separator
        header_h = 48
        draw.line([(x, y+header_h), (x+cw, y+header_h)], fill=(0, 0, 0), width=2)
        # Title
        draw.text((x + cw//2, y + 14), title, fill=(0, 0, 0), font=f_bold, anchor="mt")
        # Attributes
        ay = y + header_h + 16
        for attr in attrs:
            draw.text((x + 16, ay), attr, fill=(128, 20, 20), font=f_reg)
            ay += 32

    # Association Lines
    # Customer to Order
    draw.line([(320, 200), (460, 200)], fill=(0, 0, 0), width=2)
    draw.text((330, 208), "1", fill=(0, 0, 0), font=f_bold)
    draw.text((420, 208), "0..*", fill=(0, 0, 0), font=f_bold)
    draw.text((350, 175), "places", fill=(0, 0, 0), font=f_small)
    draw.polygon([(410, 182), (410, 192), (418, 187)], fill=(0, 0, 0))

    # Order to OrderItem
    draw.line([(740, 200), (870, 200)], fill=(0, 0, 0), width=2)
    draw.text((750, 208), "1", fill=(0, 0, 0), font=f_bold)
    draw.text((820, 208), "1..*", fill=(0, 0, 0), font=f_bold)
    draw.text((765, 175), "contains", fill=(0, 0, 0), font=f_small)
    draw.polygon([(835, 182), (835, 192), (843, 187)], fill=(0, 0, 0))

    # OrderItem to Product
    draw.line([(1110, 200), (1180, 200)], fill=(0, 0, 0), width=2)
    draw.text((1120, 208), "*", fill=(0, 0, 0), font=f_bold)
    draw.text((1155, 208), "1", fill=(0, 0, 0), font=f_bold)

    out_path = os.path.join(ASSETS_DIR, 'predicted_q18_class.png')
    im.save(out_path)
    print(f"Saved {out_path}")

# -------------------------------------------------------------
# 2. Q20: State Machine Diagram (Order Lifecycle)
# -------------------------------------------------------------
def create_state_machine():
    w, h = 1300, 680
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(18, 20)

    # States
    states = {
        "Created": (180, 100, 220, 70),
        "Authorized": (540, 100, 240, 70),
        "Shipped": (920, 100, 220, 70),
        "Cancelled": (540, 380, 240, 70),
        "Delivered": (920, 380, 220, 70)
    }

    # Initial state
    draw.ellipse([80, 120, 110, 150], fill=(0, 0, 0))
    draw.line([(110, 135), (180, 135)], fill=(0, 0, 0), width=2)
    # arrow head
    draw.polygon([(180, 135), (170, 130), (170, 140)], fill=(0, 0, 0))

    for name, (x, y, sw, sh) in states.items():
        # Shadow
        draw.rounded_rectangle([x+4, y+4, x+sw+4, y+sh+4], radius=16, fill=(225, 225, 225))
        # Rounded box
        draw.rounded_rectangle([x, y, x+sw, y+sh], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
        draw.text((x + sw//2, y + sh//2), name, fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Transition 1: Created -> Authorized
    draw.line([(400, 135), (540, 135)], fill=(0, 0, 0), width=2)
    draw.polygon([(540, 135), (530, 130), (530, 140)], fill=(0, 0, 0))
    draw.text((470, 105), "payment authorized", fill=(0, 0, 0), font=f_small, anchor="ms")

    # Transition 2: Authorized -> Shipped
    draw.line([(780, 135), (920, 135)], fill=(0, 0, 0), width=2)
    draw.polygon([(920, 135), (910, 130), (910, 140)], fill=(0, 0, 0))
    draw.text((850, 105), "items dispatched", fill=(0, 0, 0), font=f_small, anchor="ms")

    # Transition 3: Shipped -> Delivered
    draw.line([(1030, 170), (1030, 380)], fill=(0, 0, 0), width=2)
    draw.polygon([(1030, 380), (1025, 370), (1035, 370)], fill=(0, 0, 0))
    draw.text((1045, 275), "delivery confirmed", fill=(0, 0, 0), font=f_small, anchor="ls")

    # Transition 4: Created -> Cancelled
    draw.line([(290, 170), (290, 415), (540, 415)], fill=(0, 0, 0), width=2)
    draw.polygon([(540, 415), (530, 410), (530, 420)], fill=(0, 0, 0))
    draw.text((380, 395), "customer cancels", fill=(0, 0, 0), font=f_small, anchor="ms")

    # Transition 5: Authorized -> Cancelled
    draw.line([(660, 170), (660, 380)], fill=(0, 0, 0), width=2)
    draw.polygon([(660, 380), (655, 370), (665, 370)], fill=(0, 0, 0))
    draw.text((670, 275), "fraud detected / refund", fill=(0, 0, 0), font=f_small, anchor="ls")

    # Final state after Delivered
    draw.line([(1030, 450), (1030, 520)], fill=(0, 0, 0), width=2)
    draw.polygon([(1030, 520), (1025, 510), (1035, 510)], fill=(0, 0, 0))
    draw.ellipse([1010, 520, 1050, 560], outline=(0, 0, 0), width=2)
    draw.ellipse([1017, 527, 1043, 553], fill=(0, 0, 0))

    # Final state after Cancelled
    draw.line([(660, 450), (660, 520)], fill=(0, 0, 0), width=2)
    draw.polygon([(660, 520), (655, 510), (665, 510)], fill=(0, 0, 0))
    draw.ellipse([640, 520, 680, 560], outline=(0, 0, 0), width=2)
    draw.ellipse([647, 527, 673, 553], fill=(0, 0, 0))

    out_path = os.path.join(ASSETS_DIR, 'predicted_q20_statemachine.png')
    im.save(out_path)
    print(f"Saved {out_path}")

# -------------------------------------------------------------
# 3. Q21: Activity Diagram 1 (Checkout Payment & Inventory - Fork/Join)
# -------------------------------------------------------------
def create_activity_fork_join():
    w, h = 1000, 950
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(18, 20)

    # Initial node
    draw.ellipse([485, 40, 515, 70], fill=(0, 0, 0))
    draw.line([(500, 70), (500, 110)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 110), (495, 100), (505, 100)], fill=(0, 0, 0))

    # Action 1: Receive Order
    draw.rounded_rectangle([380, 110, 620, 170], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 140), "Receive Order", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Fork Bar
    draw.line([(500, 170), (500, 220)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 220), (495, 210), (505, 210)], fill=(0, 0, 0))

    # Fork Bar (thick horizontal)
    draw.rectangle([200, 220, 800, 230], fill=(0, 0, 0))

    # Branch A: Charge Payment (left)
    draw.line([(320, 230), (320, 290)], fill=(0, 0, 0), width=2)
    draw.polygon([(320, 290), (315, 280), (325, 280)], fill=(0, 0, 0))
    draw.rounded_rectangle([200, 290, 440, 350], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((320, 320), "Process Payment", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Branch B: Reserve Warehouse Stock (right)
    draw.line([(680, 230), (680, 290)], fill=(0, 0, 0), width=2)
    draw.polygon([(680, 290), (675, 280), (685, 280)], fill=(0, 0, 0))
    draw.rounded_rectangle([560, 290, 800, 350], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((680, 320), "Reserve Stock", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Sub-action under Payment: Validate Fraud Check
    draw.line([(320, 350), (320, 400)], fill=(0, 0, 0), width=2)
    draw.polygon([(320, 400), (315, 390), (325, 390)], fill=(0, 0, 0))
    draw.rounded_rectangle([200, 400, 440, 460], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((320, 430), "Verify Security Token", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Sub-action under Stock: Generate Packing Slip
    draw.line([(680, 350), (680, 400)], fill=(0, 0, 0), width=2)
    draw.polygon([(680, 400), (675, 390), (685, 390)], fill=(0, 0, 0))
    draw.rounded_rectangle([560, 400, 800, 460], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((680, 430), "Print Packing Slip", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Both down to Join Bar
    draw.line([(320, 460), (320, 520)], fill=(0, 0, 0), width=2)
    draw.polygon([(320, 520), (315, 510), (325, 510)], fill=(0, 0, 0))
    draw.line([(680, 460), (680, 520)], fill=(0, 0, 0), width=2)
    draw.polygon([(680, 520), (675, 510), (685, 510)], fill=(0, 0, 0))

    # Join Bar (thick horizontal)
    draw.rectangle([200, 520, 800, 530], fill=(0, 0, 0))

    # After Join: Send Order Confirmation
    draw.line([(500, 530), (500, 590)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 590), (495, 580), (505, 580)], fill=(0, 0, 0))
    draw.rounded_rectangle([350, 590, 650, 650], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 620), "Send Confirmation Email", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Final Node
    draw.line([(500, 650), (500, 710)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 710), (495, 700), (505, 700)], fill=(0, 0, 0))
    draw.ellipse([480, 710, 520, 750], outline=(0, 0, 0), width=2)
    draw.ellipse([487, 717, 513, 743], fill=(0, 0, 0))

    out_path = os.path.join(ASSETS_DIR, 'predicted_q21_activity.png')
    im.save(out_path)
    print(f"Saved {out_path}")

# -------------------------------------------------------------
# 4. Q23: Activity Diagram 2 (Decision Diamond & Guard Conditions)
# -------------------------------------------------------------
def create_activity_decision():
    w, h = 1000, 950
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(18, 20)

    # Initial node
    draw.ellipse([485, 40, 515, 70], fill=(0, 0, 0))
    draw.line([(500, 70), (500, 110)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 110), (495, 100), (505, 100)], fill=(0, 0, 0))

    # Action 1: Weigh Package
    draw.rounded_rectangle([380, 110, 620, 170], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 140), "Weigh Package", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Decision Diamond
    draw.line([(500, 170), (500, 230)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 230), (495, 220), (505, 220)], fill=(0, 0, 0))

    # Diamond center at (500, 260)
    draw.polygon([(500, 230), (540, 260), (500, 290), (460, 260)], fill=(254, 243, 226), outline=(0, 0, 0), width=2)

    # Branch 1 (Left): [Weight > 30kg] -> Freight Transport
    draw.line([(460, 260), (300, 260), (300, 340)], fill=(0, 0, 0), width=2)
    draw.polygon([(300, 340), (295, 330), (305, 330)], fill=(0, 0, 0))
    draw.text((360, 240), "[Weight > 30kg]", fill=(0, 0, 0), font=f_small, anchor="ms")

    draw.rounded_rectangle([180, 340, 420, 400], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((300, 370), "Assign Freight Carrier", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Branch 2 (Right): [Weight <= 30kg] -> Standard Courier
    draw.line([(540, 260), (700, 260), (700, 340)], fill=(0, 0, 0), width=2)
    draw.polygon([(700, 340), (695, 330), (705, 330)], fill=(0, 0, 0))
    draw.text((640, 240), "[Weight <= 30kg]", fill=(0, 0, 0), font=f_small, anchor="ms")

    draw.rounded_rectangle([580, 340, 820, 400], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((700, 370), "Assign Standard Courier", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Both down to Merge Diamond at (500, 480)
    draw.line([(300, 400), (300, 480), (460, 480)], fill=(0, 0, 0), width=2)
    draw.polygon([(460, 480), (450, 475), (450, 485)], fill=(0, 0, 0))

    draw.line([(700, 400), (700, 480), (540, 480)], fill=(0, 0, 0), width=2)
    draw.polygon([(540, 480), (550, 475), (550, 485)], fill=(0, 0, 0))

    # Merge diamond
    draw.polygon([(500, 450), (540, 480), (500, 510), (460, 480)], fill=(254, 243, 226), outline=(0, 0, 0), width=2)

    # Down from Merge to "Generate Shipping Label"
    draw.line([(500, 510), (500, 570)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 570), (495, 560), (505, 560)], fill=(0, 0, 0))

    draw.rounded_rectangle([360, 570, 640, 630], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 600), "Generate Shipping Label", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Final Node
    draw.line([(500, 630), (500, 690)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 690), (495, 680), (505, 680)], fill=(0, 0, 0))
    draw.ellipse([480, 690, 520, 730], outline=(0, 0, 0), width=2)
    draw.ellipse([487, 697, 513, 723], fill=(0, 0, 0))

    out_path = os.path.join(ASSETS_DIR, 'predicted_q23_activity.png')
    im.save(out_path)
    print(f"Saved {out_path}")

if __name__ == '__main__':
    create_class_diagram()
    create_state_machine()
    create_activity_fork_join()
    create_activity_decision()
    print("All 4 predicted diagrams created successfully!")
