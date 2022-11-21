
def create_line(lista,nums,oper,space=""):
  leng=[len(num) for num in nums]
  leng=max(leng)
  if leng > 4:
    raise valueError("failed")
  leng+=2
  lista[0]+=str(space+(nums[0]).rjust(leng," "))
  lista[1]+=str(space+(oper+" "*(leng-len(nums[1])-1)+nums[1]))
  lista[2]+=str(space+"".rjust(leng,"-"))
  
  if oper =="+":
    lista[3]+=space+str(int(nums[0])+int(nums[1])).rjust(leng," ")
  else:
    lista[3]+=str(space+str(int(nums[0])-int(nums[1])).rjust(leng," "))
  return lista
      


def arithmetic_arranger(listnum,printval=False):


  if type(listnum)!= list :
    raise TypeError("Only lists are allowed")
    
  if len(listnum) > 5:
    return "Error: Too many problems." 
  toprint=["","","",""]
  space=""
  for operation in listnum:
    operation=operation.replace(" ","")
    if type(operation)!= str :
      raise TypeError("Operation Must be Strings")
    if "+" in operation:
      operands=operation.split("+")
      if operands[0].isnumeric() and operands[1].isnumeric():
        try:toprint=create_line(toprint,operands,"+",space)
        except: return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Numbers must only contain digits."      
    elif "-" in operation:
      operands=operation.split("-")
      if operands[0].isnumeric() and operands[1].isnumeric():
        try:toprint=create_line(toprint,operands,"-",space)
        except: return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Numbers must only contain digits."
    else:
      return "Error: Operator must be '+' or '-'."
    space="    "
  aux=""
  aux=toprint[0]+"\n"+toprint[1]+"\n"+toprint[2]
  if printval:
      aux+="\n"+toprint[3]
  return aux
    