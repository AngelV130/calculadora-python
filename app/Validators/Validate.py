def validate(data, validates):
    errors = {}


    for elemento in validates:
        if elemento['name'] not in data or not data[elemento['name']]:
            errors[elemento['name']] = elemento['name'] + " es requerido."
        else:
            if not isinstance(data[elemento['name']], elemento['type']):
                if elemento['type'] == float:
                    if not isinstance(data[elemento['name']], int):
                        errors[elemento['name']] = elemento['name'] + " debe ser de tipo " + str(elemento['type']).replace("<class '", "").replace("'>", "") + "."
                else:
                    errors[elemento['name']] = elemento['name'] + " debe ser de tipo " + str(elemento['type']).replace("<class '", "").replace("'>", "") + "."
    return errors