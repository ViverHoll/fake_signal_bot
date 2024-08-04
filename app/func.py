import os

from PIL import Image, ImageDraw


def add_text_on_photo(text: str,
                      photo_path: str,
                      new_path_photo: str):
    im = Image.open(photo_path)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (220, 80),
        text,
        fill=(144, 80, 235),
        stroke_width=2,
        font_size=200
    )
    im.save(new_path_photo)


if __name__ == "__main__":
    add_text_on_photo(
        "x2.94",
        os.path.abspath("image/lucky_jet.jpg"),
        os.path.abspath("image/lucky_jet_new.jpg")
    )
