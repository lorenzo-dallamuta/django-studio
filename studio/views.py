from studio.models import Medico
from django.shortcuts import render
from accounts.models import User
from studio.models import Medico, Studio


def home(request):
    try:
        user = User.objects.filter(username=request.user.username).first()
    except:
        user = None
    # query = Studio.objects.filter(pk=1).prefetch_related('medico')
    studio = Studio.objects.first()
    medici = Medico.objects.filter(studio__id=studio.id)

    context = {'user': user, 'studio': studio, "medici": medici}
    try:
        context['image'] = user.avatar
    except:
        pass

    return render(request, 'studio/home.html', context=context)


# class medici(ListView):
#     template_name = 'studio/body.html'
#     paginate_by = 5

#     def get_queryset(self):
#         self.studio = get_object_or_404(Studio, name=self.kwargs['studio'])
#         return Medico.objects.filter(studio__id=self.studio.id)
