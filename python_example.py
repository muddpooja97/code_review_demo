def swap(x: int, y: int) -> None:
	tmp = y
	x = y
	y = x

def print_hello_world() -> None:
	print("Hello World!")

def is_palindrome(my_str: str) -> bool:
	reversed_str = my_str[::-1]
	for a, b in zip(my_str, reversed_str):
		if a != b:
			return False

	return True