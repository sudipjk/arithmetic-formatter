def addition(l):
  k=0
  if l[2]=='+':
    k=int(l[0])+int(l[1])
  else:
    k=int(l[0])-int(l[1])
  return str(k).rjust(len(total_slashes(l)))

def bottom(l):
  s=""
  for i in range(len(l)):
    if i!=0:
      s+="    "+addition(l[i])
    else:
      s+=addition(l[i])
  return s
    


def total_slashes(l):
  s=""
  if len(l[0])>len(l[1]):
    s+=('-'*(len(l[0])+2))
  else:
    s+=('-'*(len(l[1])+2))
  return s

def slashes(l):
  s=""
  for i in range(len(l)):
    if i==0:
      s+=total_slashes(l[i])
    else:
      s+="    "+total_slashes(l[i])
  return s

def down(l):
  s=""
  if len(l[0])>len(l[1]):
    s=l[1].rjust(len(l[0]))
  else:
    s=l[1]
  return s

def front(l):
  s=""
  if len(l[0])>len(l[1]):
    s=l[0]
  else:
    s=l[0].rjust(len(l[1]))
  return s

def top(l):
  final=""
  for i in range(len(l)):
    if i==0:
      final+="  "+front(l[i])
    else:
      final+="      "+front(l[i])
  return final
  
def middle(l):
  s=""
  for i in range(len(l)):
    if i==0:
      s+=l[i][2]+" "+down(l[i])
    else:
      s+="    "+l[i][2]+" "+down(l[i])
  return s


def containsDigit(l):
  l[0]=l[0].strip()
  l[1]=l[1].strip()
  for i in range(len(l)):
    for j in range(len(l[i])):
      if ord(l[i][j])>=48 and ord(l[i][j])<=57:
        continue
      else:
        return False
  return True

def arithmetic_arranger(problems,option=False):
    final=[]
    if len(problems)>5:
      return "Error: Too many problems."
    for i in problems:
      if '+' not in i and '-' not in i:
        return "Error: Operator must be '+' or '-'."
      else:
        if '+' in i:
          l=i.split('+')
          if not containsDigit(l):
            return "Error: Numbers must only contain digits."
          else:
            if len(l[0])>4 or len(l[1])>4:
              return "Error: Numbers cannot be more than four digits."
            else:
              l.append('+')
              final.append(l)
        if '-' in i:
          l=i.split('-')
          if not containsDigit(l):
            return "Error: Numbers must only contain digits."
          else:
            if len(l[0])>4 or len(l[1])>4:
              return "Error: Numbers cannot be more than four digits."
            else:
              l.append('-')
              final.append(l)
    if option:
      return (top(final)+"\n"+middle(final)+"\n"+slashes(final)+"\n"+bottom(final))    
    else:
      return top(final)+"\n"+middle(final)+"\n"+slashes(final)