# Create Operation — Using Model Manager

## Django Shell Commands
```python
Book.objects.create(title="1984",author="George Orwell",publication_year=1949)

Output
No explicit output from .save(), but creation is confirmed by:

python
Book.objects.values_list()
# Output:
# <QuerySet [
#     (1, '1984', 'George Orwell', 1949)