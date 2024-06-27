from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email_usuario = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage(
                "Mensaje desde App Django",
                f"El usuario con nombre {nombre} con la dirección {email_usuario} escribe lo siguiente:\n\n{contenido}",
                "", ["hernanrmarce031105@gmail.com"], reply_to=[email_usuario]
            )
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")
                
    return render(request, "Contacto/contacto.html", {"miformulario": formulario_contacto})
