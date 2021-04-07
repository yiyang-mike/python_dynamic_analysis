import ast
import subprocess
import sys
import ast_fund
import ast_test
import ast_call
import pdb
import time

count_files = 0

def general_dump(node):
  print(ast.dump(node,indent=2))

def find_all_file(visitor, fs, offset):
   for item in fs:
    if ".py" == item[-3:]:
      global count_files
      count_files=count_files+1
      print(item)
      p = subprocess.Popen(["cat", offset+item ],stdin=subprocess.PIPE 
                                                              ,stdout=subprocess.PIPE,
                                                              universal_newlines=True)
      code = ast.parse(p.stdout.read())
      ast_node = code
      visitor.visit(code)
    
      p.terminate()
    elif not "." in item and not len(item) == 0:
      print(offset+item)
      new_fs = list()
      fol = subprocess.Popen(["ls",offset+item],stdin=subprocess.PIPE 
                                                          ,stdout=subprocess.PIPE,
                                                           universal_newlines=True)
      all_fi = fol.stdout.read()
      new_fs = all_fi.split("\n")
      find_all_file(visitor, new_fs,offset+item+'/')

def lib_check(fs):
  tSTART = time.time()
  visitor = ast_call.Analysis_Ast_call()
  find_all_file(visitor, fs,sys.argv[1])
  inp = ' '

  print("\nFinished search for "+str(count_files)+" files"+" ({:.02f}s)".format(time.time() - tSTART))
  while len(inp)!= 0 or inp=="n":
    inp = input("dump? (full_dump/call/getattr/setattr/.../dyna) ")
    if inp == 'full_dump':
      general_dump(code)
    elif inp == 'sbc':
      print(visitor.get_subscript_count())
    elif inp == 'call':
      print(visitor.get_call_count())
    elif inp == 'name':
      print(visitor.get_name_count())
    elif inp == "getattr":
      print(visitor.get_getattr_count())
    elif inp == "delattr":
      print(visitor.get_delattr_count())
    elif inp == "setattr":
      print(visitor.get_setattr_count())
    elif inp == "hasattr":
      print(visitor.get_hasattr_count())
    elif inp == "dyna":
      print("hasattr {}".format(visitor.get_hasattr_count()))
      print("getattr {}".format(visitor.get_getattr_count()))
      print("delattr {}".format(visitor.get_delattr_count()))
      print("setattr {}".format(visitor.get_setattr_count()))
      print("eval {}".format(visitor.get_eval_count()))
      print("exec {}".format(visitor.get_exec_count()))

if __name__ == '__main__':
  open_file =sys.argv[1]
  fol = subprocess.Popen(["ls",open_file],stdin=subprocess.PIPE 
                                                          ,stdout=subprocess.PIPE,
                                                          universal_newlines=True)
  
  all_files = fol.stdout.read()

  fs = all_files.split("\n")

  print(fs)
  lib_check(fs)

  
  fol.terminate()

