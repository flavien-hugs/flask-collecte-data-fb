import os
import random
import textwrap
from PIL import Image, ImageFont, ImageDraw
from apps.models import Content, Gender


class OpenGraphImage:

    def __init__(self, uid, first_name, description):
        background = self.base()
        self.location = self._location(uid)
        self.print_on_img(background, first_name.capitalize(), 70, 50)

        sentences = textwrap.wrap(description, width=60)
        current_h, pad = 180, 10

        for sentence in sentences:
            width, height = self.print_on_img(
                background, sentence, 40, current_h
            )
            current_h += height + pad

        background.save(self._path(uid))

    def _path(self, uid):
        return os.path.join(
            'apps', 'static',
            'tmp', f'{uid}.jpg'
        )

    def _location(self, uid):
        return f"tmp/{uid}.jpg"

    def base(self):
        img = Image.new('RGB', (1200, 630), "#18BC9C")
        return img

    def print_on_img(self, img, text, size, height):
        font = ImageFont.truetype(
            os.path.join(
                'apps', 'static', 'fonts',
                'Arcon-Regular.otf'
            ), size
        )
        draw = ImageDraw.Draw(img)
        width, height = draw.textsize(text, font)
        position = ((img.width - width)/2, height)
        draw.text(position, text, (255, 225, 255), font=font)
        return (height, height)


def find_content(gender):
    contents = Content.query.filter(Content.gender==Gender[gender]).all()
    return random.choice(contents)
