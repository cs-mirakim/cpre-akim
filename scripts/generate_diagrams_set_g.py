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
# -------------------------------------------------------------
# 3. Q21: Activity Diagram 1 (Checkout Payment & Inventory - Fork/Join)
# -------------------------------------------------------------
def create_activity_fork_join():
    w, h = 1000, 960
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(18, 20)

    # Title Banner
    draw.rectangle([0, 0, w, 40], fill=(245, 247, 250))
    draw.line([(0, 40), (w, 40)], fill=(210, 215, 225), width=1)
    draw.text((w//2, 20), "UML Activity Diagram: Order Processing & Fulfillment Workflow", fill=(60, 70, 85), font=f_small, anchor="mm")

    # Initial node
    draw.ellipse([485, 65, 515, 95], fill=(0, 0, 0))
    draw.line([(500, 95), (500, 135)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 135), (495, 125), (505, 125)], fill=(0, 0, 0))

    # Action 1: Receive Order
    draw.rounded_rectangle([370, 135, 630, 195], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 165), "Receive Order", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Fork Bar
    draw.line([(500, 195), (500, 245)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 245), (495, 235), (505, 235)], fill=(0, 0, 0))

    # Fork Bar (thick horizontal)
    draw.rectangle([180, 245, 820, 257], fill=(0, 0, 0))
    draw.text((835, 251), "«fork»", fill=(80, 80, 80), font=f_small, anchor="lm")

    # Branch A: Process Payment (left)
    draw.line([(310, 257), (310, 315)], fill=(0, 0, 0), width=2)
    draw.polygon([(310, 315), (305, 305), (315, 305)], fill=(0, 0, 0))
    draw.rounded_rectangle([180, 315, 440, 375], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((310, 345), "Process Payment", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Branch B: Reserve Inventory (right)
    draw.line([(690, 257), (690, 315)], fill=(0, 0, 0), width=2)
    draw.polygon([(690, 315), (685, 305), (695, 305)], fill=(0, 0, 0))
    draw.rounded_rectangle([560, 315, 820, 375], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((690, 345), "Reserve Inventory", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Sub-action under Payment: Verify Payment Token
    draw.line([(310, 375), (310, 435)], fill=(0, 0, 0), width=2)
    draw.polygon([(310, 435), (305, 425), (315, 425)], fill=(0, 0, 0))
    draw.rounded_rectangle([180, 435, 440, 495], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((310, 465), "Verify Payment Token", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Sub-action under Stock: Generate Packing Slip
    draw.line([(690, 375), (690, 435)], fill=(0, 0, 0), width=2)
    draw.polygon([(690, 435), (685, 425), (695, 425)], fill=(0, 0, 0))
    draw.rounded_rectangle([560, 435, 820, 495], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((690, 465), "Generate Packing Slip", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Both down to Join Bar
    draw.line([(310, 495), (310, 560)], fill=(0, 0, 0), width=2)
    draw.polygon([(310, 560), (305, 550), (315, 550)], fill=(0, 0, 0))
    draw.line([(690, 495), (690, 560)], fill=(0, 0, 0), width=2)
    draw.polygon([(690, 560), (685, 550), (695, 550)], fill=(0, 0, 0))

    # Join Bar (thick horizontal)
    draw.rectangle([180, 560, 820, 572], fill=(0, 0, 0))
    draw.text((835, 566), "«join»", fill=(80, 80, 80), font=f_small, anchor="lm")

    # After Join: Send Confirmation Email
    draw.line([(500, 572), (500, 635)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 635), (495, 625), (505, 625)], fill=(0, 0, 0))
    draw.rounded_rectangle([340, 635, 660, 695], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 665), "Send Confirmation Email", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Final Node
    draw.line([(500, 695), (500, 755)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 755), (495, 745), (505, 745)], fill=(0, 0, 0))
    draw.ellipse([480, 755, 520, 795], outline=(0, 0, 0), width=2)
    draw.ellipse([487, 762, 513, 788], fill=(0, 0, 0))

    out_path = os.path.join(ASSETS_DIR, 'predicted_q21_activity.png')
    im.save(out_path)
    print(f"Saved {out_path}")

# -------------------------------------------------------------
# 4. Q23: Activity Diagram 2 (Decision Diamond & Guard Conditions)
# -------------------------------------------------------------
def create_activity_decision():
    w, h = 1000, 960
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    f_reg, f_bold, f_small = get_fonts(18, 20)

    # Title Banner
    draw.rectangle([0, 0, w, 40], fill=(245, 247, 250))
    draw.line([(0, 40), (w, 40)], fill=(210, 215, 225), width=1)
    draw.text((w//2, 20), "UML Activity Diagram: Logistics Parcel Dispatch Decision & Merge", fill=(60, 70, 85), font=f_small, anchor="mm")

    # Initial node
    draw.ellipse([485, 65, 515, 95], fill=(0, 0, 0))
    draw.line([(500, 95), (500, 135)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 135), (495, 125), (505, 125)], fill=(0, 0, 0))

    # Action 1: Inspect Parcel Weight
    draw.rounded_rectangle([360, 135, 640, 195], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 165), "Inspect Parcel Weight", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Decision Diamond
    draw.line([(500, 195), (500, 255)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 255), (495, 245), (505, 245)], fill=(0, 0, 0))

    # Decision Diamond center at (500, 285)
    draw.polygon([(500, 255), (545, 285), (500, 315), (455, 285)], fill=(254, 243, 226), outline=(0, 0, 0), width=2)

    # Branch 1 (Left): [Weight > 30 kg] -> Assign Heavy Freight Carrier
    draw.line([(455, 285), (280, 285), (280, 375)], fill=(0, 0, 0), width=2)
    draw.polygon([(280, 375), (275, 365), (285, 365)], fill=(0, 0, 0))
    draw.text((350, 260), "[Weight > 30 kg]", fill=(160, 20, 20), font=f_bold, anchor="ms")

    draw.rounded_rectangle([130, 375, 430, 435], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((280, 405), "Assign Heavy Freight Carrier", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Branch 2 (Right): [Weight <= 30 kg] -> Assign Standard Courier
    draw.line([(545, 285), (720, 285), (720, 375)], fill=(0, 0, 0), width=2)
    draw.polygon([(720, 375), (715, 365), (725, 365)], fill=(0, 0, 0))
    draw.text((650, 260), "[Weight <= 30 kg]", fill=(20, 120, 20), font=f_bold, anchor="ms")

    draw.rounded_rectangle([570, 375, 870, 435], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((720, 405), "Assign Standard Courier", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Both down to Merge Diamond at (500, 525)
    draw.line([(280, 435), (280, 525), (455, 525)], fill=(0, 0, 0), width=2)
    draw.polygon([(455, 525), (445, 520), (445, 530)], fill=(0, 0, 0))

    draw.line([(720, 435), (720, 525), (545, 525)], fill=(0, 0, 0), width=2)
    draw.polygon([(545, 525), (555, 520), (555, 530)], fill=(0, 0, 0))

    # Merge diamond
    draw.polygon([(500, 495), (545, 525), (500, 555), (455, 525)], fill=(254, 243, 226), outline=(0, 0, 0), width=2)

    # Down from Merge to "Generate Shipping Label"
    draw.line([(500, 555), (500, 625)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 625), (495, 615), (505, 615)], fill=(0, 0, 0))

    draw.rounded_rectangle([340, 625, 660, 685], radius=16, fill=(254, 243, 226), outline=(0, 0, 0), width=2)
    draw.text((500, 655), "Generate Shipping Label", fill=(0, 0, 0), font=f_bold, anchor="mm")

    # Down to Final Node
    draw.line([(500, 685), (500, 755)], fill=(0, 0, 0), width=2)
    draw.polygon([(500, 755), (495, 745), (505, 745)], fill=(0, 0, 0))
    draw.ellipse([480, 755, 520, 795], outline=(0, 0, 0), width=2)
    draw.ellipse([487, 762, 513, 788], fill=(0, 0, 0))

    out_path = os.path.join(ASSETS_DIR, 'predicted_q23_activity.png')
    im.save(out_path)
    print(f"Saved {out_path}")

if __name__ == '__main__':
    create_class_diagram()
    create_state_machine()
    create_activity_fork_join()
    create_activity_decision()
    print("All 4 predicted diagrams created successfully!")
