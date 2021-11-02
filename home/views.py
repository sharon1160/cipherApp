from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import TextTransForm, TextPlayfairForm, TextCesarForm
from .algorithms.interrupted_transposition import interruptedTransposition
from .algorithms.Playfair import DesencriptarPlayfair

TEMPLATE_DIRS = (
  'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
  return render(request, 'index.html')

############# CIFRADO #############

#### INTERRUPTED TRANSPOSITION

def cipher(request):
  return transposition_cipher(request)

def transposition_cipher(request):
  if request.method == 'POST':
    form = TextTransForm(request.POST)
    if form.is_valid():
      key = form.cleaned_data['key']
      plainText = form.cleaned_data['plain_text']
      ciphertext, msg = interruptedTransposition(key, plainText)
      return render (request, 'transposition/result.html', {'result': ciphertext, 'msg': msg})
  else:
    form = TextTransForm()

  return render(request, 'transposition/transposition_form.html', {'form': form})

############# DESCIFRAR #############

def menu_decipher(request):
  return render(request, 'menu_decipher.html')

#### PLAYFAIR

def playfair(request):
  return playfair_decipher(request)

def playfair_decipher(request):
  if request.method == 'POST':
    form = TextPlayfairForm(request.POST)
    if form.is_valid():
      key = form.cleaned_data['key']
      ciphertext = form.cleaned_data['text_cipher']
      plainText = DesencriptarPlayfair(key,ciphertext) # Aqui poner la funcion
      return render (request, 'playfair/result.html', {'result': plainText})
  else:
    form = TextPlayfairForm()

  return render(request, 'playfair/playfair_form.html', {'form': form})

#### CESAR

def cesar(request):
  return cesar_decipher(request)

def cesar_decipher(request):
  if request.method == 'POST':
    form = TextCesarForm(request.POST)
    if form.is_valid():
      key = form.cleaned_data['key']
      ciphertext = form.cleaned_data['text_cipher']
      plainText = interruptedTransposition(key, ciphertext) # Aqui poner la funcion
      return render (request, 'cesar/result.html', {'result': plainText})
  else:
    form = TextCesarForm()

  return render(request, 'cesar/cesar_form.html', {'form': form})