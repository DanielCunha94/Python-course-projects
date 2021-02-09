def arithmetic_arranger(problems, show= False):
  
  if len(problems)>5:
    return "Error: Too many problems."

  f_str=f""
  s_str= t_str= q_str = f_str

  for index, value in enumerate(problems):
    problems[index] = value.replace(" ","")

    if problems[index].count("+") == 1:
      kk= problems[index].split("+")
      if not kk[0].isnumeric() or not kk[1].isnumeric():
        return "Error: Numbers must only contain digits."
      s= max(len(kk[0]), len(kk[1]))+2
      op = int(kk[0])+int(kk[1]) 
      sinal = "+"
    elif problems[index].count("-") == 1:
      kk= problems[index].split("-")
      if not kk[0].isnumeric() or not kk[1].isnumeric():
        return "Error: Numbers must only contain digits."
      s= max(len(kk[0]), len(kk[1]))+2
      op = int(kk[0])-int(kk[1])
      sinal = "-"
    else:
      return "Error: Operator must be '+' or '-'."
    
    if s-2>4:
      return "Error: Numbers cannot be more than four digits."

    l= "-"*s 
    f_str = f_str + f"{kk[0]:>{s}}"+ "    "
    s_str = s_str + f"{sinal}{kk[1]:>{s-1}}"+ "    "
    t_str = t_str + f"{l}"+ "    "
    q_str = q_str + f"{op:>{s}}"+ "    " 
  
  if show:
    final_str = f_str.rstrip()+"\n" + s_str.rstrip() + "\n" + t_str.rstrip() + "\n"+q_str.rstrip()
  else:
    final_str = f_str.rstrip()+"\n" + s_str.rstrip() + "\n" + t_str.rstrip()

  return final_str
  
  