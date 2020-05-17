from random import choice, randint
import os
import cv2


class Product:
	def __init__(self, id, name, category, color, cost, description, image):
		self.id = id
		self.name = name
		self.category = category
		self.color = color
		self.cost = cost
		self.description = description
		self.image = image


class Category:
	def __init__(self, id, name, cost_range, description):
		self.id = id
		self.name = name
		self.cost_range = cost_range
		self.description = description


colors = {
	1: 'Белый',
	2: 'Черный',
	3: 'Серый',
	4: 'Бирюзовый',
	5: 'Бежевый',
	6: 'Розовый',
	7: 'Желтый',
	8: 'Синий',
	9: 'Зеленый',
	10: 'Красный',
}


def get_cat_imgs(id):
	onlyfiles = [f for f in os.listdir(os.path.join('categories', str(id))) if os.path.isfile(os.path.join('categories', str(id), f))]

	return onlyfiles


def get_category_pool():
	description = 'Без описания'
	categories = [
		Category(1, 'Кровати', (9990, 35990), [description]),
		Category(2, 'Столы', (5990, 18990), [description]),
		Category(3, 'Стулья', (1990, 5990), [description]),
		Category(4, 'Диваны', (19990, 41990), [description]),
		Category(5, 'Шкафы', (16990, 50990), [description])
	]

	return categories


def get_name_pool(filename):
	names = []

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			word = line[:-1]
			names.append(word.lower())

	return names


def get_image(id):
	files = [f for f in os.listdir(os.path.join('categories', str(id))) if os.path.isfile(os.path.join('categories', str(id), f))]
	name = choice(files)
	color = colors[int(name[:name.find('_')])]
	img = cv2.imread(os.path.join('categories', str(id), name))
	new_name = str(randint(0, 1000000)) + '_' + name
	base = os.path.split(os.getcwd())[0]

	cv2.imwrite(os.path.join(base, 'furniture_shop', 'media', 'product_pics', new_name), img)

	return new_name, color


def generate_product(start, end):
	products = []
	name_pool = get_name_pool("swe_nouns.txt")
	categories = get_category_pool()

	for i in range(start, end, 1):
		cat = choice(categories)
		img_info = get_image(cat.id)

		product = Product(
			id=i + 1,
			name=choice(name_pool),
			category=cat.name,
			cost=float(randint(cat.cost_range[0], cat.cost_range[1])),
			description=cat.description,
			image=img_info[0],
			color=img_info[1]
		)

		products.append(product)

	return products


def json_output(product):
	res = '['

	for p in product:
		row = f'{{"model": "shop.product", "pk": {p.id}, "fields": {{"name": "{p.name}", "category": "{p.category}", "color": "{p.color}", "cost": {p.cost}, "description": "{p.description}", "images": "product_pics/{p.image}"}}}}'
		res += row + ', '

	res = res[:len(res) - 2] + ']'

	return res


def main():
	products = generate_product(0, 100)
	out = json_output(products)

	with open('product.json', 'w') as f:
		f.write(out)


if __name__ == '__main__':
	main()
