
import re
def clean_text(text):
    text=text.lower()
    text=text.replace('c++','cplusplus').replace('c#','csharp')
    text=re.sub(r'[^a-z0-9\s]',' ',text)
    return text.replace('cplusplus','c++').replace('csharp','c#')
