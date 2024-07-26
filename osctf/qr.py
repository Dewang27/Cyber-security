from Crypto.Util.number import long_to_bytes,inverse,GCD,bytes_to_long
from random import *


'''flag = b'REDACTED'

p = 96517490730367252566551196176049957092195411726055764912412605750547823858339
a = 1337

flag = bin(bytes_to_long(flag))[2:]
encrypt = []

for bit in flag:
    encrypt.append(pow(a, (randint(2, p) * randrange(2, p, 2)) + int(bit), p))
    
print(encrypt)'''

from Crypto.Util.number import long_to_bytes

# The encrypted values
encrypted_values = [
    [22669242357499213108739139123540498576712276675707825520226104937626916961164, 37739668184440283669142551967709956128855334825882997559266083688111182240250, 25441665154628681485284503278748795972155196569837035753551875903751126142907, 35474505298556513912261603284362124842534115048111240988499653344464862347910, 71151726893269930043162595577071144115819190380361907433725654317094008784114, 73908762436740808052248681916206887963850159072530911859252452338379974236177, 57101936693938413660193888525274029620321481186566605918839145923743543515485, 50142333201706360628926860142168383004375393280107340032844355956106602452523, 66674223908870374966793234843060598734149612681545963187829047004109492467665, 75645951336401957433211616046598596196060464792740476510614442261473108101899, 94528733593743148889841689957696362251114835391113504434828558197260207590866, 338929841930217321055430137125845807027667700750167006527471975419285881175, 75088745144792582813916110577214942601913690860975091089436299911890274849516, 74394014010432727069604983822453343060373458821166358799217874034131664206428, 91221454312560232354241720239905868418614720160185328828194353719168557045934, 
89436045494785057136882190534245736811593108055016502277283940183490502024882, 36631994189142987353938811699895106669313412655518192297575560793247704071860, 49403836768060341935370936426818980205828912886168944869209309717919544869947, 5616873069301481432517730919085312761422493127537663227459245162137215060735, 75692295200755294854688807216380730178664527141203391464535121521209043834993, 15194708204076967436620162748020990752047142968672860194686090885307864541474, 27277222211574032304771363985383912197197327554327469597153300479846356132808, 45261613524045806253381673048386226694937942616980606201869397738899866905378, 26498263144816281499090104271140576634942820174774993262349660857222993248471, 87216049531517871472233771214866020579318469232551002046372594293084924479565, 61079631140009807983697771559698911811124899161770558765256300027873402624773, 40187385460801786365229051630671758050898348280702951477774368430993662284223, 19435004756275149573206597582697564506077159657516804306707743145398145728190, 60534803688140235437766737595053893019813287990331834061734276631971889937279, 17573561855930392335155769049734222227716957010154641579911147686774188998566, 
41403316081054585754934637071855801014515749681128353900785407130105322243984, 40362328775237311903945159656511902356255783631337123381232819980986120456505, 57384464268475230386821062576143029524498446034687355025688002978188223711228, 74708560803113835980340910678062550296115799591572427722008511140168307336323, 74935272654162080601713865548118116906970893658126663792668800521042780150102, 30676375144360278365095181463678017210742380110381246442386971233358605801174, 51218809129488243088667250185728056488185967028209708831208561153043218896914, 52667228342599779803395395514675913186746539512597988672827688776368848026404, 40594056301032510988069804296372301083061251058162211839008693187246371187689, 37290991127881086823246556743553921965773790053301868408488315804483282116318, 5746745299518583409738624442060864880649976464429203847655956078291015323024, 83142796591762846779423574172404777751215334009592343937308070283358587157918, 1706097043709823185789843875896794690811119846511423394258191917855932285445, 13959599257811926066796633697525167722734651987360297280847164040236153673966, 33518788862070124533164301115377784528680041802197136462152725129830513482288, 67884134834968989556778104209935732570770732953490080241251674446055336732267, 9122428024434962902595132465707738388892318405258337198964284798807832111183, 45219015459930012381528100022109703929142328005565688519969281228478587025156, 37937438320920938080194998531655411538645397488518809263576468548095334941049, 65463191167111256133850830561950011602415787482391546687108828852078336346911, 60267390775769712809243637108005516372054896996335986578776656061913988505380, 31187280205923216765025642712731268538092737496945912665477089963549936661000, 39272203117676991849401256050052660389252891090765421072850812790511853633553, 78650399942810180369166637327220488673491469759016027310017260378395192153917, 63679779865600882115457578102137190521431770150485077494234497317040310556099, 94197711842546391399936480688526532205484253031969515698149700461481218435503, 55426351612657722347952609331927607250320193708145787272479883713911328260171, 94579488448780631031570551761117560463614768969716618208863957906602543864256, 42533211515825827897607197697818367567724897911870487437227525480798959030736, 71817193990486711499448836892334029689594769863757209290780334731796075040964, 49582582372627092919996673631156116915578095143759344425462558619751837756115, 16778862498079304970130684233228282291061728198209025400841438773809486045439, 14720766794414702326013223598332514689730269727677755351121759524459792723815, 91823179796422607777458789555431412361727477658725342545633205873539390524421, 12694496938346057655349578497630025226490487986396361007943957007999746501758, 73256087035268026678251823321714291938230083291400455643716217526282587453490, 82067053864614955720331353764077356749839546969350079359806989229896280871639, 2294214511684098951448895697206660875590100097765398000960427914742478567468, 94996367172467362549072804695542787589471757112709399248918663083637674875430, 59474972193189900872036261980527256847598779519129004892669760035949359596606, 41485046826485366939559105778182279178776733141732587039714077484707517673414, 30412373303809291358251419626484743728420797010128289787459320584456794477728, 16757273319641017346460609339812262074112156687285784823742352746685264992379, 14153394449089890608134311960881667677866890754276351688174647355758384644208, 35267312148665588028133403157437977272702217909940645971373606689401454239924, 25465572937315970004671485436432326847481734301701086900680247656344895637489, 91772640899291600179884634716699977518176166265177845979210905419023385427169, 21202239116914803055046359653747295796716387504506260166689961462743702888272, 38004169931088542628056717769207753056395024570208499914119987227199372776609, 90200388178027170845901671405926529885003050744671942306854133475369592255284, 67103463297019868103506162494808639910142863443197903858998004329088015085523, 63711271696919572850260563707814751558803656037405411887337920717563822065752, 77668043054392826789311460278906027367647248204625519502878680145405861209190, 44569139842369210610100977433213151422864959112673084241197625375177236769097, 58443888034627936323756326700272770246863224271563209128177317645955486143403, 80851036613437865066354537941959631305841498627989280039977583470550685884031, 9021753887527487436199159854975234579459170761210967112439040341901658426878, 84387698184222592645514926620408729191662827277136602275202779173241313177512, 29589066716928530039314971637335850646071216993197616270416702240213988708218, 64726951774614639011075770690988313459581285735819050256715848241230131038358, 30500821175393449650880839482563016060280355078274606393428875534120413692351, 52518903414921155720607415198610600547400377020270396066959711966325275416218, 23587780722750722770275831382258422302869745535367947800297505821028954037171, 33414084368227213965052202768373969326135601029670262014942312319657066989279, 67712235194933598828927102315642664823927554129129073489793529336688516628376, 44555037196293370995200765960065412645438350638060651696204475599201076709237, 73006002456940502435655404506315494322512733852942509890976346775163427165310, 62703204333859958106441079329987788867826810342083200718161524691314631366192, 41360739245070421742301640606287372301286012210246939265330115507136267210529, 21524966058106637889690861152062902783679249838848325868661667338362305512605, 43553249569815730507179981484772699321159546492004250922181426029453077920079, 14297444443172990665307586017069954404946684905826170950127732631547063239665, 24801649245070520747846216461134075637301799914670831528569224459302974479910, 71792950629879690389862969053832052341534509142032062883899129973901240720300, 48990800423597725830976475702202144208371799233843252282437888550703983177871, 
58932401176503301188939484670758239439029400910940273819954708091952185128101, 29805329545570657187061054277681037842386998505222318319869493263184453237335, 15021531307879623848342180806906885935426313848470834110190625625842603446892, 68301407971708771621955668309504704919448633895470419327248228378437371071707, 9041464349332920322053492322397467090982581639189634512821125823846406612686, 11645745705922740709992328444030957451421417877718952690532310638657049342012, 51519900725182834651012610242386227837010938922312446801520177957974712078733, 44072901569695371905510566384412886394954631489325181572552132004876471926263, 2606048910031069923678310129611989877756680559818904877334463917523219457609, 75753391664218975184134365440412662853259852104152712468951238127372145976339, 15480514194144494756165942191551223126468735462611235289028554445294653717141, 19907633778461246967896664600495182499389474055142800242657274675739166803459, 89286628534912356047272665197390938286813366717592767552269206113618450939987, 27724319524510901684103616013027701443212064913957198385891885446777643746947, 38770117147346725679667410493958876599763936741087731663850249509589239785493, 65213064141729790434518900170350221145766268290137703560118563019872038545472, 25704540471861897687747270141706366995654183460471840204494658897334997899410, 65353972147881189621914437255471747539197260946549775695445665481738514018425, 36069772255465284610802002597370753632135897350479023749362126239947236277675, 18809654537942067000907702507841673030325079244794968097216484489611489035106, 3867306407828405923822343829963635592400348330249025324186683001404658494180, 73678870136284092359610021648501635899427042366666265069949512488413523159725, 48478244667566777439295217098581533365776702109187818027699849083490521359726, 84005115144173955512866423834950812997259510339179151333292546017897718331217, 37533207779115588974731425824672500768814451827290604489403885903799278408109, 62520882892756925687378853000041503608165019098415708109035365448936067075407, 85499048737699394218744193752544278618630199679756107562869131518958092363862, 95166408910762550632514932625225255516360966186280552697059772790259563372320, 37462475664148421034992033218613706530522104818289591891751450118252831347609, 94508256013291571790243986375559184516307754290264521542077092405054083703796, 65575664767021919088218400821682212721218608241034982140920541997560959832078, 69796871204916953128744037044487475274812991800348514457981101256036613662450, 71123466069972860915641815812956297172446932814780863255421860347745339199629, 63059270582688428236713604360977756712949795939221234541977720634978042557479, 2895225665369795341321356875129343263397212618538040274487630324221756395495, 65566307731462140194389734325472877491172365995570187411331075306139762031691, 67495500086827763496189943427683723468094947513106020864296576416747386551624, 47327207060445198242643423041825971662581649032249539703427514503618193886073, 63204694409902426108355501692976612908254464638403016377958775376484463511135, 58678775008860624636119162877531161014718979482142182771573146907326391425717, 95044055427287512366276936777264478827232704338437414982679688810793641069496, 82831529119748071029058540358860696342778528562238155536059617869845912700645, 43861224659586250512358671261916534919565134804576376429874826957318740209391, 65566917866614326229674768694805290458186567484087989784979570783651032452878, 38244169424037873706697845015870038778906775351079489415332867905622651749809, 960399506344712151036004621994096547805426885129053793447354781928718828195, 5817124209012913179571296814083271647384848077852052426002263275626218345025, 70843959224405026070085178283269324817986855784912640735177226071183254884180, 78893743676398216527680939638758475458781793761483387360338397232407930725502, 80085810695337939133588773854239299711553039209380726603692605277411409303966, 77251365454813869055486641660028450494651325862988383334727321218418560985376, 3251943778803976711286061838768710050216271276434532906629466523146190977265, 92459083556560234338584648642953484041505603211400792226006167449071904938087, 41315404555636554566353045264784979438558322501883993961664043314479122030982, 33667921732374812293555545145317542830269138082203394549564420337563511193264, 50621317952967079741222119913032402394225411815446734158547018570454283770610, 61538555407587216288628161469598279569212468026569037020569554472277505867860, 39606381801095228171182252714963949195391349029446098094433836311947366748974, 17953182036365687621683574841421811357208731161754128420243424237624005507292, 6190971254605091232451529905747605417656775783024123539018809172451881761215, 24900864704471553434195010048955554593325138038080996664735907228770196880560, 10543195327397254020284310322430207644894242960895519587035695647412134999016, 47924531000639762023673307267122638007581576823068862921870896068866633394171, 19608471008911567550722544831800884194350927182490432232297048805561567190068, 73186293738418227162466985240965059382406888048823737842292990865577384260402, 46543617838237527608676169663642406675114888125078816251773853670035125668327, 10887521163982995742665591212887572254641573865819852321227254297463369378757, 95864064768743007099114077501237604640804188923396179519872005842740443029053, 93491158725857563983450270953464865480053052171181924427857859244709726666071, 66825162565490641340913352156970328411699085617818733870637467906069035138441, 88654055348896157513190254742817045113247315845423358391652859909742319633366, 77111213038828555934590491117487574876536940586374816487888235710362552865868, 26678676680954697758157596968058851948710733628229767222823914638197415347290, 45274196742261399015310184050782710721838593098302997420730602792248829914662, 11127057880291193918266637875818674553751410261869322342628348401264220296286, 93462971473448293984429493262651106641176064756281135412131328283064855378988, 90302791214563481426594767957092003195180657420583244979056724424177116030853, 15313848593678085835799518445701439801201857788077887972051482039480548393637, 28614362238386344451433803011769862093332477963804536169743753131346648335975, 96491672177543312015480691847973658772711259385679857934718873155088408055046, 42301694889548951016246284894329404464594688959616187013899635091103337836717, 46353007060252533455483227916744905299151183342666007163476701567951253528736, 79839703062477374459886524392435098801822289144847449478702368595623902987680, 46783400551087333523958538798205546101411729752062735369103520262740178438753, 56872651091298734129449461270914178234764299121906396309921602466898140304365, 55345094401475685162234185361328679014862432225300545395490433120615543516349, 71857988633674287131692935982565878924171301998834033964230950051788343943421, 73397553618456249814488665236594681860325090363523487802693708209869330880507, 91273817268449052212505869236740446096003331079462740258133485266870552861006, 41125713977491932720809445466298017068859216103887924591071386105259166186610, 10976272927609182135453062171314099889424242502585646696510784536426947241849, 74833007251806404834992968420737342446360952912467741893229250823477851895274, 38783541642734736023791760201077416997507081321013703558508973853069710934783, 84248864059313265407718358918343928748160949336813609666210932674632143654824, 82602002119241454477141450021218821487564602836760639860648023592499587185856, 89819647896782114807682181082759429437661708787869659336592879965813906997708, 23947255344454489668491857346046788876253021175185681444747952805430910288653, 45079677286325826130627514645496230345783737235639911042111222603703961525471, 31422315820021970621139404712399912221539882071460492381363799041483199779170, 78319051979712454760132140327765937454261888111097632383458050081958251932718, 13195058600578339298317331174447828396628584821721804422117397583118862095468, 76331308821686112269980476446767367482076206695320817648912917023040484744371, 85170210949791075377874335436657985171655895727142420005420448205376733873316, 82555492183656104712338936014903798922258809238013067932914827160603637621174, 12853005456280472788501210198110293457770020153015023657261972261311335921418, 54248544836879684654909756290276457357272919419446162758946246806760522100711, 87867368966726802666208924336758462717985240907205754302063242165609320760427, 73987307448912593135218860198268250462112582891066381555467243973016617080097, 62034957522597381807235151354312171918753368363851082317347374304031679600835, 71522279909103982493300281091673068587691535938891602681331258161179646018191, 47335993876757842828698766773477345247204614564806619542087825435513112987645, 48773159050572757429890800098259949250072566477582372396422636674323769400104, 31226180332173013494837685738648368082411434224960692624560991892476408389960, 59749707224753370726933899896607122727427655755816079818836748123403303618382, 13766045506333347863667381014672985531647803309594301027648194094171298738229, 90335253544133308792500347574392037813202491123760375294542737540752624583995, 95170606184823264968832958138783311990043706962099995010700617639475230600727, 55404200670899879712624286794610841624897767385622505408175747048711395105465]

]

p = 96517490730367252566551196176049957092195411726055764912412605750547823858339
a = 1337

# Decrypt the values
decrypted_bits = []
for value in encrypted_values:
    decrypted_values = [pow(v, -1, p) for v in value]   # modular inverse
    bit = [(dv - a) % 2 for dv in decrypted_values] # assuming the encryption used a similar bit operation
    decrypted_bits.append(bit)


#print(decrypted_bits)
decrypted_bits=[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1]
# Combine bits into bytes and then to the flag
flag_bits_str = ''.join(map(str, decrypted_bits))  # Convert each bit to a string and join them
flag_int = int(flag_bits_str, 2)
flag_bytes = long_to_bytes(flag_int)
print(flag_bytes)

