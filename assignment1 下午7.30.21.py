import re
def cun_sent(para):
      para = re.sub('([.!?\?])([^"])', r"\1\n\2", para)
      para = re.sub('([.!?\?]["])([^.!?\?])', r'\1\n\2', para)
      para = para.strip()
      return para.split("\n")

def cun_sent_two(para_two):
      para_two = re.sub('([ .!?\?])([^"])', r"\1\n\2", para_two)
      para_two = re.sub('([.!?\?]["])([^.!?\?])', r'\1\n\2', para_two)
      para_two = para_two.strip()
      return para_two.split("\n")

text = ''
file = open('test_2.txt')
for line in file:
      line=line.replace('."','".')
      line=line.replace('!"','"!')
      line=line.replace('?"','"?')
      line=line.strip()
      text = text +line+' '

text=re.sub('[\n:,]','',text)
text=re.split(r'[!.?]',text)
text_temp_1=text
text_temp=[]
for i in range(len(text)):
      text_temp.append(text[i][2:])
      
      
#print(text_temp)
#print(text)
text=text_temp
#for p in range(len(text_two)):
      #text_two[p] = cun_sent_two(text_two[p])
      #for q in range(len(text_two[p])):
            #text_two[p][q] = text_two[p][q].strip( )
#print(text_two)
list = []
for i in text:
      list.append(i)
list.reverse()
text = "".join(list)
Sirs_name = re.findall('(\\b[A-Z][a-z]*\\b)', text)
Sirs_name = set(Sirs_name)
if 'Sir' in Sirs_name:
      Sirs_name.remove('Sir')
if 'I' in Sirs_name:
      Sirs_name.remove('I')
if 'Knave' in Sirs_name:
      Sirs_name.remove('Knave')
if 'Knaves' in Sirs_name:
      Sirs_name.remove('Knaves')
if 'Knight' in Sirs_name:
      Sirs_name.remove('Knight')
if 'All' in Sirs_name:
      Sirs_name.remove('All')
if 'Sirs' in Sirs_name:
      Sirs_name.remove('Sirs')
print(Sirs_name)
ass=[]
for i in Sirs_name:
      ass.append(i)

Sirs_name=ass
number = []
n=len(Sirs_name)
p=2**n
s='0'
for i in range(len(Sirs_name)-1):
      s+='0'
for i in range(p):
      number.append(f'{i:0{len(Sirs_name)}b}')
pattern = re.compile('"(.*)"')

list_one = []
list_two = []
say_name = []
say_in_name = []
other_name = []
temp=[]
ppp=''
text=text_temp_1

for u in range(len(text)):
      temp=[]
      temp1=[]
      t1=''
      t2=''
      judge=0
      text[u] = re.sub('[.!:,]','',text[u])
      text[u] = re.sub('["]',' " ',text[u])
      if '"' not in text[u]:
            continue
      else:

            text[u] = text[u].split()
            for word in text[u]:
                  if word == '"':
                        judge += 1
                        continue
                  if judge == 1:
                        t1+=word+' '
                  if judge == 0:
                        t2 += word+' '
                  if judge == 2:
                        judge = 0
                        continue
      list_one.append(t1)
      list_two.append(t2)
      t1=t1.split()
      t2=t2.split()
      for i in t1:
            if i in Sirs_name:
                  temp.append(i)
      for i in t2:
            if  i in Sirs_name:
                  say_name.append(i)

      for num in range(len(say_name)):

            if 'and I'in list_one[num]:

                  temp.append(str(say_name[len(say_name)-1]))
                  break
                  
      say_in_name.append(temp)
      temp1=[]

      other_name = []
      for line in list_one:
            for i in line:
                  i = i.split()
                  for q in i:
                        print(q)
                        if q in Sirs_name:
                              say_in_name.append(q)


print(111)
print(say_in_name)
print(say_name)
print(other_name)
print(111)
tt={}
def add(ui,i):
      ui=0
      for pp in i:
            ui += int(pp)
      return ui
solution = []
judge=1
def gggg():
      global judge
      global tt
      ui=0
      for i in number:

            for a in range(len(Sirs_name)):
                  tt[Sirs_name[a]] = i[a]
            

            for t in list_one[b]:

                  if 'I' in t and 'am' in t:
                        if 'Knight' in t:
                              solution.append(i)

                        if 'Knave' in t:
                              judge=0
                              return
                  elif 'all' in t or 'All' in t:

                        if 'Knight' in t:

                              if add(ui,i)==len(Sirs_name):
                                    solution.append(i)
                        if 'Knave' in t:

                              if add(ui,i) == 0:
                                    solution.append(i)
                  elif 'at least' in t or 'At least' in t or ' or ' in t:
                        if 'us' in t:
                              if 'Knight' in t:
                                    if tt[say_name[b]] == 1:  # 说话者为1，其余全部加起来大于等于0#
                                          if add(ui,i) >= 1 :
                                                solution.append(i)

                                    if tt[say_name[b]] == 0:  # 说话者为0，这种情况NO SOLUTION#
                                          judge = 0
                                          return

                        if 'us' not in t:
                              if 'Knave' in t:
                                    if tt[say_name[b]] == 1:  # 说话者为1，其余全部加起来小于等于Len(u)-1#
                                          if add(ui, i) <= len(say_in_name[b]):
                                                solution.append(i)
                                                print(333333)
                                    if tt[say_name[b]] == 0:  # 说话者为0，其余全部加起来等于len(u)#
                                          if add(ui, i) == len(say_in_name[b]):
                                                solution.append(i)
                                                print(333333)
                  elif 'At most' in t:
                        if 'us' in t:
                              if 'Knight' in t:
                                    if tt[say_name[b]] == 1:#说话者为1，其余全部为0#
                                          if add(ui, i) == 1:
                                                solution.append(i)
                                    if tt[say_name[b]] == 0:#说话者为0，其余全部加起来小于等于1#
                                          if add(ui, i) <= 1:
                                                solution.append(i)
                              if 'Knave' in t:
                                    if tt[say_name[b]] >= len(other_name[b])-1:  # 说话者为1，其余加起来大于等于len(引号里去除说话人)-2#
                                          if add(ui, i) <= 1:
                                                solution.append(i)
                                    if tt[say_name[b]] <= len(other_name[b]) :  # 说话者为0，其余全部加起来小于等于len(引号里去除说话人)-2#
                                          if add(ui, i) <= 1:
                                                solution.append(i)
                        if 'us' not in t:
                              if 'Knight' in t:
                                    if tt[say_name[b]] == 1:  # 说话者为1，其余全部加起来小于等于1#
                                          if add(ui, i) <= 2:
                                                solution.append(i)
                                    if tt[say_name[b]] == 0:  # 说话者为0，其余全部加起来大于等于2#
                                          if add(ui, i) >= 2:
                                                solution.append(i)
                              if 'Knave' in t:
                                    if tt[say_name[b]] == 1:  # 说话者为1，其余加起来大于等于len(引号里的人数)-1#
                                          if add(ui, i) >= len(say_in_name[b]):
                                                solution.append(i)
                                    if tt[say_name[b]] == 0:  # 说话者为0，其余全部加起来小于等于len(引号里的人数)-2#
                                          if add(ui, i) <= len(say_in_name[b]-2):
                                                solution.append(i)

                  elif 'exactly' in t or 'Exactly' in t:
                        if 'us' in t:
                              if 'Knight' in t:

                                    if tt[say_name[b]] == 1:#说话者为1，其余人都为零#
                                          if add(ui, i) == 1:
                                                print(111111111111111)
                                                solution.append(i)
                                    if tt[say_name[b]] == 0:#说话者为0，其余人加起来大于等于2或者等于0#
                                          if add(ui, i) >= 2 or add(ui, i) == 0:
                                                solution.append(i)
                              if 'Knave' in t:
                                    if tt[say_name[b]] == 1:#说话者为1，其余人加起来等于，也就是==len(Sirs_name)-2#
                                          if add(ui, i) == len(other_name[b]) - 1:
                                                solution.append(i)
                                    if tt[say_name[b]] <= len(other_name[b]) - 2:#说话者为0，其余人加起来小于等于,也就是<=len(Sirs_name)-2#
                                          judge = 0
                        if 'us' not in t:
                              if 'Knight' in t:
                                    if tt[say_name[b]] == 1:#说话者为1，其余加起来合为1#
                                          if add(ui, i) == 2:
                                                solution.append(i)
                                                print(123131312)
                                    if tt[say_name[b]] == 0:#说话者为0，其余加起来#
                                          if add(ui, i) == 0 or add(ui, i) >= 2:
                                                solution.append(i)
                                                print(2122112111112221)
                              if 'Knave' in t:
                                    if tt[say_name[b]] == 1:  # 说话者为1，其余加起来合为1#
                                          if add(ui, i) == 2:
                                                solution.append(i)
                                                print(122121122121121212112)
                                    if tt[say_name[b]] == 0:#说话者为0，其余全为0或者其余加起来大于等于2#
                                          if add(ui, i) == 0 or add(ui, i) >= 2:
                                                solution.append(i)
                                                print(1231231231313123131231231)

                  elif 'Sir' in t and 'and' in t:
                        if 'are Knight' in t:
                              if tt[say_name[b]]==1:
                                    if add(ui, i) == len(Sirs_name):
                                          solution.append(i)
                              elif tt[say_name[b]]== 0:
                                    if add(ui, i) <= len(Sirs_name):
                                          solution.append(i)

                        if 'are Knave' in t:
                              if tt[say_name[b]] == 1:
                                    if add(ui, i) == 0:
                                          solution.append(i)
                              if tt[say_name[b]] == 0:
                                    if add(ui, i) >= 1:
                                          solution.append(i)
                  elif 'Sir' in t:

                        if 'is a Knight' in t:
                              if(add(ui,i))==2:
                                    solution.append(i)
                              if(add(ui,i))==0:
                                    solution.append(i)
                        if 'is a Knaves' in t:
                              if(add(ui,i)==1):
                                    solution.append(i)

print(88888)
print(say_name)
print(say_in_name)
print(other_name)
print(88888)
solution_final=[]

for b in range(len(list_one)):
      if judge==1:
            gggg()
            if solution_final==[]:
                  solution_final=solution
            else:
                  solution_final=set(solution)&set(solution_final)
      else:

            break



print(f'solution have {solution_final}')
if solution==[]:
      print('no solution')
file.close()

