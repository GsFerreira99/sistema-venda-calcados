import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def filtro_dinheiro(valor):
    try:
        dinheiro = float(valor)
        return moeda(dinheiro)
    except:
        pass

    try:
        dinheiro = valor.replace(".", "")
        dinheiro = dinheiro.replace(",", ".")
        return moeda(dinheiro)
    except:
        pass

    return moeda(valor)

def converter_string_float(val):
    try:
        return float(val)
    except:
        try:
            return float(val.replace(",", "."))
        except:
            return float(0)

def limpar_dinheiro(val):
    return converter_string_float(val.replace("R$ ", ""))
 
def limpar_porcento(val):
    val = val.replace("%", "")
    return converter_string_float(val)

def converter_string_int(val):
    try:
        return int(val)
    except:
        return 0


def mascara_porcento(val):
    limpo = limpar_porcento(val)
    return f"{limpo}%"

def moeda(valor):
    try:
        valor = float(valor)
    except:
        valor = limpar_dinheiro(valor)
    return locale.currency(valor, grouping=True)

    
