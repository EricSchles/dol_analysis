import requests
import lxml.html

r = requests.get("https://www.dol.gov/agencies/ilab/resources/reports/child-labor/afghanistan")
html = lxml.html.fromstring(r.text)
results = html.xpath('//div[@class="field field-name-field-i field-type-text-with-summary field-label-hidden"]')
import code
code.interact(local=locals())
