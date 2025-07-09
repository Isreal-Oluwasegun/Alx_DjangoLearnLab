# update.md`


## Django Shell Commands
```python
book = Book.objects.get(title='1984')
book.title = "Nineteen Eighty-Four"
book.save()

Output
No explicit output from .save(), but confirmed with:

python
Book.objects.values_list()
# Output:
# <QuerySet [
#     (1, '1984', 'George Orwell', 1949)