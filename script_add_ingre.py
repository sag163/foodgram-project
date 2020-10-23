import json


with open('assistant_product/ingredients.json', 'r') as f:
    data = json.load(f)
    print(
        json.dumps(data,
        ensure_ascii=False,))
    with open("assistant_product/ingree.json", "w") as file:
        print(json.dumps(data,
        ensure_ascii=False,), file=file)