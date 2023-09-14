import re
import sys
sys.tracebacklimit=0
import warnings
warnings.filterwarnings(action='ignore', category=SyntaxWarning)

a=str(input("Please enter equation:"))
regexp= re.compile(r'[^+*()%/0-9\-]')
list_no=['+-', '-+', '*+', '+*', '+/' , '/+' , '-*', '*-', '-/', '/-' , '/*' , '*/']
res = [ele for ele in list_no if(ele in a)]
if regexp.search(a) or bool(res):
    print('Exquation is not valid. Your equation was')
    print(a)
else:
    try:
      b=eval(a)
    except TypeError:
      pass
      print("There was a mistake in the equation.Prehaps try adding a operator before the ().Your equation was:")
      print(a)
      sys.exit()
else:
    print(b)
