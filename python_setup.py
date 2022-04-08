def hello():
    print('hello user')

def pack(one,two,three):
    return [one,two,three]

def eat_lunch(list):
  if len(list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(list)):
      if i == 0:
        print("First I eat "+{list[0]})
      else:
        print("Next I eat "+{list[i]})

hello()
print(pack("a","b","c"))
eat_lunch([])
eat_lunch(["pbj"])
eat_lunch(["cereal","sandwich","pie"])