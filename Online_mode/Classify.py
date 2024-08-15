from .raw_material import raw_material
from .contact_form import contact_form


def classify(data, type):
    if type == "yclzbj":
        raw_material(data)
    elif type == "jljzlxd":
        contact_form(data)
