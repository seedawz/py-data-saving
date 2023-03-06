def writedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('สบายดีไหม')
def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        file.write(text)

adddata('วันนี้วันจันทร์')
