from PIL import Image, ImageDraw, ImageFont


def generate_meme(image_path, text, font_path, text_color, font_size, shadow_offset, shadow_color):
    image = Image.open(image_path)

    blank_image = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(blank_image)

    font = ImageFont.truetype(font_path, font_size)

    lines = text.split("\n")

    line_heights = [draw.textbbox((0, 0), line, font=font)[
        3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines]

    text_height = sum(line_heights)

    image_center = (image.width // 2, image.height*2 // 3)
    y_start = image.height - text_height - image.height // 6

    shadow_y = y_start
    for line, height in zip(lines, line_heights):
        text_width = draw.textbbox((0, 0), line, font=font)[
            2] - draw.textbbox((0, 0), line, font=font)[0]

        text_x = image_center[0] - text_width // 2 + shadow_offset[0]
        shadow_position = (text_x, shadow_y + shadow_offset[1])

        draw.text(shadow_position, line, fill=shadow_color, font=font)
        shadow_y += height

    text_y = y_start
    for line, height in zip(lines, line_heights):
        text_width = draw.textbbox((0, 0), line, font=font)[
            2] - draw.textbbox((0, 0), line, font=font)[0]

        text_x = image_center[0] - text_width // 2
        text_position = (text_x, text_y)

        draw.text(text_position, line, fill=text_color, font=font)
        text_y += height

    final_image = Image.alpha_composite(image.convert("RGBA"), blank_image)

    return final_image


image_path = "memes/69.JPG"
text = "If you want to master Python\n Subscribe for more tutorials"
font_path = "impact/impact.ttf"
font_size = 50
text_color = "white"
shadow_offset = (4, 4)
shadow_color = "black"

meme = generate_meme(image_path, text, font_path, text_color,
                     font_size, shadow_offset, shadow_color)
meme.show()
meme.save("GeneratedMemes/subscribe_meme.png")
