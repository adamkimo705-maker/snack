import curses 
import random


screen = curses.initscr() # للعمل مع التيرمينال curses هذه الدالة تهيئ مكتبة
curses.curs_set(0) #إخفاء المؤشر =0 , 1=اظهار
screen_height, screen_width = screen.getmaxyx() #الحصول على ارتفاع وعرض الشاشة
window = curses.newwin(screen_height, screen_width, 0, 0) #إنشاء نافذة جديده بالارتفاع والعرض المطلوب تبدأمن النقطة (0,0)
window.keypad(1) #تفعيل أزرار الكيبورد 1=مفعل 0=معطل
window.timeout(100) #تعيين وقت الانتظار قبل الضغط علي زر جديد في الكيبورد =100 ميلي ثانية
#لتحديد موقع بداية الثعبان (الرأس)
snk_x = screen_width // 4 #تحديد موقع البداية بالعرض (1/4) ربع عرض الشاشه   
snk_y = screen_height // 2 #تحديد موقع البداية بالطول (1/2) نصف طول الشاشه
#لتحديد موقع باقي جسد الثعبان
snake = [
    [snk_y, snk_x], # الرأس =[0]f[0]=y,[1]=x
    [snk_y, snk_x - 1], # الجسم =[1]f[0]=y,[1]=x
    [snk_y, snk_x - 2] # الذيل =[2]f[0]=y,[1]=x
]
food = [screen_height // 2, screen_width // 2]#تحديد موقع الوجبة #food[0] = snake_y, food[1] = snake_x
window.addch(food[0], food[1], curses.ACS_PI)#addch = add character in window الشاشه(y, x, character)

key = curses.KEY_RIGHT #تحديد اتجاه الثعبان افتراضياً يمين

while True:
    next_key = window.getch() # الحصول على الضغط على زر الكيبورد
    key = key if next_key == -1 else next_key # إذا لم يتم الضغط على أي زر = (-1) يبقى الاتجاه نفسه
    #or
    #if next_key != -1:
    #    key = next_key
    
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]: # التحقق من الاصطدام رأس الثعبان بالحافة أو بجسم الثعبان
    # snake[0][0] = رأس الثعبان [بالنسبة للطول]
    # snake[0][1] = رأس الثعبان [بالنسبة للعرض]
    # snake[1:] = بقية جسم الثعبان
        curses.endwin()
        quit() #إنهاء البرنامج

    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
         new_food = [
         random.randint(1, screen_height - 1),
         random.randint(1, screen_width - 1)
         ]
         food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
