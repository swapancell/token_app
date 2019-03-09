from django.shortcuts import render

# Create your views here.

def clearing_tokens():
    token_list = tokens.objects.all()
    for token in token_list:
        if int(token.expiry) < int(datetime.now().timestamp()):
            token.delete()
        else:
            pass






def token_handler(request):
    if request.method == "GET":
        action = request.GET.get("action",None)
        if action == "add":
            token = request.GET.get("token",None)
            instance = tokens.objects.create(token = token,expiry = str(int(datetime.now().timestamp())+90))
            instance.save()
            clearing_tokens()
            #print("token saved ")
            #print(token)
            return HttpResponse(json.dumps({
                "status":"added"
                }))
        else:
            clearing_tokens()
            tokens_list = [x for x in tokens.objects.all()]
            if len(tokens_list) != 0:
                index = tokens_list.index(random.choice(tokens_list))
                token_obj = tokens_list[index]
                token = token_obj.token
                token_obj.delete()
                return HttpResponse(json.dumps({
                    "status":"success",
                    "token":token
                    }))
            else:
                return HttpResponse(json.dumps({
                    "status":"fail",
                    "reason":"no token available"
                    }))

