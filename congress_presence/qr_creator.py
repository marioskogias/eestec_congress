from models import Participant
import qrcode

def create_qr():
    data = "http://eestec.ntua.gr/congress2014/#%s"

    #participants_stuff
    participants = Participant.objects.all()
    file_name = "qrs/%s_%s.png"
    for p in participants:
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data % p.id)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(file_name % (p.first_name, p.last_name))
        except:
            print p
