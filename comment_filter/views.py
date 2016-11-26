from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_comments.models import Comment
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view


from comment_filter.models import CensoredWord, ReportedComment




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
        #print ('comment_split', comment_split)
        #print('censored_words', censored_words)
        for char in ' ?.!/;:,':
            comment_split = comment_split.replace(char,'')

        if comment_split.lower() in censored_words:
            comment_splits[index] = comment_splits[index].replace(comment_splits[index], '**censored**')
        index += 1
    #print('comment_splits', comment_splits)
    comment_join = ' '.join(comment_splits)
    if comment.comment != comment_join:
        # notify user
        pass

    comment.comment = comment_join
    #print('comment_join', comment_join)
    comment.save()

    return JSONResponse("Ok", status=200)


@api_view(['POST'])
def report_comment(request):
    comment_id = request.POST.get('comment_id')
    user_id = request.POST.get('user_id')
    comment = Comment.objects.get(id=comment_id)
    user = User.objects.get(id=user_id)
    reported, created = ReportedComment.objects.get_or_create(comment=comment, reporter=user)
    if created:
        response = 'You are succesfully report this comment'
    else:
        response = 'You have reported this comment before'

    reported_count = ReportedComment.objects.filter(comment=comment).count()
    if reported_count > 10:
        comment.is_removed = True
        comment.save()

    
    return JSONResponse({'response': response}, status=200)

def notifications(request, template_name):
    notifs = request.user.notifications.unread()
    context = {'notifs': notifs}

    return render(request, template_name, context)

def notifications_mark_all_as_read(request):
    request.user.notifications.mark_all_as_read()

    return redirect('/comment_filter/notifications/')
