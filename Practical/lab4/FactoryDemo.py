import ShapeFactory

shape_factory: ShapeFactory = ShapeFactory()

circle = shape_factory.getObject('circle')
circle.draw()