import ast
class Analysis_Ast_FuncDef(ast.NodeVisitor):
  count = 1
  def _init_(self):
    self.count = 1
    self.is_top_level = True

  def visit_FunctionDef(self, node):
    print("{} {} {}".format("FunctionDef", self.count, node.name))
    self.count=self.count+1
    self.generic_visit(node)

  