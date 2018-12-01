#!/srv/homeassistant/bin/python3
import lxml.html

root = lxml.html.parse("http://www.cityofmadison.com/residents/winter/parking/al
ternateSideParking.cfm")
roadside = root.xpath('//div[@class="clearfix"]//strong//text()')[0]

print(roadside)