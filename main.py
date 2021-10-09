import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6DnaMwWaVH844btosu9npilm1TvJwYyYHz1qMIuIQeu9TrLpCkG2Kvhw4rxuvUHx-1xBpTrzVQs3uCKyT4gowlYihhR_Izlxqc7m6pvCs7albkGtkEpjOQX93_b1dye15jZfzU'
    transferData = TransferData(access_token)

    file_from = input("ENTER THE FILE PATH TO TRANSFER : ")
    file_to = input("ENTER THE DROPBOX PATH : ")
    transferData.upload_file(file_from, file_to)
    print("FILE HAS BEEN MOVED SUCCESFULLY")

main()