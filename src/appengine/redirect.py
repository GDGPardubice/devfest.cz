import webapp2

class AllHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://www.devfest.cz", True)

app = webapp2.WSGIApplication([('/.*', AllHandler)])