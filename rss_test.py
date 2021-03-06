import feedparser

#берем список по категории
rss_url = 'https://www.tokyotosho.info/rss.php?filter=1&reversepolarity=1'
#превращаем в удобный для путона вид
rss_data = feedparser.parse(rss_url)

#список подстрок, которые должны быть в названии, обязательно все
check = ['[HorribleSubs]', 'Black Clover']

def checkall(check, new_title):
	for i in range(len(check)):
		if not (check[i] in new_title):
			return False
	return True

#цикл обработки, 150 - количество записей, которое выдает сайт в своем rss
for i in range(len(rss_data['entries'])):
	#берем только названия
	title = rss_data['entries'][i]['title']
	#разбираем строку на отдельные куски
	splited_title = title.split( )
	#задаем разделитель для сборки
	s = " "
	#собираем строчку заново, отрезая лишнее
	new_title = s.join(splited_title[:-1])
	#выдираем номер серии
	episode_number = splited_title[-2:-1]

	#if check in new_title:     #вот тут надо сделать проверку, что ВСЕ элементы списка есть в переменной new_title
	#	print(new_title)
	
	if checkall(check, new_title):
		print(new_title)

	#если вот так захардкодить прям по индексам, то будет нужный результат, но хочется сделать это абстрактно,
	#на случай, если количество элементов изменится
	# if all([check[0] in new_title, check[1] in new_title]):
	#  	print(new_title)
