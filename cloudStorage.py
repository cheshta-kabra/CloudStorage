import shutil
import os
import dropbox
path=input('enter the path of the folder to be sorted')
listoffiles=os.listdir(path)
for file in listoffiles:
        name,ext=os.path.splitext(file)
        ext=ext[1:]
        if ext=='':
            continue
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        else:
            os.mkdir(path+'/'+ext)
            shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
class TransferData:
    def __init__(self,accessTocken):
        self.accessTocken=accessTocken
    def uplodFile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accessTocken)
        with open(filefrom,'rb')as f:
            dbx.files_upload(f.read(),fileto)
def main():
    accessTocken='16MdDNmUwUYAAAAAAAAAAdNG2KtcEtAsrsOjGHdzLFePzld34Xy4yq4Uv4jfvgm9'
    transferData=TransferData(accessTocken)
    filefrom=path
    fileto=/storage
    transferData.uplodFile(filefrom,fileto)
    print('File Uploded!')

main()




