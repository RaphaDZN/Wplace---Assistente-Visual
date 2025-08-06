from PIL import Image, ImageDraw
import numpy as np
from scipy.spatial import KDTree

WPLACE_PALETTE = [
    "#000000", "#474747", "#858585", "#C2C2C2", "#FFFFFF", "#7F202A", "#D13345",
    "#FF6380", "#FFAEC1", "#A64A27", "#CF6A3B", "#E69C48", "#F5D4A5", "#A68627",
    "#D9B03B", "#FFF248", "#FFFBCB", "#4A7F20", "#6AD133", "#A5FF63", "#D9FFC2",
    "#207F56", "#33D18A", "#63FFAE", "#C2FFDD", "#2775A6", "#3B9AD9", "#48D4FF",
    "#A5EDFF", "#2734A6", "#3B4CCF", "#4869FF", "#A5B3FF", "#5627A6", "#8A3BD9",
    "#B048FF", "#DDA5FF", "#9C27A6", "#CF3BCB", "#FF48F5", "#FFA5FB"
]

PALETTE_RGB = np.array([tuple(int(c[i:i+2], 16) for i in (1, 3, 5)) for c in WPLACE_PALETTE])
KD_TREE = KDTree(PALETTE_RGB)

def process_image_for_guide(image_stream, grid_width, grid_height, include_white=False):
    try:
        input_image = Image.open(image_stream)
        image_with_alpha = input_image.convert("RGBA")
        resized_image = image_with_alpha.resize((grid_width, grid_height), Image.Resampling.LANCZOS)
        pixel_data = np.array(resized_image)
        pixels_to_paint = []
        for r in range(grid_height):
            for c in range(grid_width):
                pixel_rgba = pixel_data[r, c]
                if pixel_rgba[3] < 100: continue
                pixel_rgb = pixel_rgba[:3]
                if not include_white:
                    if pixel_rgb[0] > 245 and pixel_rgb[1] > 245 and pixel_rgb[2] > 245:
                        continue
                _, index = KD_TREE.query(pixel_rgb)
                closest_color_hex = WPLACE_PALETTE[index]
                if not include_white:
                    if closest_color_hex == "#FFFFFF":
                        continue
                pixels_to_paint.append({"row": r, "col": c, "color": closest_color_hex})
        return pixels_to_paint
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return None

def generate_instructions(pixels_to_paint, center_x, center_y, grid_width, grid_height):
    offset_x = grid_width // 2
    offset_y = grid_height // 2
    start_x = center_x - offset_x
    start_y = center_y - offset_y
    instructions = []
    for pixel in pixels_to_paint:
        instructions.append({
            "x": start_x + pixel["col"],
            "y": start_y + pixel["row"],
            "color": pixel["color"],
            "grid_pos": (pixel["row"], pixel["col"])
        })
    return instructions

def draw_minimap(processed_pixels, width, height, instructions, highlight_index=-1):
    cell_size = 12
    img_width = width * cell_size
    img_height = height * cell_size
    img = Image.new('RGB', (img_width, img_height), '#CCCCCC')
    draw = ImageDraw.Draw(img)

    for pixel in processed_pixels:
        col, row = pixel['col'], pixel['row']
        draw.rectangle(
            [(col * cell_size, row * cell_size), 
             ((col + 1) * cell_size - 1, (row + 1) * cell_size - 1)],
            fill=pixel['color']
        )
    
    if highlight_index != -1 and highlight_index < len(instructions):
        pixel_to_highlight = instructions[highlight_index]
        row, col = pixel_to_highlight['grid_pos']
        
        draw.rectangle(
            [(col * cell_size, row * cell_size), 
             ((col + 1) * cell_size - 1, (row + 1) * cell_size - 1)],
            outline="#00FF00", width=2
        )
            
    return img
