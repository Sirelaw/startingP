ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Modify list
ft_list[1] = "World!"

# Create new tuple (since tuples are immutable)
ft_tuple = ("Hello", "Germany!")

# Modify set
ft_set.remove("tutu!")
ft_set.add("Heilbronn!")

# Modify dictionary value
ft_dict["Hello"] = "42Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)