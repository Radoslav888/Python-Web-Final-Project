from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from Hestia.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignOutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')


def user_details_view(request, pk):
    user = UserModel.objects.filter(pk=pk).get()
    listings = user.listing_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 4)

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    context = {
        'listings': listings,
        'object': user,
        'is_owner': request.user == user,
    }
    return render(request, 'accounts/profile-details-page.html', context)


class EditUserView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'phone_number')

    def get_success_url(self, **kwargs):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

