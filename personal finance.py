import time
import calendar
import os
import shutil
from text_to_pdf_convertor import text_to_pdf
def texpense():
    a=[]
    print("\n!!!press enter twice when completed!!!\n")
    for i in range(100000):
         k=input(f"{i+1}th expense: ")
         if(k==""):
            break
         
         z=int(k.split(" ")[0]) #for providing error when you dont provide int value first
         a.append(k)
        
    return a

def calculate(b):
    e=0
    d=0
    for i in range(len(b)):
       d = int(b[i].split(" ")[0])
       e=e+d
    return e

def store(f,k,x):

   l=open(k,'a')
   if x!=4:
        g=time.strftime("%d")
        c=calendar.month_name[int(time.strftime("%m"))]
        y=time.strftime("%Y")
        l.write(f"\n{g}-{c}-{y}:\n")
   else:
       x=input("date for which you have to add the expense(d-m-y): ")
       l.write(f"\n{x}:\n")

   for i in range(len(f)):
        l.write(f"{i+1}. {f[i]}\n")
   l.close

def store_t(a,k):
    f=open(k,"a")
    f.write(f"{a}\n")
    f.close

def store_amount(amount,a):
    file2=open('amount.txt','w')
    file2.write(f'{int(amount)-a}')
    file2.close()

def read(k):
    f=open(k,'r')
    sum=0
    line=0
    while True:
        line=f.readline()
        if not line:
            break
        sum=sum+int(line)
    f.close()
    return sum

def overview(a,k,amount,today_kharcha):
    if k==1 or k==4:
        print(f"total expense for this month = {a}")
        print(f"total money left(parents) = {int(amount)-today_kharcha}")
    else:
        print(f"total extra amount you have is : {a}\n")

def newfile_generator(file):
    month=int(time.strftime("%m"))
    a=f"{calendar.month_name[month]}_{file}"
    f=open(a,"w")
    f.close
    return a

# def file_manager():
#     a=f"{calendar.month_name[month-1]}_hisab.txt"
#     b=f"{calendar.month_name[month-1]}_kharcha.txt"
#     c=f"{calendar.month_name[month-1]}_amount.txt"
    
#     if os.path.exists(a):
#         shutil.move(a,f'previous month hisab/{a}')
#         shutil.move(b,f'previous month hisab/{b}')
#         shutil.move(c,f'previous month hisab/{c}')

def file_manager():
    a=f"{calendar.month_name[month-1]}_hisab.txt"
    a1=f"{calendar.month_name[month-1]}_hisab.pdf"                                   
    os.remove(a)
    a_o=text_to_pdf(a,a1)

    b=f"{calendar.month_name[month-1]}_kharcha.txt"
    c=f"{calendar.month_name[month-1]}_amount.txt"


def month_initition():
    b=newfile_generator("kharcha.txt")
    a=newfile_generator("hisab.txt")
    c=newfile_generator("amount.txt")
    

    l=open("current_files.txt",'w')
    l.write(f"{a} {b} {c}")
    l.close
    
    file_manager()

def backup():
    if os.path.exists('backup/amount_backup.txt'):
        os.remove('backup/amount_backup.txt')
    shutil.copy('amount.txt','backup/amount_backup.txt')
    


while True:
    month=int(time.strftime("%m"))
    file_name=f"{calendar.month_name[month]}_{'hisab.txt'}"
    if(os.path.exists(file_name)):
        None
    else:
        month_initition()

    f=open("current_files.txt",'r')
    list1=f.read().split(" ")
    a=list1[0]

    b=list1[1]

    c=list1[2]
    if os.path.exists('amount.txt')==False:
        f11=open("amount.txt",'x')
        f11.close()

    f=open("amount.txt",'r')

    amount=f.readline()
    f.close

    x=int(input("press 1: daily expense\npress 2: extra money hisab(use '+' '-' for showing transaction)\npress 3: checking current status\npress 4:adding expense for previous dates\npress 5: mom dad hisab\npress 6:exit\n"))
    backup()

    if x==6:
        break
    if x==5:
        expense=texpense()
        store(expense,c,x)
        today_kharcha=calculate(expense)
        total=read('amount.txt')
        file1=open('amount.txt','w')
        file1.write(f'{total+today_kharcha}')
        file1.close()
    else:
        if x!=3:
            expense=texpense()
            store(expense,a,x) if x==1 or x==4 else store(expense,"extramoney_hisab.txt",x) 
            today_kharcha=calculate(expense)
            store_t(today_kharcha,b) if x==1 or x==4 else store_t(today_kharcha,"extra_kharcha.txt")
            total= (read(b) if x==1 or x==4 else read("extra_kharcha.txt"))
            if x==1 or x==4:
                store_amount(amount,today_kharcha)  
            overview(total,x,amount,today_kharcha)
        else:
            total= read(b)
            total1=read("extra_kharcha.txt")
            overview(total,1,amount,0)
            overview(total1,2,amount,0)
            z=int(input("press 1: daily hisab record\npress 2:extra money record\npress 3: exit\n"))
            os.startfile(a) if z==1 else os.startfile("extramoney_hisab.txt") if z==2 else print("THANKS")


