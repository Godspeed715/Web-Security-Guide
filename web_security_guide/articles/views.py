# articles/views.py
from django.shortcuts import render, redirect
from django.http import Http404
# from django.contrib.auth.decorators import login_required   # --- AUTH (commented out) ---
# from .models import OwaspTop10                              # --- DATABASE (commented out) ---

# Import static content data file (replaces DB)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import ARTICLES


# Create your views here.
# @login_required                                             # --- AUTH (commented out) ---
def owasp_list(request):
    """Redirect to first article"""
    return redirect('owasp', page_no=1)


# @login_required                                             # --- AUTH (commented out) ---
def owasp(request, page_no):
    # --- DATABASE (commented out) ---
    # page_count = OwaspTop10.objects.all().count()
    # prev_id = page_no - 1 if page_no > 0 else None
    # next_id = page_no + 1 if page_no < page_count else None
    # article = get_object_or_404(OwaspTop10, page_no=page_no)
    # return render(request, 'index.html', {'article': article, 'prev_id': prev_id, 'next_id': next_id})

    # --- STATIC DATA (new code) ---
    page_count = len(ARTICLES)
    prev_id = page_no - 1 if page_no > 1 else None
    next_id = page_no + 1 if page_no < page_count else None

    # Find the matching article dict and expose its keys as attributes
    data = next((a for a in ARTICLES if a["page_no"] == page_no), None)
    if data is None:
        raise Http404(f"No article found for page {page_no}")

    # Wrap dict as a simple object so templates can use article.title etc.
    article = type("Article", (), data)()

    return render(request, 'index.html', {'article': article, 'prev_id': prev_id, 'next_id': next_id})
