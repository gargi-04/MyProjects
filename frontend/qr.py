import qrcode
import qrcode.image.svg
from io import BytesIO
from backend.models import Ticket

def qr_generation(qr_content,ticket):
    context = {}
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(qr_content, image_factory=factory, box_size=20)
    img1= qrcode.make(qr_content)
    stream = BytesIO()
    type(img)
    img.save(stream)
    img1.save(str(qr_content["entry"])+".png")
    #ticket.QR_Code=qr_content["entry"])+".png"
    context["svg"] = stream.getvalue().decode()
    ticket.qr_svg=context["svg"]
    ticket.save()
    return (ticket)