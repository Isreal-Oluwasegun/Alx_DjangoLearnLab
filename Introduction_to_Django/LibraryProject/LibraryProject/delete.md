### delete.md

## Django Shell Commands
```python
book = Book.objects.get(id=3)
book.delete()

Output
text
(1, {'bookshelf.Book': 1})

Final Check
python
Book.objects.values_list()
# Output:
# <QuerySet [
#     (1, 'Complete Django', 'Isreal M.S', 2025)
# ]>