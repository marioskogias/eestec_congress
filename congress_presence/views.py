# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Count

from models import Participant

TOKEN = "test"

class BaseView(View):

    def get(self, request):
        members = Participant.objects
        lcs = members.values('lc').annotate(count=Count('lc'))
        all_absences = members.filter(here = False)

        all_here = []
        some_here = []
        none_here = []

        for item in lcs:
            absences = filter(lambda x: x.lc == item['lc'], all_absences)
            if not absences: # none missing
                all_here.append(item)
            elif item['count'] == len(absences): # all missing
                name_list = map(lambda x: x.__str__(), absences)
                temp = {'name': item['lc'], 'missing': name_list}
                none_here.append(temp)
            else: # some missing
                name_list = map(lambda x: x.__str__(), absences)
                temp = {'name': item['lc'], 'count': item['count'],
                        'missing': name_list}
                some_here.append(temp)

        return render_to_response('index.html', {'all_missing': none_here,
                                                 'some_missing': some_here,
                                                 'all_here': all_here})
    def put(self, request, *args, **kwargs):
        data = request.raw_post_data
        key = data.split('=')[0]
        val = data.split('=')[1]
        if key == 'token' and val == TOKEN:
            try:
                participant = Participant.objects.get(id=self.kwargs['id'])
            except Participant.DoesNotExist:
                return HttpResponse(status=404)
            participant.here = True
            participant.save()
            return HttpResponse(status=200)
        return HttpResponse(status=401)
