from random import choice, randint
import os
import cv2


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


def get_name_pool(filename):
	names = []

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			word = line[:-1]
			names.append(word.lower())

	return names

names = get_name_pool('swe_nouns.txt')
color_d = {
	1 : 2,
	2 : 8,
	3 : 9,
	4 : 1,
	5 : 3,
	6 : 4,
	7 : 10,
	8 : 5
}
products = []
feature_sets = []

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
		#image_f = '10_2_sjdhbf'
		color = image_f[0:image_f.find('-')]
		var = image_f[len(color) + 1:image_f[len(color) + 1:].find('-') + len(color) + 1]

		if randint(0, 100) > 94:
			in_stock = False
		else:
			in_stock = True
		if in_stock:
			if randint(0, 100) > 70:
				on_sale = True
				discount = int(randint(1, 3) * 10)
			else:
				on_sale = False
				discount = 0
		else:
			on_sale = False
			discount = 0

		image = 'product_pics/' + image_f + str(randint(0, 1000000))

		product = Product(
			id=id,
			name=names[id % len(names)],
			category=1,
			color=color_d[int(color)],
			cost=int(randint(10, 30) * 1000 - 1),
			description="",
			image=image,
			displayed=True,
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

		return id + 1, first_set_id


def json_output_product(product):
	'''
	res = '['

	for p in product:
		row = f'{{"model": "shop.product", "pk": {p.id}, "fields": {{"name": "{p.name}", "category": "{p.category}", "color": "{p.color}", "cost": {p.cost}, "description": "{p.description}", "images": "product_pics/{p.image}"}}}}'
		res += row + ', '

	res = res[:len(res) - 2] + ']'
	'''
	res = '{
    "type": "table",
    "database": null,
    "name": "shop_product",
    "withoutRowId": true,
    "ddl": "CREATE TABLE \"shop_product\" (\"id\" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \"name\" varchar(50) NOT NULL, \"category_id\" integer NOT NULL REFERENCES \"shop_category\" (\"id\") DEFERRABLE INITIALLY DEFERRED, \"color_id\" integer NOT NULL REFERENCES \"shop_color\" (\"id\") DEFERRABLE INITIALLY DEFERRED, \"description\" text NOT NULL, \"image\" varchar(100) NOT NULL, \"discount\" integer NOT NULL, \"displayed\" bool NOT NULL, \"in_stock\" bool NOT NULL, \"on_sale\" bool NOT NULL, \"cost\" integer NOT NULL);",
    "columns": [
        {
            "name": "id",
            "type": "integer",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL "
                },
                {
                    "type": "PRIMARY KEY",
                    "definition": "PRIMARY KEY AUTOINCREMENT"
                }
            ]
        },
        {
            "name": "name",
            "type": "varchar",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "category_id",
            "type": "integer",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL "
                },
                {
                    "type": "FOREIGN KEY",
                    "definition": "REFERENCES \"shop_category\" (\"id\") "
                }
            ]
        },
        {
            "name": "color_id",
            "type": "integer",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL "
                },
                {
                    "type": "FOREIGN KEY",
                    "definition": "REFERENCES \"shop_color\" (\"id\") "
                }
            ]
        },
        {
            "name": "description",
            "type": "text",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "image",
            "type": "varchar",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "discount",
            "type": "integer",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "displayed",
            "type": "bool",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "in_stock",
            "type": "bool",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "on_sale",
            "type": "bool",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        },
        {
            "name": "cost",
            "type": "integer",
            "constraints": [
                {
                    "type": "NOT NULL",
                    "definition": "NOT NULL"
                }
            ]
        }
    ],'

	return res


def generate_all():
	cur_p_id = 0
	cur_set_id = 0
	cur_p_id, cur_set_id = bed_generator(cur_p_id, cur_set_id, 100)


