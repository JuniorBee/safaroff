from django.views.generic import ListView, FormView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render_to_response
from .models import About, Quote, Service, Worker, Work, BlogPost, Category
from .forms import ContactForm


class MainPageView(ListView):
    template_name = 'mainapp/index.html'
    model = BlogPost
    context_object_name = 'posts'
    paginate_by = 4

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = self.get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.get(id=1)
        context['quotes'] = Quote.objects.all()
        context['services'] = Service.objects.all()
        context['workers'] = Worker.objects.all()
        context['works'] = Work.objects.all()
        context['categories'] = Category.objects.all()
        context['form'] = ContactForm
        return context

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', None)
        if page is not None:
            context = self.get_context_data()
            return render_to_response('mainapp/posts_ajax.html', context)
        return super().get(request, args, kwargs)


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        data = form.cleaned_data
        message = data.get('message') + '\nSent by: '+data.get('name', '')
        send_mail(
            subject=data.get('subject').strip(),
            message=message,
            from_email=data['email'],
            recipient_list=['official@example.com'],
        )
        return super(ContactView, self).form_valid(form)


def success(request):
    return HttpResponse("OK", status=200)
