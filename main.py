import qrcode

gen_code = qrcode.make("https://cetonline.karnataka.gov.in/kea/")
gen_code.save("qrcode.png")
