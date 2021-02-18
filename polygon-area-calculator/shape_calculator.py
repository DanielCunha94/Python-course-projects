class Rectangle:

  def __init__(self, width, heigth):
    self.width = width
    self.height= heigth

  def set_width(self, width):
    self.width = width

  def set_height(self, heigth):
    self.height= heigth

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2*self.width + 2*self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width< 50 and self.height <50 : 
      w = '*'* self.width + '\n'
      h= w * self.height 
      return h
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    w_times=0
    h_times=0
    if self.height >= shape.height:
      w_times = self.width // shape.width

    if self.width >= shape.width:
      h_times = self.height // shape.height
    return w_times*h_times

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, width):
    super().__init__(width, width)

  def set_width(self, width):
    self.width = width
    self.height= width

  def set_height(self, heigth):
    self.height= heigth
    self.width = heigth

  def set_side(self, heigth):
    self.height= heigth
    self.width = heigth
    
  def __str__(self):
    return f"Square(side={self.width})"
