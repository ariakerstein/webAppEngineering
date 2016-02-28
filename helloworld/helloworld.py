import os


import webapp2

form="""
<form method="post">
	What is your birthdate?
	<br>
	<br>
	<label> Day
		<input type="text" name="Day">
	</label>

	<label> Month
		<input type="text" name="Month">
	</label>

	<label> Year
		<input type="text" name="Year">
	</label>
	<br>
	<br>

</form>
<br>

<form method="post">
	What will you work on?
	<br>
	<label> Role
		<input type="text" name="Role">
	</label>
	<br>
	<label> Objective
		<input type="text" name="Objective">
	</label>
	<br>
	<label> Flow Block Title
		<input type="text" name="Title">
	</label>

	<br>
	<br>
		<input type = "submit">

</form>
"""

class Handles(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)


class MainPage(Handler):
	def get(self):
		self.write("Hello, Ari")

# class MainPage(webapp2.RequestHandler):
#     def write_form(error=""):
#     	self.response.out.write(form % {"error": error})
   

    # def get(self):
    #     self.response.out.write(form)

    def post(self):
    	user_month = valid_month(self.request.get("month"))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year'))
    	<div style="color: red">%(error)s</div>
    	
    if not (user_day and user_month and user_year):
    	self.response.out.writes(form)
    else:
		self.response.out.write("Great! that sounds like it'll be time well spent.")

# class TestHandler(webapp2.RequestHandler):
# 	def post(self):
# 		q = self.request.get("q")
# 		self.response.out.write(q)


		### The content below will return the request headers for debugging purposes ##
		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)





