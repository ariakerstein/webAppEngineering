import os

import jinja2
import webapp2
import asciichan

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		items = self.request.get_all("food")
		self.render("shopping_list.html", items = items)

# # class MainPage(webapp2.RequestHandler):
# #     def write_form(error=""):
# #     	self.response.out.write(form % {"error": error})

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


#     # def get(self):
#     #     self.response.out.write(form)

#     def post(self):
#     	user_month = valid_month(self.request.get("month"))
#     	user_day = valid_day(self.request.get('day'))
#     	user_year = valid_year(self.request.get('year'))
#     	<div style="color: red">%(error)s</div>
    	
#     if not (user_day and user_month and user_year):
#     	self.response.out.writes(form)
#     else:
# 		self.response.out.write("Great! that sounds like it'll be time well spent.")

# class TestHandler(webapp2.RequestHandler):
# 	def post(self):
# 		q = self.request.get("q")
# 		self.response.out.write(q)


		### The content below will return the request headers for debugging purposes ##
		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.out.write(self.request)






