import Circle, Rectangle, Square


class ShapeFactory:

    def getObject(shapeType:str):
        if shapeType:
            if shapeType.title() in ['Circle', 'Rectangle', 'Square']:
                shapeType = shapeType.title()
                return globals()[shapeType]()
            else:
                return None
        else:
            return None
