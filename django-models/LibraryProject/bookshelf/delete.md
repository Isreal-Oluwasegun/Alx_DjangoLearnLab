### delete.md

## Django Shell Commands
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


Final Check
python
Book.objects.values_list()
# Output:
# <QuerySet [
# ]>