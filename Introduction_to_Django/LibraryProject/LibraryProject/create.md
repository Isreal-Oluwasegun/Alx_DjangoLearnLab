# Create Operation

## Django Shell Commands
```python
book = Book(title="Mr Success", author="Makinde I.S", publication_year=2025)
book.save()

Output
No explicit output from .save(), but creation is confirmed by:

python
Book.objects.values_list()
# Output:
# <QuerySet [
#     (1, 'Complete Django', 'Isreal M.S', 2025),
#     (2, 'Mr Success', 'Makinde I.S', 2025)