# # Python Packages
# Modules are the .py files that contain definitions for functions, classes, and variables. Packages are the folders that contain the modules.

# So far, we have been working with singular modules (i.e., bday_messages.py). However, a collection of related modules with a similar purpose is a package.

# This is where things get crazy. There are 400,000+ Python packages in the world (and that's only counting those on PyPI, the official Python Package Index). You could even build and register your own module on PyPI for others to use!

# Python can tell a regular folder from a package if it has an __init__.py file, in addition to other .py files.

# Note: Some large and specialized packages are called "libraries".

# Here are some examples of packages and libraries in Python:

# 🔢 NumPy, Pandas, SciPy for data analysis.
# 📊 Matplotlib, Seaborn, Plotly for data visualization.
# 🧠 Scikit-learn, TensorFlow for machine learning.
# 🌐 Beautiful Soup for web scraping.
# 👾 Pygame for mini-games.
# 🤖 NLTK, OpenAI for chatbots.
# 🛠️ OS, Requests for automation.
# These packages make Python one of the most versatile languages in existence; you can use it to make all sorts of applications!

import wikipedia

# print(wikipedia.summary("Wikipedia"))

army=wikipedia.search("Indian Army", results=10, suggestion=False)
print(army)

army_summary=wikipedia.summary("Indian Army ranks and insignia", sentences=100,auto_suggest=True, redirect=True)
print(army_summary)