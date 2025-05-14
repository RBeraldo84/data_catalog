# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from datetime import datetime
# import os

# def gerar_pdf(solicitacao, steward):
#     # Criação do buffer em memória
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer, pagesize=letter)
    
#     # Definindo as informações do PDF
#     c.drawString(100, 750, f"Solicitação ID: {solicitacao.id}")
#     c.drawString(100, 735, f"Nome do Solicitante: {solicitacao.solicitante_nome}")
#     c.drawString(100, 720, f"Data da Solicitação: {solicitacao.data_solicitacao.strftime('%d/%m/%Y')}")
#     c.drawString(100, 705, f"Nome do Aprovador: {steward.nome}")
#     c.drawString(100, 690, f"Data de Aprovação: {datetime.now().strftime('%d/%m/%Y')}")
#     c.drawString(100, 675, f"Nome da Tabela: {solicitacao.tabela_nome}")
#     c.drawString(100, 660, f"Hash de Verificação: {solicitacao.hash_verificacao}")
    
#     # Salvando o PDF no buffer
#     c.save()
    
#     # Movendo o ponteiro para o início do buffer
#     buffer.seek(0)
    
#     # Definindo o caminho para salvar o arquivo PDF
#     output_path = f"static/pdf/solicitacao_{solicitacao.id}_aprovada.pdf"
    
#     # Salvando o conteúdo do buffer em um arquivo
#     with open(output_path, 'wb') as f:
#         f.write(buffer.getvalue())
    
#     return output_path
