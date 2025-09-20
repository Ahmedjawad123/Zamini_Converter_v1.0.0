from PIL import Image, ImageDraw, ImageFont
import os

# Folder containing your images
folder = "media"

# Steps mapping
steps = {
    "step1_download.JPG": "Step 1: Download",
    "step2_open_rar.JPG": "Step 2: Open RAR",
    "step3_select_files.JPG": "Step 3: Select Files",
    "step4_software_view.JPG": "Step 4: Software View",
    "step5_rename.JPG": "Step 5: Rename",
    "step6_output.JPG": "Step 6: Output",
    "step_7_done.JPG": "Step 7: Done",
    "Zamini_Converter_page2.jpg": "Zamini Converter Page 2"
}

# Font path
font_path = "arial.ttf"  # make sure this exists

for filename, text in steps.items():
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        img = Image.open(path).convert("RGBA")
        txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        
        # Automatically adjust font size to fit image width
        font_size = int(img.width / len(text) * 1.5)  # heuristic
        font_size = max(30, min(font_size, 100))  # min 30px, max 100px
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (img.width - text_width) / 2
        y = 20  # 20px from top

        # Draw semi-transparent rectangle behind text
        draw.rectangle([x - 15, y - 10, x + text_width + 15, y + text_height + 10], fill=(0, 0, 0, 180))

        # Draw text
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

        # Combine layers and save
        combined = Image.alpha_composite(img, txt_layer).convert("RGB")
        combined.save(os.path.join(folder,filename))
        print(f"Labeled image saved: labeled_{filename}")
    else:
        print(f"{filename} not found")
