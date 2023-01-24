#下载对应chrome的webdriver，叫做chromedriver（版本要选对）
#下载对应系统和版本的miniconda，右下角切换python的interpreter到这个conda(base)
#kernel输入 pip install selenium

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\chromedriver_win322\chromedriver.exe') 

def login():  
    #用来登录进studentlink的选课界面
    
    driver.get('https://www.bu.edu/link/bin/uiscgi_studentlink.pl/')
    #进studentlink网页
    
    driver.find_element('xpath','/html/body/center[1]/table[4]/tbody/tr/td[1]/table/tbody/tr[1]/td/a/img').click()
    driver.find_element('xpath','/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/font/a[8]').click()
    #点击academics以及registration

    driver.find_element('id','j_username').send_keys('yubo@bu.edu')
    driver.find_element('id','j_password').send_keys('QYbb20011023')
    #在登录界面 输入用户名和密码

    driver.find_element('xpath','//*[@id="wrapper"]/div/form/button').click()
    #点击登录按钮
    
    #sleep(15) 

#点击push （目前无法完成）
    #driver.find_element('xpath','/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]').click()
    
    print('\n'+'-----------------------------------'+'\n')
    print('Waiting for you to push ~') 
    while True:
        try: 
            if driver.find_element('xpath','/html/body/table[3]/tbody/tr[1]/th[1]'):
                print('\n'+'Thank you for your effort !!!')
                break
        except:
            pass 
    

def Goal(): 
    goal = ''
    print('\n'+'-----------------------------------'+'\n')
    print('Option List:'+'\n')
    print('1: [ Forestalling ]'+'\n'+'2: [ Waitting for someone to drop ]'+'\n'+'3: [ Quit ]'+'\n')
    
    while not (goal == '1' or goal == '2' or goal == '3'):
        goal = input("(Please enter 1, 2, or 3): ")
        if goal == '1':
            Plan()
            #选择抢课，然后接着要问planner的事
            break
        elif goal == '2':
            Wait()
            #选择蹲课，然后开始问课程信息
            break
        elif goal == '3':
            Quit()
            #选择退出程序
            break
        else:
            print('\n'+'Please enter a valid answer!'+'\n')
    
            
def Plan():
    plan = ''
    print('\n'+'-----------------------------------'+'\n')
    print('Are you done with the planner?'+'\n')
    print('1: [ Yes, I am ready to take courses ]'+'\n'+'2: [ No, the planner is incompleted ]'+'\n'+'3: [ Quit ]'+'\n')
    
    while not (plan == '1' or plan == '2' or plan == '3'):
        plan = input("(Please enter 1, 2, or 3): ")
        if plan == '1':
            Take()
            #planner已经完成了，立刻抢课！
            break
        elif plan == '2':
            Notplan()
            #planner尚未完成，先去planner排课
            break
        elif plan == '3':
            Quit()
            #选择退出程序
            break
        else:
            print('\n'+'Please enter a valid answer!'+'\n')
            
def Quit():
    print('\n'+'-----------------------------------'+'\n')
    print('Thanks for using, have a great day!')
    return        
    
def Wait():
    col = ''
    dep = ''
    cor = ''
    sec = ''
    print('\n'+'-----------------------------------'+'\n')
    col = input("Which college does the course you want belong to? \n\n"+"(eg: if you want CAS CS 111 A1, CAS would be the college): ")
    dep = input("\n"+"Which department does the course you want belong to? \n\n"+"(eg: if you want CAS CS 111 A1, CS would be the department): ")
    cor = input("\n"+"What is the course number of the course you want? \n\n"+"(eg: if you want CAS CS 111 A1, 111 would be the course number): ")
    sec = input("\n"+"Which section of the course do you want? \n\n"+"(eg: if you want CAS CS 111 A1,  A1 would be the section): ")
    a = ''
    print('\n'+'-----------------------------------'+'\n')
    print("Is [ "+col+' '+dep+' '+cor+' '+sec+' ] the course you want?'+"\n")
    print('1: [ Yes ]'+'\n'+'2: [ No, try again ]'+'\n'+'3: [ Quit ]'+'\n')
    
    while not (a == '1' or a == '2' or a == '3'):
        plan = input("(Please enter 1, 2, or 3): ")
        if plan == '1':
            Dun(col, dep, cor, sec)
            #写对了！蹲课去
            break
        elif plan == '2':
            Wait()
            #写错了，再输入一遍
            break
        elif plan == '3':
            Quit()
            #选择退出程序
            break
        else:
            print('\n'+'Please enter a valid answer!'+'\n')
            
def Dun(col, dep, cor, sec):
    driver.find_element('xpath','/html/body/center[1]/table[2]/tbody/tr[3]/td[2]/a').click()
    driver.find_element('xpath','/html/body/table[4]/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td[1]/select').click()
    driver.find_element('xpath','/html/body/table[4]/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td[1]/select/option[3]').click()
    driver.find_element('name','Dept').send_keys('CS')
    driver.find_element('name','Course').send_keys('111')
    driver.find_element('name','Section').send_keys('A1')
    driver.find_element('xpath','/html/body/table[4]/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td[6]/input').click()
    #随便选一门课进到选课界面，然后再找指定的课
    driver.find_element('name','College').send_keys(col)
    driver.find_element('name','Dept').send_keys(dep)
    driver.find_element('name','Course').send_keys(cor)
    driver.find_element('name','Section').send_keys(sec)
    driver.find_element('xpath', '/html/body/form/center[2]/table/tbody/tr/td[2]/input').click()
    
    if sec == 'A1':
        box = '/html/body/form/table[1]/tbody/tr[3]/td[1]/input'
        flag = '/html/body/form/table[1]/tbody/tr[3]/td[1]/a/img'
    else:
        box = '/html/body/form/table[1]/tbody/tr[2]/td[1]/input'
        flag = '/html/body/form/table[1]/tbody/tr[2]/td[1]/a/img'
        
    if len(driver.find_elements('partial link text', col+' '+dep+cor+' '+sec)) == 0:
        return Notfind(col, dep, cor, sec)
    else: 
        pass
    
    print('\n'+'-----------------------------------'+'\n')
    print('We have found the course, we will add it when it has an open seat!'+'\n')
    
    while True:
        if len(driver.find_elements('xpath', box)) == 0:
            #找不到点击位置，说明没空位
            driver.find_element('xpath', flag).click()
            sleep(10)
            driver.find_element('xpath','/html/body/table[2]/tbody/tr/td[2]/font[1]/a').click()
            #点回去,back
        else:
            if len(driver.find_elements('xpath', "//*[text()[contains(.,'ADD CLASSES')]]")) == 1:
                #双重保险，证明这个课能点上
                print('Open seat !!!')
                break           
            
    #len(driver.find_elements('xpath', "//*[text()[contains(.,'WHY CLASS IS BLOCKED')]]")) == 0:

def Take():
    return

def Notplan():
    #既然planner还没弄好，那就现场排课
    #/html/body/form/table[1]/tbody/tr[3]/td[12]
    #就只有tr[]有改变,换section,tr变，换ending time或者看星期几，td换
    return

def Notfind(col, dep, cor, sec):
    driver.find_element('xpath','/html/body/table[2]/tbody/tr/td[2]/a').click()
    a = ''
    print('\n'+'-----------------------------------'+'\n')
    print('Sorry, we could not find'+' [ '+col+' '+dep+' '+cor+' '+sec+' ]'+'\n')
    print('Do you want to try another course?'+'\n')
    print('1: [ Yes ]'+'\n'+'2: [ No, I will quit for now ]'+'\n')
    
    while not (a == '1' or a == '2'):
        a = input("(Please enter 1 or 2): ")
        if a == '1':
            Wait()
            #再接着去选课号，然后蹲课！
            break
        elif a == '2':
            Quit()
            #选择退出程序
            break
        else:
            print('\n'+'Please enter a valid answer!'+'\n')
            
def Start():
    sem = ''
    year = ''
    print('\n'+'-----------------------------------'+'\n')
    sem = input("Which semester do you register for? \n\n"+"(eg: if you register for Spring 2023, Spring would be the semester): ")
    year = input("\n"+"Which year do you register for? \n\n"+"(eg: if you register for Spring 2023, 2023 would be the semester): ")
    
    a = ''
    print('\n'+'-----------------------------------'+'\n')
    print("Is [ "+sem+' '+year+' ] the semester and year you register for?'+"\n")
    print('1: [ Yes ]'+'\n'+'2: [ No, try again ]'+'\n'+'3: [ Quit ]'+'\n')
    
    while not (a == '1' or a == '2' or a == '3'):
        choice = input("(Please enter 1, 2, or 3): ")
        if choice == '1':
            Reg(sem, year)
            #写对了！找对应的reg option
            break
        elif choice == '2':
            Start()
            #写错了，再输入一遍
            break
        elif choice == '3':
            Quit()
            #选择退出程序
            break
        else:
            print('\n'+'Please enter a valid answer!'+'\n')
    
def Reg(sem, year):    
    a = driver.find_elements('partial link text','Reg')
    bad = 0
    while bad != len(a):
        #assume 至少会有一个reg option，有时是两个
        a[bad].click()
        find = driver.find_elements('xpath', "//*[text()[contains(.,"+"'"+sem+' '+year+"'"+")]]") 
        #点开其中一个，找字眼
        if len(find) == 1:
            #找到对的reg option
            Goal()
            break
        else:
            #找的不对，只有两种情况
            bad += 1
            if bad >= len(a):
                print('\n'+'-----------------------------------'+'\n')
                print('Sorry, we could not find the corresponding semester and year'+'\n'+'Let us try again!')
                driver.find_element('xpath','/html/body/table[1]/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/a/img').click()
                driver.find_element('xpath','/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/font/a[8]').click()
                Start()
                #实在找不到，就重新输入
            else:
                driver.find_element('xpath','/html/body/table[1]/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/a/img').click()
                driver.find_element('xpath','/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/font/a[8]').click()
                #找的不对，但是还有别的reg option没有看过，就退出去点另外的

    
if __name__ == '__main__':
    login()
    Start()
    #a = driver.find_elements('text','Spring 2023')
    #a = driver.find_elements('xpath', "//*[text()[contains(.,'Fall')]]")      
        #By.xpath("//*[text()[contains(.,'foobar')]]")
        #/html/body/table[1]/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/a/img  /html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/font/a[8]
    # /html/body/center[1]/table[1]/tbody/tr/td[1]

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    