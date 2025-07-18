Book.objects.filter(name="Mk")
Book.objects.values_list()
Librarian.objects.filter(library__name__iexact="obj library")