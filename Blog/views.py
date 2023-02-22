from django.shortcuts import render, redirect, HttpResponse
from .models import Post, BlogComment
from django.contrib import messages
from Blog.templatestags import extras


def blogHome(request):
    allPost = Post.objects.all()
    context = {"allPost": allPost}
    return render(request, "blog/home.html", context=context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]

        else:
            replyDict[reply.parent.sno].append(reply)

    context = {"post": post, "comments": comments, "replyDict": replyDict}

    return render(request, "blog/blogPost.html", context=context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.Post.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if not (user.is_anonymous):
            if parentSno == "":
                userComment = BlogComment(comment=comment, user=user, post=post)
                userComment.save()
                messages.success(request, "Ваш комментарии добавлен")
            else:
                parent = BlogComment.objects.get(sno=parentSno)
                _userComment = BlogComment(comment=comment, user=user, parent=parent, post=post)
                _userComment.save()
                messages.warning(request, "Ваш ответ был успешно добавлен к сообщению !")

        else:
            messages.warning(request, "Вы не авторизованны")
            return redirect(f"/blog/{post.slug}")

    return HttpResponse("404 - Не верный запрос !")

