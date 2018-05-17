# Lab 7: recursive descent
In this lab, you will write a parser for evolutionary trees on a simplified version of the Newick format.

You solution should have a lexer and a syntax analyzer using recursive descent.

## Write a lexical analyser
Write a "lexer" which takes a string on (presumably) Newick format and returns a list containing these tokens:
* The characters (, ), :, and ;
* Leaves as strings.
Spaces in the input string are ignored. Brackets are special: they denote comments that should be ignored.
For example, if the input string is ```Python (a,     (   b, c [hubba]))   ;``` then the lexer should return ```Python['(', 'a', ',', '(', 'b', ',', 'c', ')', ')', ';']```. 

### Hint
* You do not have to have perfect error handling in the lexer, but it can help you take add some checks for unexpected characters, for example. This can be helpful when debugging.
* You do not have to arrange with a special class for tokens, a list of strings works well in this exercise.

### The grammar and a parser
The grammar for trees is as follows.
```Python
start = tree ';'
      ;
tree = '(' tree ',' tree ')'
     | LEAF
     ;
```

Write a recursive descent parser "parse_newick" for this grammar, which takes as input a list of terminals a returned from your lexer. The parser should return a tree, which needs a datastructure that you should design. This datastructure should have the operations "n_leaves()" and "height()" defined. Hence, the following code should work in your finished module(s):
```Python
s = "((a,b), (c, d));"
t = parse_newick(lexer(s))
print(t.n_leaves()) # => 4
print(t.height())   # => 3
```
  
### Example data
You find some simple example data in my repo: da3018_rec_descent. Make your own test data as well!
