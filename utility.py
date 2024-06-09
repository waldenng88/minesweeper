import settings


def height_shifter(percentage):
    return (settings.HEIGHT / 100) * percentage


def width_shifter(percentage):
    return (settings.WIDTH / 100) * percentage
