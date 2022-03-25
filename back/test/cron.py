from rss.models import Job
from rss.serializers import JobMarkReadSerializer
from django.db.models import Prefetch
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.sql.datastructures import Join


def test_command_1():
    # print('test 1')
    # jobs = Job.objects.filter(id__in = ['91a4d7b6-ea26-4dfc-bb01-ba4118be67cc', '18791b80-b86a-4715-b325-aa1924667801']).select_related('readed_users').all()
    # jobs = Job.objects.filter(id__in = ['91a4d7b6-ea26-4dfc-bb01-ba4118be67cc', '18791b80-b86a-4715-b325-aa1924667801']).all()

# prefetch_related
    # job = jobs[1]

    # job = Job.objects.prefetch_related(Prefetch('readed_users', User.objects.filter(id=2), 'readed_auth_user')).get(pk='18791b80-b86a-4715-b325-aa1924667801')
    # print(job.readed_auth_user)

    # data = JobTestSerializer(job).data

    # print(data)
    # job = Job.objects.annotate(Count('readed_users')).get(pk='18791b80-b86a-4715-b325-aa1924667801')

    # print(job)

    # print(job.readed_users.all())




    
