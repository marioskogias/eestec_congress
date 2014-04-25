# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import View
from django.db.models import Count

from models import Participant


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
            if not absences:
                all_here.append(item)
            elif item['count'] == len(absences):
                name_list = map(lambda x: x.__str__(), absences)
                temp = {'name': item['lc'], 'count': item['count'],
                        'missing': name_list}
                some_here.append(temp)
            else:
                name_list = map(lambda x: x.__str__(), absences)
                temp = {'name': item['lc'], 'missing': name_list}
                none_here.append(temp)

        return render_to_response('index.html')
