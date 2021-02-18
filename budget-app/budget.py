from math import floor
class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.total = 0

  def deposit(self, amount, description=""):
    obj = {"amount":amount,
    "description": description}

    self.ledger.append(obj)
    self.total += amount 

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      obj = {"amount": -amount,
      "description": description}

      self.ledger.append(obj)
      self.total -= amount 
      return True
    else:
      return False

  def get_balance(self):
    return self.total
  
  def transfer(self, amount, budget):
    if self.check_funds(amount): 
      description= f"Transfer to {budget.category}"
      self.withdraw(amount, description)

      description= f"Transfer from {self.category}"
      budget.deposit(amount, description )
      return True
    else:
      return False

  def check_funds(self, amount):
    return False if amount > self.total else True

  def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" +  f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            
        output = title + items + "Total: " + str(self.total)
        return output


def create_spend_chart(categories):
  total = 0
  data = {}
  size = len(categories)*3+1
  has = ' o '
  dont_has = '   '
  final='Percentage spent by category\n'

  for i in categories:
    data[i.category] = 0
    for j in i.ledger:
      if j['amount'] < 0:
        total +=    j['amount']
        data[i.category] += j['amount']
  
  total = abs(round(total,2))

  for i in data:
    data[i] = abs(round(data[i],2))
    data[i] = floor(((data[i]/total)*10))*10 

  for i in range(100,-10,-10):
    row = F"{i:3}|"
    for j in data:
      if data[j]>= i:
        row += has
      else:
       row += dont_has
    final += row +" \n"
    
  final += f"    {'-'*size}\n"

  max_word_size = len(max(data.keys(), key=len))

  for i in range(0,max_word_size):
    row2 = "    "
    for j in data:
      if i < len(j):
        row2 += f" {j[i]} "
      else:
        row2 += "   "

    if i < (max_word_size -1): 
      final += row2 +" \n" 
    else:
      final += row2 +" "
 
  return final 
      