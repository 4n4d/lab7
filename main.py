def lexer(input):
  # Input: string
  # Output: List containing tokens (, ), : and ;
  # Leaves as strings
  # anything between [] are comments that should be ignored.

  # remove all whitespace
  input = input.replace(" ", "")

  output = [] # list to be populated with tokens
  brac_count = 0 # if "enters a comment", brac_count increases
  i = 0 # loops through the elements if input
  
  while i < len(input):
    if input[i] in ['(',')',':',';',','] and brac_count == 0:
      output.append(input[i]) # just append the token
    elif input[i] == '[':
      brac_count = brac_count + 1 # increase the brac_count
    elif input[i] == ']':
      brac_count = brac_count - 1 # decrease the brac_count
      if brac_count < 0:
        raise TypeError # if closing a comment without starting it first
    elif brac_count == 0:
      # a string is detected, j is used to find the substring to make it into a token
      j = i + 1
      while not input[j] in ['(',')',':',';','[',']',','] and j < len(input):
        j = j + 1

      output.append(input[i:j])
      i = j - 1
        
    i = i + 1
  
  return output

class rooted_tree:
  def __init__(self, name = "Unnamed"):
    self._root = name
    self._children = []

  def append_child(self, c):
    self._children.append(c)

  def n_leaves(self):
    if self._children == []:
      return 1
    else:
      return self.__leaf_count()

  def __leaf_count(self):
    i = 0
    for c in self._children:
      i = i + c.n_leaves()
    return i
  
  def height(self):
    if self._children == []:
      return 0
    else:
      return 1 + self.__height_count()

  def __height_count(self):
    i = 0
    for c in self._children:
      j = c.height()
      if j > i:
        i = j
    return i

  def __str__(self):
    s = self._root
    if self._children != []:
      s = s + ":[ "
      for c in self._children:
        s = s + str(c) + ", "
      s = s[:-1] + " ] "
    return s
      
def parse_tree(input):
  # input: list of tokens
  # output: tree

  output = rooted_tree()
  
  if input[0] == '(':
    # everything until the next ',' should be parsed as a tree
    # identify this segment of the input string
    para_count = 0 # dont count ',' inside parenthesis
    i = 1

    while i < len(input):
      if input[i] == '(':
        para_count = para_count + 1
      elif input[i] == ')':
        para_count = para_count - 1
        if para_count < 0:
          raise KeyError # syntax error, too many closing parenthesis
      elif para_count == 0 and input[i] == ',':
        # found the ','
        break
      i = i + 1

    output.append_child(parse_tree(input[1:i]))
    i = i + 1
    j = i

    # find the second tree
    while j < len(input):
      if para_count == 0 and input[j] == ')':
        break
      elif input[j] == '(':
        para_count = para_count + 1
      elif input[j] == ')':
        para_count = para_count - 1
        if para_count < 0:
          raise KeyError # syntax error, too many closing parenthesis

      j = j + 1
    output.append_child(parse_tree(input[i:j]))
  
  else:
    # reinitialize rooted tree with the leaf-label
    output = rooted_tree(input[0])
    
  return output

def parse_newick(input):
  # input: list of tokens
  # output: tree

  # this function will only be called the first time, hence it is
  # the "start grammar"
  
  if input[-1] != ';':
    raise TypeError

  input = input[:-1]

  return parse_tree(input)



if __name__ == '__main__':
  print " "
  l = ["((a,b), (c, d));",
       "a;",
       " (a,    (  b,  c [hubba]))    ;"]
  for s in l:
    tlist = lexer(s)
    t = parse_newick(tlist)
    print "input         : " + s
    print "tokenrepr     : " + str(tlist)
    print "representation: " + str(t)
    print "height        : " + str(t.height())
    print "leaves        : " + str(t.n_leaves())
    print " "
