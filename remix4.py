lists = ["yes"]
gamer = "boy"

def format(args):
  if isinstance(args, list):
    print(str(args[0]).format(args[1]))
  else:
    print("no")
format(["gamer {0}", "squad"])