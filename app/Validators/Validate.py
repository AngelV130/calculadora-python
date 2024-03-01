def validate(data, validates):
    errors = {}


    for elemento in validates:
        if elemento['name'] in data or data[elemento['name']] or data[elemento['name']] == 0:
            if not isinstance(data[elemento['name']], elemento['type']):
                if elemento['type'] == float:
                    if not isinstance(data[elemento['name']], int):
                        errors[elemento['name']] = elemento['name'] + " debe ser de tipo " + str(elemento['type']).replace("<class '", "").replace("'>", "") + "."
                else:
                    errors[elemento['name']] = elemento['name'] + " debe ser de tipo " + str(elemento['type']).replace("<class '", "").replace("'>", "") + "."
        else:
            errors[elemento['name']] = elemento['name'] + " es requerido."
            
    return errors