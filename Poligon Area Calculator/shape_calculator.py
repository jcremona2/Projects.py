class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
    
  def set_width(self,width):
    self.width=width
  
  def set_height(self,height):
    self.height=height
    
  def get_area(self): 
    "Returns area (width * height)"
    return self.width*self.height
  def get_perimeter(self): 
    "Returns perimeter (2 * width + 2 * height)"
    return 2*self.width + 2*self.height
  def get_diagonal(self): 
    "Returns diagonal ((width ** 2 + height ** 2) ** .5)"
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self): 
    "Returns a string that represents the shape using lines of *."
    if self.width >=50 or self.height >=50:
      return "Too big for picture."
    else:
      aux=""
      for i in range(self.height):
        aux+="*"*self.width+"\n"
      return aux
  def get_amount_inside(self,shape): 
    "Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). "
    return self.get_area()//shape.get_area()
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
  def __init__(self,side):
    self.height=side
    self.width=self.height
  
  def set_side(self,value):
    self.height=value
    self.width=value

  def __str__(self):
    return f"Square(side={self.width})"