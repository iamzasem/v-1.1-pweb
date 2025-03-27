from urllib import request
from django.shortcuts import render, HttpResponse, redirect  # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.conf import settings # type: ignore
from .models import AlbumCategory, Photo
from django.http import JsonResponse # type: ignore
from django.core.paginator import Paginator # type: ignore
import os
from django.core.mail import send_mail # type: ignore

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):  # Note: Duplicated in URLs
    return render(request, 'gallery.html')


def seo(request):
    return render(request, 'seo.html')

def thumbnails(request):
    return render(request, 'thumbnails.html')

def digitalmarketing(request):
    return render(request, 'digitalmarketing.html')

def services(request):
    return render(request, 'services.html')

def gallery_page(request):
    albums = AlbumCategory.objects.prefetch_related('photos').all()
    context = {'albums': albums}
    return render(request, 'gallery.html', context)

def about_page(request):
    try:
        friends_album = AlbumCategory.objects.get(name='Friends')
        friends_photos = Photo.objects.filter(album=friends_album)
    except AlbumCategory.DoesNotExist:
        friends_photos = []
    
    try:
        projects_album = AlbumCategory.objects.get(name='Projects')
        project_photos = Photo.objects.filter(album=projects_album)
    except AlbumCategory.DoesNotExist:
        project_photos = []
    
    context = {
        'friends_photos': friends_photos,
        'project_photos': project_photos,
    }
    return render(request, 'about.html', context)




# Note: This appears again but with a different implementation
def gallery(request):
    albums = AlbumCategory.objects.all()  # Fixed from "Album" to "AlbumCategory"
    return render(request, 'gallery.html', {'albums': albums})

def gallery_view(request):
    albums = []
    gallery_path = os.path.join(settings.STATICFILES_DIRS[0], 'gallery')
    
    if os.path.exists(gallery_path):
        for album_name in os.listdir(gallery_path):
            album_folder = os.path.join(gallery_path, album_name)
            if os.path.isdir(album_folder):
                photo_files = [f for f in os.listdir(album_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
                if photo_files:
                    photos = [f'gallery/{album_name}/{file}' for file in photo_files]
                    albums.append({
                        'name': album_name.capitalize(),
                        'cover_image': photos[0],
                        'photos': photos
                    })
    
    return render(request, 'gallery.html', {'albums': albums})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            subject=f"New Contact Form Message from {first_name}",
            message=f"From: {email}\n\nMessage: {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['iamzasemworks@gmail.com'],  # Your email
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def contact(request):
    whatsapp_number = "9779845996160"
    whatsapp_message = "Hi Zasem, I want to chat about a project!"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message.replace(' ', '%20')}"
    return render(request, 'contact.html', {'whatsapp_url': whatsapp_url})


def german_view(request):
    return render(request, 'german.html')

def grammarlevels(request):
    return render(request, 'grammar-levels.html')

def a1Topics(request):
    return render(request, 'a1-topics.html')

def otherTopics(request):
    return render(request, 'other-topics.html')

def nouns_view(request):
    return render(request, 'nouns.html')

def articles_view(request):
    return render(request, 'articles.html')

def adjectives_view(request):
    return render(request, 'adjectives.html')

def conjugation_view(request):
    return render(request, 'conjugation.html')

def deshalbtrotzdem_view(request):
    return render(request, 'deshalbtrotzdem.html')

def cases_view(request):
    return render(request, 'cases.html')

def prepositions_view(request):
    return render(request, 'prepositions.html')

def structure_view(request):
    return render(request, 'structure.html')

def listening_view(request):
    return render(request, 'listening.html')

def writing_view(request):
    return render(request, 'writing.html')

def speaking_view(request):
    return render(request, 'speaking.html')

def culture_view(request):
    return render(request, 'culture.html')

def exam_view(request):
    return render(request, 'exam.html')

def personal_pronouns_view(request):
    return render(request, 'personal-pronouns.html')

def verbs_wfrage_ja_nein_normaler_view(request):
    return render(request, 'verbs-wfrage-ja-nein-normaler.html')

def imperative_view(request):
    return render(request, 'imperative.html')

def akkusative_view(request):
    return render(request, 'akkusative.html')

def possessive_view(request):
    return render(request, 'possessive.html')

def modalverbpresent_view(request):
    return render(request, 'modalverbpresent.html')

def praterituma1_view(request):
    return render(request, 'praterituma1.html')

def trennbare_view(request):
    return render(request, 'trennbare.html')

def dative_view(request):
    return render(request, 'dative.html')

def wechsel_view(request):
    return render(request, 'wechsel.html')

def partizip2_view(request):
    return render(request, 'partizip2.html')

def welcherdieser_view(request):
    return render(request, 'welcherdieser.html')


def a2topics_view(request):
    return render(request, 'a2-topics.html')

def doch_view(request):
    return render(request, 'doch.html')

def reflexive_view(request):
    return render(request, 'reflexive.html')

def weil_view(request):
    return render(request, 'weil.html')

def modal_prateritum_view(request):
    return render(request, 'modal_prateritum.html')


def dass_view(request):
    return render(request, 'dass.html')

def wenn_view(request):
    return render(request, 'wenn.html')

def adjend_view(request):
    return render(request, 'adjend.html')

def comperlative_superlative_view(request):
    return render(request, 'comperlativesuperlative.html')

def werden_view(request):
    return render(request, 'werden.html')

def indirect_view(request):
    return render(request, 'indirect.html')

def konjunktiv2_view(request):
    return render(request, 'konjunktiv2.html')

def genetivname_view(request):
    return render(request, 'genetivname.html')

def als_view(request):
    return render(request, 'als.html')

def extrapronomen_view(request):
    return render(request, 'extrapronomen.html')

def Interrogativartikel_view(request):
    return render(request, 'Interrogativartikel.html')

def genetivname_view(request):
    return render(request, 'genetivname.html')

def relativsatz_view(request):
    return render(request, 'relativsatz.html')

def damitumzu_view(request):
    return render(request, 'damitumzu.html')

def konjunktivII_view(request):
    return render(request, 'konjunktivII.html')

def verbenmitpreposition_view(request):
    return render(request, 'verbenmitpreposition.html')


def wfrageprep_view(request):
    return render(request, 'wfrageprep.html')


def konjunktivII_view(request):
    return render(request, 'konjunktivII.html')


def b1_topics_view(request):
    return render(request, 'b1-topics.html')

def konjunktivII_view(request):
    return render(request, 'konjunktivII.html')

def infinitiv_zu(request):
    return render(request, 'infinitiv-zu.html')

def lassen(request):
    return render(request, 'lassen.html')

def obwohl(request):
    return render(request, 'obwohl.html')

def genitiv(request):
    return render(request, 'genitiv.html')

def wegen_trotz(request):
    return render(request, 'wegen-trotz.html')

def praeteritum(request):
    return render(request, 'praeteritum.html')

def temp_praep(request):
    return render(request, 'temp-praep.html')

def deshalb_darum(request):
    return render(request, 'deshalb-darum.html')

def sodass(request):
    return render(request, 'sodass.html')

def konj2(request):
    return render(request, 'konj2.html')

def pronomen_praep(request):
    return render(request, 'pronomen-praep.html')

def verben_praep(request):
    return render(request, 'verben-praep.html')

def komp_super(request):
    return render(request, 'komp-super.html')

def aus_material(request):
    return render(request, 'aus-material.html')

def relativ_dativ(request):
    return render(request, 'relativ-dativ.html')

def relativ_praep(request):
    return render(request, 'relativ-praep.html')

def plusquam(request):
    return render(request, 'plusquam.html')

def temp_neben(request):
    return render(request, 'temp-neben.html')

def brauchen_zu(request):
    return render(request, 'brauchen-zu.html')

def reflexiv(request):
    return render(request, 'reflexiv.html')

def konnektoren(request):
    return render(request, 'konnektoren.html')

def adj_ohne_art(request):
    return render(request, 'adj-ohne-art.html')

def passiv(request):
    return render(request, 'passiv.html')

def passiv_modal(request):
    return render(request, 'passiv-modal.html')

def genitiv_praep(request):
    return render(request, 'genitiv-praep.html')

def artikelpronomen(request):
    return render(request, 'artikelpronomen.html')

def relativ_was_wo(request):
    return render(request, 'relativ-was-wo.html')

def je_desto(request):
    return render(request, 'je-desto.html')

def partizip_adj(request):
    return render(request, 'partizip-adj.html')

def n_dekl(request):
    return render(request, 'n-dekl.html')

def practiceExam(request):
    return render(request, 'practice_Exam.html')

def exam1(request):
    return render(request, 'exam1.html')

def exam2(request):
    return render(request, 'exam2.html')


def exam3(request):
    return render(request, 'exam3.html')



def exam4(request):
    return render(request, 'exam4.html')



def exam5(request):
    return render(request, 'exam5.html')


def exam6(request):
    return render(request, 'exam6.html')

def exam7(request):
    return render(request, 'exam7.html')

def exam8(request):
    return render(request, 'exam8.html')

def exam9(request):
    return render(request, 'exam9.html')

def exam10(request):
    return render(request, 'exam10.html')


def schreibenb1m2(request):
    return render(request, 'schreibenb1m2.html')



def schreibenb1(request):
    return render(request, 'schreibenb1.html')

def schreibenb1m3(request):
    return render(request, 'schreibenb1m3.html')

def schreibenb1m4(request):
    return render(request, 'schreibenb1m4.html')

def schreibenb1m5(request):
    return render(request, 'schreibenb1m5.html')

def schreibenb1m6(request):
    return render(request, 'schreibenb1m6.html')

def schreibenb1m7(request):
    return render(request, 'schreibenb1m7.html')

def schreibenb1m8(request):
    return render(request, 'schreibenb1m8.html')

def schreibenb1m9(request):
    return render(request, 'schreibenb1m9.html')

def schreibenb1m10(request):
    return render(request, 'schreibenb1m10.html')

def sprechenb1m1(request):
    return render(request, 'sprechenb1m1.html')


def sprechenb1m2(request):
    return render(request, 'sprechenb1m2.html')

def sprechenb1m3(request):
    return render(request, 'sprechenb1m3.html')

def sprechenb1m4(request):
    return render(request, 'sprechenb1m4.html')

def sprechenb1m5(request):
    return render(request, 'sprechenb1m5.html')

def sprechenb1m6(request):
    return render(request, 'sprechenb1m6.html')

def sprechenb1m7(request):
    return render(request, 'sprechenb1m7.html')

def sprechenb1m8(request):
    return render(request, 'sprechenb1m8.html')

def sprechenb1m9(request):
    return render(request, 'sprechenb1m9.html')

def sprechenb1m10(request):
    return render(request, 'sprechenb1m10.html')


