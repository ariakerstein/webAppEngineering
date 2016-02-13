def escape_html(s):
	for (i, o) in (("&", "&amp;"),
					(">", "&gt;"),
					("<", "&lt;"),
					('"', "&quote;")):
		s = s.replace(i, o)
	return s

print escape_html("<br>html!</br>")
