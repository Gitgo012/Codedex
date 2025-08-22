# Write code below 💖
from functools import reduce
#In Python, we can transform data using three powerful functions: map(), filter(), and reduce(). These functions allow us to manipulate, select, and aggregate data efficiently. Let's explore each one!
# MAP Example
# syntax - map(function, data)
# def divide_by_2(x):
#   return x/2

# halved=map(divide_by_2,[1,2,3,4,5])
# print(list(halved))

#FILTER fnc
#Here, we select elements from the data that satisfy the given condition specified by the function and return a new list. It helps extract specific items from a dataset based on the criteria you define. The input function in filter() must return a boolean.
#syntax - filter(function, data)
#example
# def filter_even(x):
#   return x % 2==0
#   #output will be boolean

# even_num=filter(filter_even, [1,2,3,4,5])
# print(list(even_num))

#REDUCE fnc
#syntax - 
# from functools import reduce
# reduce(function, data, initial)
#reduce() takes a collection of iterable data and combines its elements into a single value via a function. An optional initial value can be used, as well.

# This function is ideal for tasks like summing up a list of numbers.
#example

# from functools import reduce

# def multiply(x,y):
#   return x*y

# prod=reduce(multiply, [1,2,3,4,5])
# print(prod)

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
#EXERCISE
def filter_playlist(song_tuple):
    song, duration = song_tuple
    return duration>5
    
def min_to_seconds(song_tuple):
  song,duration=song_tuple
  minutes=int(duration)
  seconds=(duration-minutes)*100
  duration= minutes*60+seconds
  return song, duration

def total_playtime(sum, song_tuple):
  song,duration=song_tuple
  return duration+sum

filtered=filter(filter_playlist, playlist)
song_names=[song for song, _ in filtered]
print(song_names)

mapped=map(min_to_seconds, playlist)
print(list(mapped))

total=reduce(total_playtime, playlist, 0)
print(total)
