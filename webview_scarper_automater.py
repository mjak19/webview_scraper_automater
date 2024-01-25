import webview
from IPython import start_ipython


def custom_logic(
	window,
):  # this will open an ipython shell and then you continue your web automation scarper in runtime using python language . however you will interact with webview using javascript strings , if you like
	start_ipython(argv=[], user_ns=locals())


window = webview.create_window(
	"web scraping",
	html="""
	<h1> 
		use python in your terminal to instruct me
	</h1>
	<br>for example type window.evaluate_js("window.location.href='https://www.google.com'") 
	<br> 
	<a href= "https://www.google.com" > 
		google
	</a>
	<br> 
	<a href= "https://www.yahoo.com" > 
		yahoo 
	</a>
""",
)
webview.start(custom_logic, window)
