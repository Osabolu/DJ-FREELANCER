from django.shortcuts import render

# Create your views here.
def service(request):
    context = {
        "my_services":["services we render-","Recuitment","Procjects"]
    }
    return render(request, "dtl/service.html", context)

def testimonials(request):
    "Why not share with us today your journey with everyone since you became part of FReelancer. We want to hear from you."
    context = {
        "my_names":["Denise: Reviews i got from here made me join, and ever since, I've come in contact with amazing employers and bonded with colleagues for life",
                            "Ryce: I suggest people should stop been doubting thomas's and join the winning team. Freelancer rock!!!",
                            "Durant: It takes a lot of patience to get the right client for a job. I hate wating."]
    }
    return render(request, "dtl/test.html", context)

def case_studies(request):
    context = {
        "summary":"We are transparent, we are open to question and answers session. Book now."

    }
    return render(request, "dtl/case.html", context)

def Blog(request):
    context = {
        "For gossips and free speech, you can express yourself as you please. Join us today"
        "my_blog":["Articles","Views"]
    }
    return render(request, "dtl/blog.html", context)

def pricing(request):
    context = {
        "all":[
        "my_services:Recruitment", "Projects...",
        "my_price:Billings","Bids"]
    }
    return render(request, "dtl/pricing.html", context)