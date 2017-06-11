from docxtpl import DocxTemplate, RichText

from docxtpl import DocxTemplate


doc = DocxTemplate("test_files/test.docx")

context = { 'name' : "World company", 'ip':'127.0.0.1'}

## 보고서 자동화 
## 정형화 보고서는 
doc.render(context)
doc.save("test_files/test01.docx")