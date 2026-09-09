# videos/views.py
from django.shortcuts import render, redirect
from django.http import Http404
# from django.contrib.auth.decorators import login_required   # --- AUTH (commented out) ---
# from .models import Video                                   # --- DATABASE (commented out) ---

# Import static content data file (replaces DB)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import VIDEOS


# Create your views here.
# @login_required                                             # --- AUTH (commented out) ---
def videos_list(request):
    """Redirect to first video"""
    return redirect('videos', page_no=1)


# @login_required                                             # --- AUTH (commented out) ---
def videos(request, page_no):
    # --- DATABASE (commented out) ---
    # page_count = Video.objects.all().count()
    # prev_id = page_no - 1 if page_no > 0 else None
    # next_id = page_no + 1 if page_no < page_count else None
    # video = get_object_or_404(Video, page_no=page_no)
    # print(video.src)
    # return render(request, 'videos.html', context={'video': video, 'prev_id': prev_id, 'next_id': next_id})

    # --- STATIC DATA (new code) ---
    page_count = len(VIDEOS)
    prev_id = page_no - 1 if page_no > 1 else None
    next_id = page_no + 1 if page_no < page_count else None

    # Find the matching video dict
    data = next((v for v in VIDEOS if v["page_no"] == page_no), None)
    if data is None:
        raise Http404(f"No video found for page {page_no}")

    # Wrap dict as a simple object so templates can use video.title etc.
    video = type("Video", (), data)()
    print(video.src)  # kept for debugging as in original

    return render(request, 'videos.html', context={'video': video, 'prev_id': prev_id, 'next_id': next_id})
