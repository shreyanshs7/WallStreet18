import os, sys, schedule, time, random, json
sys.path.append('/home/shreyansh/DjangoProjects/WallStreet18/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")
import django
django.setup()
import datetime
from datetime import timedelta
from tornado import websocket, web, ioloop
from SellBuy.models import Share, SharePrice

# def share_price_update():
#     share_obj = Share.objects.all()
#     for share in share_obj:
#         # Changing each share price
#         old_share_price = share.current_price
#         new_share_price = (old_share_price) * (random.uniform(0.7, 1.3))
#         new_share_price = round(new_share_price, 2)
#         new_share = SharePrice.objects.create(share=share, price=new_share_price)
#         new_share.save()
#         share.current_price = new_share_price
#         share.previous_price = old_share_price
#         share.save()
#     print("Share price changed")
#     return True
    

# schedule.every(10).seconds.do(share_price_update)

class WebSocketHandler(websocket.WebSocketHandler):
  # Addition for Tornado as of 2017, need the following method
  # per: http://stackoverflow.com/questions/24851207/tornado-403-get-warning-when-opening-websocket/25071488#25071488
  def check_origin(self, origin):
    return True

  #on open of this socket
  def open(self):
    print ('Connection established.')
    #ioloop to wait for 3 seconds before starting to send data
    ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=3), self.send_data)

 #close connection
  def on_close(self):
    print ('Connection closed.')

  # Our function to send new (random) data for charts
  def send_data(self):
    print ("Sending Data")
    #create a bunch of random data for various dimensions we want
    share_obj = Share.objects.all()
    for share in share_obj:
        # Changing each share price
        old_share_price = share.current_price
        new_share_price = (old_share_price) * (random.uniform(0.7, 1.3))
        new_share_price = round(new_share_price, 2)
        new_share = SharePrice.objects.create(share=share, price=new_share_price)
        new_share.save()
        share.current_price = new_share_price
        share.previous_price = old_share_price
        share.save()
    print("Share price changed")
    data = ""
    for obj in share_obj:
		data+="<tr><td class='center'>"+ str(obj.current_price) +"</td></tr>"

    #write the json object to the socket
    self.write_message(json.dumps(data))

    #create new ioloop instance to intermittently publish data
    ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.send_data)


if __name__ == '__main__':
    print ("Starting websocket server program. Awaiting client requests to open websocket ...")
    application = web.Application([(r'/static/(.*)', web.StaticFileHandler, {'path': os.path.dirname(__file__)}),
                                        (r'/websocket', WebSocketHandler)])
    application.listen(8001)
    ioloop.IOLoop.instance().start()
