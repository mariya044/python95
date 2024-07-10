from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from announcement.models import Announcement

from announcement.forms import StudentAnnouncementForm

from announcement.models import Subject


@login_required()
def announcement(request,subject_id=None):
    if subject_id:
        announcement = Announcement.objects.filter(subject_id=subject_id)
    else:
        announcement = Announcement.objects.all()
    paginator=Paginator(announcement,2)
    page_number=request.GET.get('page',1)
    try:
        announcements=paginator.page(page_number)
    except PageNotAnInteger:
        announcements=paginator.page(1)
    except EmptyPage:
        announcements=paginator.page(paginator.num_pages)
    context = {
        'subjects': Subject.objects.all(),
        'announcements': announcements,

    }

    return render(request, "announcement.html", context)


@login_required()
def announcement_detail(request,announcement_id):
    announcement=get_object_or_404(Announcement,id=announcement_id)
    return render (request,'announcement_view.html',{'announcement':announcement})



@permission_required(perm="announcement.add_announcement", raise_exception=True)
def add_announcement(request):
    if request.method == "POST":
            form = StudentAnnouncementForm(request.POST, request.FILES)
            if form.is_valid():
                ann = form.save(commit=False)
                ann.user = request.user
                ann.save()
                form.save_m2m()
                return redirect("announcements")
            else:
                return redirect("announcements")
    else:
            form = StudentAnnouncementForm()
    return render(request, "add_announcement.html", {"form": form})



@login_required()
def edit_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    if request.user != announcement.user:
        return redirect(f"/announcements/{announcement_id}/")
    if request.method == "GET":
        form = StudentAnnouncementForm(instance=announcement)
    if request.method == 'POST':
        form = StudentAnnouncementForm(request.POST,instance=announcement)
        if form.is_valid():
            form.save()
        return redirect("announcements")
    return render(request, "edit_announcement.html", {"form": form, "announcement": announcement})




class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = reverse_lazy("announcements")
    template_name = "delete_announcement.html"