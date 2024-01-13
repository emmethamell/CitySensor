import requests

class Helper:
    
    #RETRIEVE HTML
    #Takes: url, Returns: html or error message if fails
    @staticmethod
    def get_html(url):
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            return html_content
        else:
            return f"Failed to retrieve the website: Status code {response.status_code}"