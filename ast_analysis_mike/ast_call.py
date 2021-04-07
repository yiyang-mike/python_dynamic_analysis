import ast
class Analysis_Ast_call(ast.NodeVisitor):
  count = 1
  subscrip_count = 1
  name_count = 1
  getattr_c = 0
  setattr_c = 0
  delattr_c = 0
  hasattr_c = 0
  eval_c = 0
  exec_c = 0
  def _init_(self):
    self.count = 0
    self.subscrip_count = 0
    self.name_count = 0

  def get_call_count(self):
    return self.count

  def get_getattr_count(self):
    return self.getattr_c 
  def get_setattr_count(self):
    return self.setattr_c 
  def get_delattr_count(self):
    return self.delattr_c 
  def get_hasattr_count(self):
    return self.hasattr_c 
  def get_eval_count(self):
    return self.eval_c
  def get_exec_count(self):
    return self.exec_c

  def get_subscript_count(self):
    return self.subscrip_count

  def get_name_count(self):
    return self.name_count

  def visit_Call(self, node):
    if isinstance(node.func, ast.Name):
      if("getattr" in node.func.id):
        self.getattr_c = self.getattr_c + 1
      elif("setattr" in node.func.id):
        self.setattr_c = self.setattr_c + 1
      elif("delattr" in node.func.id):
        self.delattr_c = self.delattr_c + 1
      elif("hasattr" in node.func.id):
        self.hasattr_c = self.hasattr_c + 1
      elif("eval" in node.func.id):
        self.eval_c = self.eval_c + 1
      elif("exec" in node.func.id):
        self.exec_c = self.exec_c + 1
    for i in node.args:
      if isinstance(i, ast.Name):
        if("getattr" in i.id):
          self.getattr_c = self.getattr_c + 1
        elif("setattr" in i.id):
          self.setattr_c = self.setattr_c + 1
        elif("delattr" in i.id):
          self.delattr_c = self.delattr_c + 1
        elif("hasattr" in i.id):
          self.hasattr_c = self.hasattr_c + 1
        elif("eval" in i.id):
          self.eval_c = self.eval_c + 1
        elif("exec" in i.id):
          self.exec_c = self.exec_c + 1


    if isinstance(node, ast.Name):
      self.name_count = self.name_count+1
    
    self.count=self.count+1
    self.generic_visit(node)

  def visit_Name(self, node):
    self.name_count = self.name_count+1
    self.generic_visit(node)

  def visit_Subscript(self,node):
    self.subscrip_count = self.subscrip_count+1
    self.generic_visit(node)
