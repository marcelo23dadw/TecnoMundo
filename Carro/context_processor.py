def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session["carro"].items():
                total += float(value.get("precio", 0))
    return {"importe_total_carro": total}
