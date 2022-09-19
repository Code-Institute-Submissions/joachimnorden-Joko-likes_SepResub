from .models import Category


def blog_categories(request):
    """
    Provides global access to categories
    """
    categories = Category.objects.all().order_by('name')

    context = {
        'categories': categories,
    }

    return context
