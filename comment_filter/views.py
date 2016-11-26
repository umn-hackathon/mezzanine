from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django_comments.models import Comment

from comment_filter.models import CensoredWord




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['POST'])
def censored_check(request):
    comment_id = request.POST.get('comment_id')

    comment = Comment.objects.get(id=comment_id)
    censored_words = CensoredWord.objects.values_list('word', flat=True)

    comment_splits = comment.comment.split()
    index = 0

    for comment_split in comment_splits:
        print ('comment_split', comment_split)
        print('censored_words', censored_words)
        if comment_split in censored_words:
            comment_splits[index] = comment_splits[index].replace(comment_splits[index], '**censored**')
        index += 1
    print('comment_splits', comment_splits)
    comment_join = ' '.join(comment_splits)
    if comment.comment != comment_join:
        # notify user
        pass

    comment.comment = comment_join
    print('comment_join', comment_join)
    comment.save()

    return JSONResponse("Ok", status=200)
