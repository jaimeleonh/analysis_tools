def randomize(input_string):
    import random, string
    random_str = "".join(random.choice(string.ascii_letters) for _ in range(10))
    return "{}_{}".format(input_string, random_str)