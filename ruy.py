from telebot import types
''' uzbek qismi'''
key=types.InlineKeyboardMarkup(row_width=2)
k1=types.InlineKeyboardButton('Russian 🇷🇺',callback_data='rus')
k2=types.InlineKeyboardButton('Uzbek 🇺🇿',callback_data='uzb')
key.add(k1,k2)

#fanlar ruyxati uzb
f=types.InlineKeyboardMarkup(row_width=1)
f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
f.add(f1,f2,f3)
#fanlar rus
p=types.InlineKeyboardMarkup(row_width=1)
p1=types.InlineKeyboardButton('Математика🧮',callback_data='matem1')
p2=types.InlineKeyboardButton('физика📡',callback_data='fiz1')
p3=types.InlineKeyboardButton('об учебном центре🔰',callback_data='info1')
p.add(p1,p2,p3)
u=types.InlineKeyboardMarkup(row_width=1)
u1=types.InlineKeyboardButton('о курсе математики',callback_data='matinfo1')
u2=types.InlineKeyboardButton('Зарегистрироваться',callback_data='ruyxat_rus')
u3=types.InlineKeyboardButton('🔙назад',callback_data='nazad')
u.add(u1,u2,u3)
y=types.InlineKeyboardMarkup(row_width=1)

y.add(u2,u3)
#matem
m=types.InlineKeyboardMarkup(row_width=1)
m1=types.InlineKeyboardButton('Matematika🧮 kurs haqida🔰',callback_data='matinfo')
m2=types.InlineKeyboardButton('Ro`yxatdan o`tish',callback_data='ruyxat')
m3=types.InlineKeyboardButton('🔙Orqaga',callback_data='orqa')
m.add(m1,m2,m3)
l=types.InlineKeyboardMarkup(row_width=1)
l.add(m2,m3)
d=types.InlineKeyboardMarkup()
d.add(m3)

q=types.InlineKeyboardMarkup(row_width=1)
q1=types.InlineKeyboardButton('Fizika📡 kurs haqida🔰',callback_data='finfo')
q2=types.InlineKeyboardButton('Ro`yxatdan o`tish',callback_data='ruyxat')
q3=types.InlineKeyboardButton('🔙Orqaga',callback_data='orqa')
q.add(q1,q2,q3)

j=types.InlineKeyboardMarkup(row_width=1)
#j1=types.InlineKeyboardButton('Ro`yxatdan o`tish📝',callback_data='ruyxat1')
j2=types.InlineKeyboardButton('🔙Orqaga',callback_data='orqa')
j.add(q2,j2)

i=types.InlineKeyboardMarkup(row_width=1)
i.add(j2)

s=types.InlineKeyboardMarkup(row_width=1)
s1=types.InlineKeyboardButton('O курсе физика',callback_data='fizinforus')
s.add(s1,u2,u3)

h=types.InlineKeyboardMarkup(row_width=1)
h.add(u2,u3)
h4=types.InlineKeyboardMarkup(row_width=1)
h4.add(u3)
knop=types.InlineKeyboardMarkup(row_width=1)
knop.add(u3)
