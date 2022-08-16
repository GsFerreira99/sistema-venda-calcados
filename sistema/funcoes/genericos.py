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

    
def cpf_cnpj(val):
    if len(val) == 11:
        return f"{val[:3]}.{val[3:6]}.{val[6:9]}-{val[9:]}"
    elif len(val) == 14:
        return f"{val[:2]}.{val[2:5]}.{val[6:8]}/{val[8:12]}-{val[12:]}"
    else:
        return val

def celular(val):
    if len(val) == 11:
        return f"{val[:2]} {val[2:7]}-{val[7:]}"
    else:
        return val