# update.md`


## Django Shell Commands
```python
book = Book.objects.get(title="Mr Success")
book.title = "Mr Victory"
book.save()

Output
No explicit output from .save(), but confirmed with:

python
Book.objects.values_list()
# Output:
# <QuerySet [
#     (1, 'Complete Django', 'Isreal M.S', 2025),
#     (3, 'Mr Victory', 'Makinde I.S', 2025)
# ]>