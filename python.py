import telebot
from telebot import types
import os
from ruy import *


token='1208425210:AAH8kj8cmxCenkar-0vgSBT_g5k8REscCPw'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def quy(ms):
    
	bot.send_message(ms.chat.id,'*Выберите язык/Tilni tanlang*',reply_markup=key,parse_mode='markdown')

@bot.callback_query_handler(func=lambda c: True)
def callback_query(call):
	data=call.data
	'''uzbek qism'''
	if data=='uzb':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	elif data=='matem':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Matematika kursini tanladingiz marhamat kurs bilan tanishib chiqing📜*',reply_markup=m,parse_mode='markdown')
	elif data=='orqa':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*Qaysi fan uchun ruyxatdan utmoqchisiz \nfanni tanlang yoki kurs haqida malumot oling*',reply_markup=f,parse_mode='markdown')
	elif data=='ruyxat':
		#bot.send_message(call.message.chat.id,'*Ro`yxatdan o`tishni to`xtatish uchun `stop` so`zini yozib yuboring*',parse_mode='markdown')
		send=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*👨‍💼ismingizni kiriting: ✍️:\n\n⚠️Eslatma:Ro`yxatga olish boshlandi bekor qilish uchun`stop` so`zini yozib yuboring*',parse_mode='markdown')
		bot.register_next_step_handler(send,ruy1)
	elif data=='matinfo':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Matematika kursimiz 0 dan boshlanadi 3 oy o`rganish qism boladi\n3 oy praktika yani Abiturient,DTM barcha variantlar ishlanadi\nKeyin o`qituvchi bilan birgalikda tahlil qilinadi\nMatematika kursimiz 1 oylik narxi 200.000 so`m*',reply_markup=l,parse_mode='markdown')
	


	elif data=='fiz':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Fizika kursini tanladingiz marhamat kurs bilan tanishib chiqing📜*',reply_markup=q,parse_mode='markdown')

	elif data=='finfo':
		j=types.InlineKeyboardMarkup(row_width=1)
		j1=types.InlineKeyboardButton('Ro`yxatdan o`tish📝',callback_data='ruyxat1')
		j2=types.InlineKeyboardButton('🔙Orqaga',callback_data='orqa')
		j.add(j1,j2)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Fizika kursimiz 0 dan boshlanadi 3 oy o`rganish qism boladi\n3 oy praktika yani Abiturient,DTM barcha variantlar ishlanadi\nKeyin o`qituvchi bilan birgalikda tahlil qilinadi\nFizika kursimiz 1 oylik narxi 200.000 so`m*',reply_markup=j,parse_mode='markdown')
	elif data=='ruyxat1':
		
		sen=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*👨‍💼ismingizni kiriting ✍️:\n\n⚠️Eslatma:Ro`yxatga olish boshlandi bekor qilish uchun`stop` so`zini yozib yuboring:*',parse_mode='markdown')
		bot.register_next_step_handler(sen,ruy4)		
	elif data=='info':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*Great Academy Toshken shahri Bodomzor metro 22-uyda joylashgan\nBizda malakali o`qutuvchilar ishlashashadi o`zlashtrishda qiynalsangiz\nqo`shimcha dars berida bu bepul kurs davomiyligi 6 oy dan\n\n📍Mo`ljal: Bodomzor metro*',reply_markup=i,parse_mode='markdown')
	elif data=='rus':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Учебный центр Великой академии Ассаламу алейкум \nДобро пожаловать к официальному боту Для получения дополнительной информации обо всех наших курсах \nnВы можете зарегистрироваться на курс*',reply_markup=p,parse_mode='markdown')
	elif data=='matem1':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Если вы выбрали курс математики, прочтите, пожалуйста, курс курс*',reply_markup=u,parse_mode='markdown')
	elif data=='matinfo1':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*💟Наш курс математики начинается с 0 3 месяца обучения будет частью 3 месяца практики, т.е. Abiturient, DTM, все варианты будут разработаны Затем проанализированы вместе с учителем Наш курс математики будет стоить 200 000 сумов в месяц*',parse_mode='markdown',reply_markup=y)






''' matematika qismi funksiyalari'''
def ruy1(ms):

	if ms.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(ms.chat.id,'*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	
	else :
		suz=ms.text
		f=open('{}M.txt'.format(ms.from_user.first_name),'a')
		f.write('1.Ism famlyasi: {}\n'.format(suz))
		f.close()
		s=bot.send_message(ms.chat.id,'*🏠Manzilingizni kiriting ✍️:*',parse_mode='markdown')
		bot.register_next_step_handler(s,ruy2)
	#else:
	#	bot.send_message(ms.chat.id,'*Malumot kiritishda shartlarga qarang hech qanday ortiqcha raqam yoki smile ishlatmang!\nBoshqattan ro`yxattan o`ting*',parse_mode='markdown',reply_markup=l)
def ruy2(ms):
	if ms.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(ms.chat.id,'*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	else:
		suz1=ms.text
		j=open('{}M.txt'.format(ms.from_user.first_name),'a')
		j.write('2.Manzili: {}\n'.format(suz1))
		j.close()
		t=bot.send_message(ms.chat.id,'*☎️Telefon raqamingizni kiriting ✍️:*',parse_mode='markdown')
		bot.register_next_step_handler(t,ruy3)
def ruy3(ms):
	if ms.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(ms.chat.id,'*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	else:
		suz2=ms.text
		suz3=ms.from_user.username
		q=open('{}M.txt'.format(ms.from_user.first_name),'a')
		q.write('3.Telefon: {}\n'.format(suz2))
		q.write('4.Telegram manzili: @{}\n'.format(suz3))
		q.write('5.Kurs nomi: Matematika')
		q.close()
		e=open('{}M.txt'.format(ms.from_user.first_name),'r')
		bot.send_document(1089169019,e)
		e.close()
		os.remove('{}M.txt'.format(ms.from_user.first_name))
		bot.send_message(ms.chat.id,'*Ro`yxatdan o`tish muvafaqiyatli yakunlandi✅*',reply_markup=d,parse_mode='markdown')
'''fizika ruyxatdan utish'''

def ruy4(msg):
	suz1=msg.text
	if suz1=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(msg.chat.id,'*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	

	else:
		g=open('{}.txt'.format(msg.from_user.first_name),'a')
		g.write('1.Ism famlyasi: {}\n'.format(suz1))
		g.close()
		y=bot.send_message(msg.chat.id,'*🏠Manzilingizni kiriting ✍️*:',parse_mode='markdown')
		bot.register_next_step_handler(y,ruy5)
	#else:
	#	bot.send_message(msg.chat.id,'*Malumot kiritishda shartlarga qarang hech qanday ortiqcha raqam yoki smile ishlatmang!\nBoshqattan ro`yxattan o`ting*',parse_mode='markdown',reply_markup=j)


def ruy5(msg):
	if msg.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(msg.chat.id,'*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	else:

		suz1=msg.text
		j=open('{}.txt'.format(msg.from_user.first_name),'a')
		j.write('2.Manzili: {}\n'.format(suz1))
		j.close()
		t1=bot.send_message(msg.chat.id,'*☎️Telefon raqamingizni kiriting ✍️:*',parse_mode='markdown')
		bot.register_next_step_handler(t1,ruy6)



def ruy6(msg):
	if msg.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(ms.chat.id,'*💟Assalomu alaykum Great Academy o`quv markazi\nrasmiy botiga xush kelibsiz bot orqali barcha kurslarimmiz\nhaqida malumot va kurs uchun\nRo`yxatdan o`tishingiz mumkin*',reply_markup=f,parse_mode='markdown')
	else:

		suz2=msg.text
		suz3=msg.from_user.username
		q=open('{}.txt'.format(msg.from_user.first_name),'a')
		q.write('3.Telefon: {}\n'.format(suz2))
		q.write('4.Telegram manzili: @{}\n'.format(suz3))
		q.write('5.Kurs nomi: Fizika')
		q.close()
		e=open('{}.txt'.format(msg.from_user.first_name),'r')
		bot.send_document(1089169019,e)
		e.close()
		os.remove('{}.txt'.format(msg.from_user.first_name))
		bot.send_message(msg.chat.id,'*Ro`yxatdan o`tish muvafaqiyatli yakunlandi✅*',reply_markup=d,parse_mode='markdown')





bot.polling()
