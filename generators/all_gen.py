from random import choice, randint, shuffle
import os
import cv2
import sqlite3

from datetime_gen import get_datetime


class Product:
	def __init__(self, id, name, category, color, cost, description, image, displayed, in_stock, on_sale, discount):
		self.id = id
		self.name = name
		self.category = category
		self.color = color
		self.cost = cost
		self.description = description
		self.image = image
		self.displayed = displayed
		self.in_stock = in_stock
		self.on_sale = on_sale
		self.discount = discount


class FeatureSet:
	def __init__(self, id, product, feature_variant):
		self.id = id
		self.product = product
		self.feature_variant = feature_variant


class User:
	def __init__(self, id, password, last_login, email, is_active, is_admin):
		self.id =id
		self.password = password
		self.last_login = last_login
		self.email = email
		self.is_active = is_active
		self.is_admin = is_admin


class Profile:
	def __init__(self, id, name, user_id, loyalty_card_id):
		self.id = id
		self.name = name
		self.user_id = user_id
		self.loyalty_card_id = loyalty_card_id


class Cart:
	def __init__(self, id, user):
		self.id = id
		self.user = user


def get_name_pool(filename):
	names = []

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			word = line[:-1]
			names.append(word.lower())

	return names


names = get_name_pool('swe_nouns.txt')
shuffle(names)
color_d = {
	1: 2,
	2: 8,
	3: 9,
	4: 1,
	5: 3,
	6: 4,
	7: 10,
	8: 5,
	9: 11,
	10: 7,
	11: 12
}
products = []
feature_sets = []
users = []
profiles = []
carts = []


def bed_generator(first_prod_id, first_set_id, n):
	images = [f for f in os.listdir(os.path.join('images', 'beds'))]
	img_len = len(images)

	bed_var_d = {
		1 : 1,
		2 : 2,
		3 : 3,
		4 : 4,
		5 : 5
	}

	for id in range(first_prod_id, first_prod_id + n, 1):
		image_f = images[id % img_len]
		color = image_f[0:image_f.find('-')]
		var = image_f[len(color) + 1:image_f[len(color) + 1:].find('-') + len(color) + 1]

		if randint(0, 100) > 94:
			in_stock = 0
		else:
			in_stock = 1
		if in_stock:
			if randint(0, 100) > 70:
				on_sale = 1
				discount = int(randint(1, 3) * 10)
			else:
				on_sale = 0
				discount = 0
		else:
			on_sale = 0
			discount = 0

		image_name = str(randint(0, 1000000)) + '_' + image_f
		img = cv2.imread(os.path.join('images', 'beds', image_f))
		base = os.path.split(os.getcwd())[0]
		cv2.imwrite(os.path.join(base, 'furniture_store', 'media', 'product_pics', image_name), img)

		product = Product(
			id=id,
			name=names[id % len(names)],
			category=1,
			color=color_d[int(color)],
			cost=int(randint(10, 30) * 1000 - 1),
			description="",
			image='product_pics/' + image_name,
			displayed=1,
			in_stock=in_stock,
			on_sale=on_sale,
			discount=discount
		)
		products.append(product)

		feature_set = FeatureSet(
			id=first_set_id,
			product=id,
			feature_variant=bed_var_d[int(var)]
		)
		first_set_id += 1
		feature_sets.append(feature_set)

	return first_prod_id + n, first_set_id


def chair_generator(first_prod_id, first_set_id, n):
	shuffle(names)
	images = [f for f in os.listdir(os.path.join('images', 'chairs'))]
	img_len = len(images)

	var_d = {
		1: 6,
		2: 7,
		3: 8,
		4: 9,
	}

	for id in range(first_prod_id, first_prod_id + n, 1):
		image_f = images[id % img_len]
		color = image_f[0:image_f.find('-')]
		var = image_f[len(color) + 1:image_f[len(color) + 1:].find('-') + len(color) + 1]

		if randint(0, 100) > 94:
			in_stock = 0
		else:
			in_stock = 1
		if in_stock:
			if randint(0, 100) > 70:
				on_sale = 1
				discount = int(randint(1, 3) * 10)
			else:
				on_sale = 0
				discount = 0
		else:
			on_sale = 0
			discount = 0

		image_name = str(randint(0, 1000000)) + '_' + image_f
		img = cv2.imread(os.path.join('images', 'chairs', image_f))
		base = os.path.split(os.getcwd())[0]
		cv2.imwrite(os.path.join(base, 'furniture_store', 'media', 'product_pics', image_name), img)

		product = Product(
			id=id,
			name=names[id % len(names)],
			category=2,
			color=color_d[int(color)],
			cost=int(randint(40, 150) * 100 - 1),
			description="",
			image='product_pics/' + image_name,
			displayed=1,
			in_stock=in_stock,
			on_sale=on_sale,
			discount=discount
		)
		products.append(product)

		feature_set = FeatureSet(
			id=first_set_id,
			product=id,
			feature_variant=var_d[int(var)]
		)
		first_set_id += 1
		feature_sets.append(feature_set)

	return first_prod_id + n, first_set_id


def table_generator(first_prod_id, first_set_id, n):
	shuffle(names)
	images = [f for f in os.listdir(os.path.join('images', 'tables'))]
	img_len = len(images)

	var_d = {
		1: 11,
		2: 12,
		3: 13
	}

	for id in range(first_prod_id, first_prod_id + n, 1):
		image_f = images[id % img_len]
		color = image_f[0:image_f.find('-')]
		var = image_f[len(color) + 1:image_f[len(color) + 1:].find('-') + len(color) + 1]

		if randint(0, 100) > 94:
			in_stock = 0
		else:
			in_stock = 1
		if in_stock:
			if randint(0, 100) > 70:
				on_sale = 1
				discount = int(randint(1, 3) * 10)
			else:
				on_sale = 0
				discount = 0
		else:
			on_sale = 0
			discount = 0

		image_name = str(randint(0, 1000000)) + '_' + image_f
		img = cv2.imread(os.path.join('images', 'tables', image_f))
		base = os.path.split(os.getcwd())[0]
		cv2.imwrite(os.path.join(base, 'furniture_store', 'media', 'product_pics', image_name), img)

		product = Product(
			id=id,
			name=names[id % len(names)],
			category=3,
			color=color_d[int(color)],
			cost=int(randint(80, 220) * 100 - 1),
			description="",
			image='product_pics/' + image_name,
			displayed=1,
			in_stock=in_stock,
			on_sale=on_sale,
			discount=discount
		)
		products.append(product)

		feature_set = FeatureSet(
			id=first_set_id,
			product=id,
			feature_variant=var_d[int(var)]
		)
		first_set_id += 1
		feature_sets.append(feature_set)

	return first_prod_id + n, first_set_id


# зеркальные(да, нет)
# назначение(Гардероб, Купе, Детский)
# угловой(да, нет)
# [цвет]-[0,1]-[1(гард), 2(купе), 3(детск)]-[0,1]
def closet_generator(first_prod_id, first_set_id, n):
	shuffle(names)
	images = [f for f in os.listdir(os.path.join('images', 'closets'))]
	img_len = len(images)

	mir_d = {
		0: 17,
		1: 16
	}

	cat_d = {
		1: 22,
		2: 23,
		3: 24
	}

	ang_d = {
		0: 20,
		1: 19
	}

	for id in range(first_prod_id, first_prod_id + n, 1):
		image_f = images[id % img_len]
		color, mirror, cat, angle = image_f.split('-')[:-1]

		if randint(0, 100) > 94:
			in_stock = 0
		else:
			in_stock = 1
		if in_stock:
			if randint(0, 100) > 70:
				on_sale = 1
				discount = int(randint(1, 3) * 10)
			else:
				on_sale = 0
				discount = 0
		else:
			on_sale = 0
			discount = 0

		image_name = str(randint(0, 1000000)) + '_' + image_f
		img = cv2.imread(os.path.join('images', 'closets', image_f))
		base = os.path.split(os.getcwd())[0]
		cv2.imwrite(os.path.join(base, 'furniture_store', 'media', 'product_pics', image_name), img)

		product = Product(
			id=id,
			name=names[id % len(names)],
			category=4,
			color=color_d[int(color)],
			cost=int(randint(10, 67) * 1000 - 1),
			description="",
			image='product_pics/' + image_name,
			displayed=1,
			in_stock=in_stock,
			on_sale=on_sale,
			discount=discount
		)
		products.append(product)

		feature_set = FeatureSet(
			id=first_set_id,
			product=id,
			feature_variant=mir_d[int(mirror)]
		)
		feature_sets.append(feature_set)
		feature_set = FeatureSet(
			id=first_set_id + 1,
			product=id,
			feature_variant=cat_d[int(cat)]
		)
		feature_sets.append(feature_set)
		feature_set = FeatureSet(
			id=first_set_id + 2,
			product=id,
			feature_variant=ang_d[int(angle)]
		)
		feature_sets.append(feature_set)

		first_set_id += 3

	return first_prod_id + n, first_set_id


def chests_generator(first_prod_id, first_set_id, n):
	shuffle(names)
	images = [f for f in os.listdir(os.path.join('images', 'chests'))]
	img_len = len(images)

	for id in range(first_prod_id, first_prod_id + n, 1):
		image_f = images[id % img_len]
		color = image_f[0:image_f.find('-')]

		if randint(0, 100) > 94:
			in_stock = 0
		else:
			in_stock = 1
		if in_stock:
			if randint(0, 100) > 70:
				on_sale = 1
				discount = int(randint(1, 3) * 10)
			else:
				on_sale = 0
				discount = 0
		else:
			on_sale = 0
			discount = 0

		image_name = str(randint(0, 1000000)) + '_' + image_f
		img = cv2.imread(os.path.join('images', 'chests', image_f))
		base = os.path.split(os.getcwd())[0]
		cv2.imwrite(os.path.join(base, 'furniture_store', 'media', 'product_pics', image_name), img)

		product = Product(
			id=id,
			name=names[id % len(names)],
			category=5,
			color=color_d[int(color)],
			cost=int(randint(50, 160) * 100 - 1),
			description="",
			image='product_pics/' + image_name,
			displayed=1,
			in_stock=in_stock,
			on_sale=on_sale,
			discount=discount
		)
		products.append(product)

	return first_prod_id + n, first_set_id


def fill_db_product(db_name):
	conn = sqlite3.connect(os.path.join(os.path.split(os.getcwd())[0], 'furniture_store', db_name))
	c = conn.cursor()
	records = [(p.id, p.name, p.category, p.color, p.description, p.image, p.discount, p.displayed, p.in_stock, p.on_sale, p.cost) for p in products]
	c.executemany('INSERT INTO shop_product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', records)
	conn.commit()
	conn.close()


def fill_db_featureset(db_name):
	conn = sqlite3.connect(os.path.join(os.path.split(os.getcwd())[0], 'furniture_store', db_name))
	c = conn.cursor()
	records = [(f.id, f.feature_variant, f.product) for f in feature_sets]
	c.executemany('INSERT INTO shop_featureset VALUES (?, ?, ?)', records)
	conn.commit()
	conn.close()


def delete_table(db_name, table):
	conn = sqlite3.connect(os.path.join(os.path.split(os.getcwd())[0], 'furniture_store', db_name))
	c = conn.cursor()
	c.execute(f"DELETE FROM {table}")
	conn.commit()
	conn.close()


# password = 123456qwe
# user0 - admin
def user_generator(db_name, n):
	conn = sqlite3.connect(os.path.join(os.path.split(os.getcwd())[0], 'furniture_store', db_name))
	c = conn.cursor()

	password = 'pbkdf2_sha256$216000$c6PyAKwEtHZz$+U9C6mqIZ59QFwqWXaTPCX+0iL6XPURunSmZhJip9rQ='
	for i in range(n):
		if i == 0:
			admin = 1
		else:
			admin = 0
		c.execute('INSERT INTO users_myuser VALUES (?, ?, ?, ?, ?, ?)', (i, password, None, f'user{ i }@mail.ru', 1, admin))
		c.execute('INSERT INTO users_profile VALUES (?, ?, ?, ?)', (i, None, i, 6))
		c.execute('INSERT INTO cart_cart VALUES (?, ?)', (i, i))

	conn.commit()
	conn.close()


def review_generator(db_name):
	conn = sqlite3.connect(os.path.join(os.path.split(os.getcwd())[0], 'furniture_store', db_name))
	c = conn.cursor()
	u_ids = [row[0] for row in c.execute('SELECT * FROM users_myuser')]
	p_ids = [row[0] for row in c.execute('SELECT * FROM shop_product')]
	id = 0

	for p in range(len(p_ids)):
		n = randint(0, 15)
		shuffle(u_ids)

		for i in range(n):
			rating = randint(1, 5)
			if rating > 3:
				review_text = [
					'Отличный товар!',
					'Лучшее за свои деньги',
					'Покупка очень понравилась, всем рекомендую!',
					'Замечательный товар, рад покупке',
					'Цена немного завышена, но товаром все равно доволен',
					'все классс!',
					'рекомендую всем для покупки этот товар, нисколько не жалею потраченных денег.',
				]
				plus = [
					'Отличное качество',
					'Простота сборки',
					'Очень удобно пользоваться',
					'Цвет отлично вписывается в обстановку',
					'+',
				]
				minus = [
					'Не обнаружил',
					'Довольно высокая цена',
					'нет',
					'Спустя месяц пользования могу сказать, что минусов не нашел.',
					'Цена',
				]
			else:
				review_text = [
					'Товар разочаровал',
					'Товар не стоит своих денег',
					'Ужасное качество материалов',
					'НЕ покупайте это!!',
					'Ужас, как вообще такое можно продавать',
					'Товар сильно разочаровал, не советую к покупке',
				]
				plus = [
					'Плюсов нет, одни минусы',
					'Из плюсов можно отметить только быструю доставку',
					'не нашел',
					'-',
					'нет',
				]
				minus = [
					'Отвратительный цвет',
					'Получил товар с дефектами',
					'Слишком высокая цена',
					'🤢🤢🤢🤢🤢',
					'не понравилось',
				]

			date = get_datetime('2015-01-01', '2020-12-31') + '.272315'
			c.execute('INSERT INTO reviews_review VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (id, choice(plus), choice(minus), choice(review_text), date, p_ids[p], u_ids[i], rating))
			id += 1

	conn.commit()
	conn.close()


def generate_all():
	cur_p_id = 1
	cur_set_id = 1
	db = 'db.sqlite3'

	# Удаляем старые картинки из директории сайта
	base = os.path.join(os.path.split(os.getcwd())[0], 'furniture_store', 'media', 'product_pics')
	files = [f for f in os.listdir(base)]
	for f in files:
		os.remove(os.path.join(base, f))

	# Удаляем прошлые данные из таблиц
	delete_table(db, 'reviews_review')
	delete_table(db, 'cart_cartitem')
	delete_table(db, 'cart_orderitem')
	delete_table(db, 'cart_order')
	delete_table(db, 'shop_featureset')
	delete_table(db, 'shop_product')

	delete_table(db, 'cart_cart')
	delete_table(db, 'users_profile')
	delete_table(db, 'users_myuser')

	# Генерация таблиц product и featureset
	cur_p_id, cur_set_id = bed_generator(cur_p_id, cur_set_id, 200)
	cur_p_id, cur_set_id = chair_generator(cur_p_id, cur_set_id, 200)
	cur_p_id, cur_set_id = table_generator(cur_p_id, cur_set_id, 200)
	cur_p_id, cur_set_id = closet_generator(cur_p_id, cur_set_id, 200)
	cur_p_id, cur_set_id = chests_generator(cur_p_id, cur_set_id, 200)
	fill_db_product(db)
	fill_db_featureset(db)

	# Генерация таблиц user, profile, cart
	user_generator(db, 500)

	review_generator(db)

generate_all()

