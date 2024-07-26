from Crypto.Util.number import long_to_bytes,bytes_to_long
import binascii

ct= "990a4695d825e060635354574bb1ffeb961ecbf6982cd4d156426f2e4ea123a15ab8102eeb09ecbeec916b0bccf98ba644f8644820a4f6d96abffe4d7844c26190d029204f41a08550a451b59c53e29a2040751a1742f3d1246cb49bc0c0fe473926bd6660411847938d7656f83274cbe7edeb251f623a786b67960515be7e29"
ct= binascii.unhexlify(ct)
n = 551504906448961847141690415172108060028728303241409233555695098354559944134593608349928135804830998592132110248539199471080424828431558863560289446722435352638365009233192053427739540819371609958014315243749107802424381558044339319969305152016580632977089138029197496120537936093909331580951370236220987003013

p= 21882732364928750538091629675163778162621616902577425071608324988253617272412493782388559800841168348434069674472295196720416514385081750301694228136439127
q= 25202744211817605397350328299983891415826580931890036611534540754079335081397262505214808536988764318124618606869256238502481259725033526700937302921554819

e = 65537
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(bytes_to_long(ct), d,n)
print(long_to_bytes(m))