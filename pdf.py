import PyPDF2

def extrair_informacoes_pdf(caminho_pdf):
    informacoes_encontradas = []

    with open(caminho_pdf, 'rb') as arquivo:
        leitor_pdf = PyPDF2.PdfFileReader(arquivo)

        # Itera pelas páginas do PDF
        for num_pagina in range(leitor_pdf.numPages):
            pagina = leitor_pdf.getPage(num_pagina)
            texto_pagina = pagina.extractText().replace(' ', '')  # Remove espaços
            print(texto_pagina)

            # Procura por palavras-chave
            if 'Nome' in texto_pagina:
                print("Nome encontrado")

            if 'Instructor' in texto_pagina:
                print("Instructor encontrado")

            if 'Data' in texto_pagina:
                print("Data encontrado")

# Substitua 'seu_arquivo.pdf' pelo caminho do seu arquivo PDF
extrair_informacoes_pdf('Model.pdf')
