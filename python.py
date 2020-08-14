import telebot
from telebot import types
import os
from ruy import *
from manba import *


token='985403265:AAFSOSsxtLT2FEC_Hq37mrgmRyxIWydSd4Q'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def quy(ms):
	#bot.send_message(ms.chat.id,ms.from_user.id)
	bot.send_message(ms.chat.id,'*Выберите язык/Tilni tanlang*',reply_markup=key,parse_mode='markdown')

@bot.callback_query_handler(func=lambda c: True)
def callback_query(call):
	data=call.data
	'''uzbek qism'''
	if data=='uzb':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=bosh_qism,reply_markup=f,parse_mode='markdown')
	elif data=='matem':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=matematika_bolim,reply_markup=m,parse_mode='markdown')
	elif data=='orqa':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*Qaysi fan uchun ruyxatdan utmoqchisiz \nfanni tanlang yoki kurs haqida malumot oling*',reply_markup=f,parse_mode='markdown')
	elif data=='ruyxat':
		#bot.send_message(call.message.chat.id,'*Ro`yxatdan o`tishni to`xtatish uchun `stop` so`zini yozib yuboring*',parse_mode='markdown')
		send=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*👨‍💼ismingizni kiriting: ✍️:\n\n⚠️Eslatma:Ro`yxatga olish boshlandi bekor qilish uchun`stop` so`zini yozib yuboring*',parse_mode='markdown')
		bot.register_next_step_handler(send,ruy1)
	elif data=='matinfo':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=matematika_info,reply_markup=l,parse_mode='markdown')
	


	elif data=='fiz':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=fizika_bolim,reply_markup=q,parse_mode='markdown')

	elif data=='finfo':
		j=types.InlineKeyboardMarkup(row_width=1)
		q2=types.InlineKeyboardButton('Ro`yxatdan o`tish',callback_data='ruyxat')
		j2=types.InlineKeyboardButton('🔙Orqaga',callback_data='orqa')
		j.add(q2,j2)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=fizika_info,reply_markup=j,parse_mode='markdown')
	elif data=='info':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=info,reply_markup=i,parse_mode='markdown')
	elif data=='rus':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=bosh_qism_rus,reply_markup=p,parse_mode='markdown')
	elif data=='matem1':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=matematika_bolim_rus,reply_markup=u,parse_mode='markdown')
	elif data=='matinfo1':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=matem_info_rus,parse_mode='markdown',reply_markup=y)

	elif data=='nazad':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=bosh_qism_rus,reply_markup=p,parse_mode='markdown')
	elif data=='fiz1':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=fizika_bolim_rus,parse_mode='markdown',reply_markup=s)
	elif data=='fizinforus':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=fizika_info_rus,reply_markup=h,parse_mode='markdown')
	elif data=='info1':
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=info_rus,reply_markup=h4,parse_mode='markdown')
	elif data=='ruyxat_rus':
		smil=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*введите ваше имя \n\n⚠️Примечание: введите слово «стоп», чтобы отменить регистрацию.*',parse_mode='markdown')
		bot.register_next_step_handler(smil,ruy5)

def ruy5(msg):
	if msg.text=='стоп':
		bot.send_message(msg.chat.id,bosh_qism_rus,reply_markup=p,parse_mode='markdown')
	else:
		ful=msg.text
		ruyxat=open('{}Rus.txt'.format(msg.from_user.first_name),'a')
		ruyxat.write('1.Ism Familyasi: {}\n'.format(ful))
		ruyxat.close()

		yubor=bot.send_message(msg.chat.id,'*🏠Введите свой адрес ✍️:*',parse_mode='markdown')
		bot.register_next_step_handler(yubor,ruy6)
def ruy6(msg):

	if msg.text=='стоп':
		bot.send_message(msg.chat.id,bosh_qism_rus,reply_markup=p,parse_mode='markdown')
	else:
		suz5=msg.text
		ful=open('{}Rus.txt'.format(msg.from_user.first_name),'a')
		ful.write('2.Manzili: {}\n'.format(suz5))
		ful.close()
		yubo2=bot.send_message(msg.chat.id,'*☎️ Введите свой номер телефона ✍️:*',parse_mode='markdown')
		bot.register_next_step_handler(yubo2,ruy7)
def ruy7(msg):
	if msg.text=='стоп':
		bot.send_message(msg.chat.id,bosh_qism_rus,reply_markup=p,parse_mode='markdown')
	else:
		suz7=msg.text
		ful=open('{}Rus.txt'.format(msg.from_user.first_name),'a')
		ful.write('3.Telefon raqami:{}\n'.format(suz7))
		ful.close()
		yubor4=bot.send_message(msg.chat.id,'*введите название курса📓:*',parse_mode='markdown')
		bot.register_next_step_handler(yubor4,ruy8)
def ruy8(msg):
	if msg.text=='стоп':
		bot.send_message(msg.chat.id,bosh_qism_rus,reply_markup=p,parse_mode='markdown')
	else:
		suz8=msg.text
		user=msg.from_user.username
		ful=open('{}Rus.txt'.format(msg.from_user.first_name),'a')
		ful.write('4.Telegram manzili: @{}\n'.format(user))
		ful.write('5.Kurs nomi: {}'.format(suz8))
		ful.close()
		sendi=open('{}Rus.txt'.format(msg.from_user.first_name),'r')
		bot.send_document(1089169019,sendi)
		sendi.close()
		os.remove('{}Rus.txt'.format(msg.from_user.first_name))
		bot.send_message(msg.chat.id,'* Регистрация успешно завершена✅*',reply_markup=knop,parse_mode='markdown')









''' matematika qismi funksiyalari'''
def ruy1(ms):

	if ms.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(ms.chat.id,bosh_qism,reply_markup=f,parse_mode='markdown')
	
	else :
		suzlar=ms.text
		farmat=open('{}.txt'.format(ms.from_user.first_name),'a')
		farmat.write('1.Ism famlyasi: {}\n'.format(suzlar))
		farmat.close()
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
		bot.send_message(ms.chat.id,bosh_qism,reply_markup=f,parse_mode='markdown')
	else:
		suz1=ms.text
		j=open('{}.txt'.format(ms.from_user.first_name),'a')
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
		bot.send_message(ms.chat.id,bosh_qism,reply_markup=f,parse_mode='markdown')
	else:
		suz2=ms.text
		suz3=ms.from_user.username
		q=open('{}.txt'.format(ms.from_user.first_name),'a')
		q.write('3.Telefon: {}\n'.format(suz2))
		q.write('4.Telegram manzili: @{}\n'.format(suz3))
		
		q.close()
		yu=bot.send_message(ms.chat.id,'*Kurs nomini yozing✍️📎:*',parse_mode='markdown')
		bot.register_next_step_handler(yu,ruy4)
def ruy4(ms):
	if ms.text=='stop':
		f=types.InlineKeyboardMarkup(row_width=1)
		f1=types.InlineKeyboardButton('Matematika🧮',callback_data='matem')
		f2=types.InlineKeyboardButton('Fizika📡',callback_data='fiz')
		f3=types.InlineKeyboardButton('O`quv markaz haqida🔰',callback_data='info')
		f.add(f1,f2,f3)
		bot.send_message(ms.chat.id,bosh_qism,reply_markup=f,parse_mode='markdown')
	else:
		
		suz3=ms.text
		fayl=open('{}.txt'.format(ms.from_user.first_name),'a')
		fayl.write('5.Kurs nomi: {}'.format(suz3))
		fayl.close()
		h=open('{}.txt'.format(ms.from_user.first_name),'r')
		bot.send_document(1089169019,h)
		h.close()
		os.remove('{}.txt'.format(ms.from_user.first_name))
		bot.send_message(ms.chat.id,'*Ro`yxatdan o`tish muvafaqiyatli yakunlandi✅*',reply_markup=d,parse_mode='markdown')
		
























bot.polling()
