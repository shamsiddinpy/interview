# with open('context.json', 'w') as file:
#     file.write("Context menejer  context.text fayiliga w orqali yoziladiii..!!!")

import json

with open('context.json', 'r') as file:
    context1 = file.read()
    if not context1.strip():
        raise Exception('The context1 file is empty')
    data = json.loads(context1)
    print(data)
