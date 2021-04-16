import string
import random
def pwd(a):
	pas=''.join(random.choice(string.ascii.letters) for _ in range(a))
	print(pas)
