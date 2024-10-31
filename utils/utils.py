class utili:
    def __init__(self):
        pass

    def CleanEstadoCivil(self, arg):
        if str(arg).upper() in ['SOLTEIRO(A)_x000D_\n', "SOLTEIRO", "SOLTEIRO(A)_x000D_\n", "SOTEIRO(A)", "SOLTEIRO (A)", "SOLTEIRA(A)", "SOLTERIO(A)", "SOLTIRO(A)", "SOLTERIRO(A)", 'SOLTEIRA']:
            return 'SOLTEIRO(A)'
        elif str(arg).upper() in ['CASADO', 'CASADO(A)']:
            return 'CASADO(A)'
        elif str(arg).upper() in ['DIVORCIADO', 'DIVORCIADO(A)']:
            return 'DIVORCIADO(A)'
        elif str(arg).upper() in ['VIUVO', 'VIUVO(A)', 'VIUVA', 'VIUVA(A)']:
            return 'VIUVO(A)'
        elif str(arg).upper() in ['SEPARADO', 'SEPARADO(A)', 'SEPARADO(A)_x000D_']:
            return 'SEPARADO(A)'
        elif str(arg).upper() in ['UNIAO ESTAVEL', 'UNIAO ESTAVEL ', 'UNIÃO ESTÁVEL', 'UNIAO ESTÁVEL', 'UNIÃO ESTAVEL', "UNIÃO ESTÁVEL_x000D_\n"]:
            return 'UNIAO ESTAVEL(A)'
        else:
            return 'PREJUDICADO'
