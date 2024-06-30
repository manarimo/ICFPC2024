-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I19728

-- Pass the encoded string
B$

-- Bind the expanded dictionary
B$
L#
  -- Make the recursive function of Decode
  B$
    Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx -- Fix

      -- Decode :: Self -> String -> String
      -- Decodes the first entry in the source then recursively process the rest.
      Ld Ls
        ? ( B= vs @I16 )
          S
          B.
            BT @I2 BD (B* @I2 B% vs @I16) v# -- Decode the first entry
            (B$ vd (B/ vs @I16)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I32
-- Apply the compressed dictionary to obtain the dict
B$

-- Make the recursive Expand function
B$
-- Fix
Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx

-- Expand :: Self -> Int -> String
Le Lp
  ? (B= vp @I0)
    S
    B.
      BT @I1 BD (B% vp @I4) @SLRDU
      B$ ve (B/ vp @I4)
@I32257358805572780821

-- Encoded string
@I44881674261207555068671380294432714337555589466401595728088305720104146270304988955614172580671311850027364621665267514772505802567909993423354843552435164477152435949551863696837359838884644434441660285742892414862357406500428024114410774590778493572691469266651280652328122248867269498157749533040720235012401474963101578275950852975048175455606241357839723182375268654027814831033547201295442038147503910671033751190851907789790253666615039414787468638805752413050792458917651284521643034859013021343341366598324716025565759476029822979954405920575351812722943160076054439175910195625356627067050647391335796300257047374145346571240344511704109824230303894465632062441619871780030110866392645849927088138729352950834688408316117252762582592323848056824249001120206748048353875868894416534248092386372573137057585408480674840049439993010526650519055713024470377793507401040459217899515214524505774756748577040499219150625854249799654270800106166256576310765240386806495864921131241460253676904920644268186059435175639131946216485671859604430791690903772758232970227547631015932407792876049414552086017549752632727274971837420759118114647593483907500929780623577193199697875402310770196876700591790427233705976814295655461505138261570584359381766626442015589743284613728551621760515573368731731127102277724258351899862570265494262474843270626501522895506959354220223849858164343358794698589623722663485820496024290706453852991337746184994288480418292486846303646604425066304131868738045295546100367953813265111432473945280186181331656726617831520672281234498505367159263170440787611463269529584893672234726947200234015158046346033772710517885619184201845686720679969135157919686731811011636923574032047872133148038502009542267207935473889852643921380890138816524389246155448932008974281266086335824249064902206917869247279779088449591329327362239725770864656034749705275807900108112667535676923534552182848907876984205819954919132384588689924786787606928441088553654392616532772314879130008036398167695240539006555395666402191304970107958659807767640229470064700432182322931388089672363658673092242592325757197722908459588361155771549208369689873933811276365772007041092587141466761244811338356683742883687922876893327246935392871349332031738742109899720430214631893918493072925182611212813297012729923828246837977643098368160012911949777058186131603497779496300310268077249205243616975848106805563558174830232023863428052030012938652628332437954019009386804511928384232612145261175448587703386843349733107412303770363881431075391083668048402917236688206670707886873421353886727061439178156129923355424962993480571001410433536480179946406008817273884694978465430226963730811092756584619876574055708909728646505095734662616821640813755985284455821499078524654367311699912324256313115359086289473276562850497364682200510974065602665423675672429143996689277591235629731692520461334465396339864185865673514902244539661409376250694150784018385092793031673599441374018837606311625916853314368061542831224181269844654891310264922357443374798292968834188598404461555798379768105348902975188016076841071461156539862511419108244451422287265904314118104348097880702950632875288679533791760608636275655568806920936675621532381545835537936130793894532171156815172267898238788524103733124014976631645495229507191706001033131545185653236769963179988212201643903755424093197167286761134865423311403358871707028252182060583360950523226433793092691595145762033250178094875705662972036889651901891115918272281688199135494836616512364101855305976281965732524019028983100589193208919281470883129324315540469859942729852044095743141716479397872863346584649568738753811161817586651493219961141941482630582575504723275965355460723369087754790939097310922256502186468687640145393688500029814977229793089113950292477234131653570908205038755819201677127720986233448649378414726452903497901226277539805255677981732301708312556105352525077786350600301371050921664304905444164327276793626678659450243973547180475195953513433562698140516550102069376232094730258021315953562885418671975862256623970966776796262211915694007271013482450345531499564190254063870102288735742528533753340549267130440422512843090838500363527294206516219051247451139840333779888439123012584172665246106791267825740112532697045572415760357540229921394407852913299070240144536709360187767660950498962137566804265298708616898445053054304201175745754516866838096401129690833718643813716664041790764191771639419966093554520692847862362210265145757687318464176713203470054355186307156524536930063054772492486602299415016493281962742340854681151597749150705320570918907465548715500112748176054603129967881997294768330712548723902460292070530973113393338830953138581013053586266274540465242857521650051036952784370610118876963805330627553093875732523739667307562886636607985936541531486965274133926266821221921894437845374001283277578572321472541655018629878781034280630450936050704566837940524336308876232250220076715993234445362049031815732534679255537471312935030760560406551502405001952589243171031689241478907805497238647384062443884174531357441269401143800586565596551404216493732950498887509109185423327898941761158752307748543390721475260861799286632348372728315098081462607355695941014091195564917421898993861491584205056559440194275116149718503708062621066505811212898691363518086494453496952609293732315896772810963352194954997445598816293663193907386533045196368096904399080584522058973687701779615545905941187984592731290342831525825027709878475679013455703694678784715787598515382187872994094207621148511194324581268203761533076708557210366314924187417245832744487988132757604216419553208896441368930411913933829844212532044586491628359476848406751780839670388842373260269844106020026582903298102615029715231397744944038879680766086833003933187440352637823071785233970974844988204886525644678876138802484768280026690232941693772782544051241110606727315830737898661924753597143794010099960851475841181622652524041849265154964463415550857070843506111842577720479398346326711537164415082458721458369359743272744189092369883151133580813337437177272326559927137735942288961443028723632355384100125104646737739499881840443778864640921981273694400468247751616187781667497333206746271626684357079133075243653782788902139748113859856175078153993452822554570374045167513394647842965263473067380050767426717140314559495456266355655590503760217760188893334373481275514952579524121166385335857583721336390376138270884606703942849962190840862935414149618862165769181361932708161795144109137398075088781540869810515749033510598266196313753833856186809476073037700241629691263412269479506074397316942990155706293267419745848377747248784300123526089106972038139238161317010263754574495279329527550334189619131665468949329389553614151418395639693589088912429649953098141828973096001303600148874557017381751141068568108617523288721031148916309709558219782935736091526982058550457888801529855063658705760031820635661492549496711065631417723101050268838302644973988018899259596039787711077469950583598056535125493902321824321264135376267388916680951058635881052630992878447528564085554054047211391053105010611091598814915336183917147768161308220771663488883406352096183530264627905830239119482824016355155776582647022998781731161477909514130428058930392340603607804114558725898990064367006825668883425224310553323995941824431574511788128376918878317879771341971527503892853639499097561942173034328604954026718162635069309617408225651826324470650708663074541417136960117259333389501912834016629411614468504173673997277835710186849002697092545985714386502402209600004887685397641402746523244293335366971399345347971946557249556308178809722745069123930993367891732557608936543164692798087756509556789054808790128956221956585731733362595014804678127341448251046857494717966435023472346163029957527082037798534661080941503863984664658491495316731357264850379905565263291653891885570455568164181992611334316890875902976499507784539985836315698230590554912295211805464506730675073429782637773740596441702425247623298871204533905485009151265099722118442421546359942111872567961236063776372927021372468439061959416540401924727221886622598478799636980443010023994204413096894140404113613556568953186725158427248617318680898832349053024658881591999858573486797101910723799197359005478523464122800773829642023748665581422816751041894823256234477495480178065867619408841791545576242192775628664000432376545787329780238876038412448038605712269577997836217968010450818212107780754046391829609952629456534672737254981714129352202146017496067331191289838016778611327832660095116584008360530019644109312419721928721245757695671573951136810160340956533056018234100500859107363125450815703460468966242439890554119184597077519409553809359072705744188375562912204025632924716279535719880144753107116396048716649811867267191592908549305348775018619687212119445826711196755312149110113257319320644293011923948574868743953156081240646991126801458928199395465631320014183050906277285785321276371570414533558192332242604169530622903118853307163195496297763684845735105558021981841719996038599756283208905617438491503795463073325457040376609806394835853316893616264101760042626780723444737378362132403510823201770600699728983287294597873682795943333900412128317841719549102957096692443904193027745411439317344729017437219750575018740872718119696813416586018589949642031355236334693088876283902098709741740043339976794859878753248215701663297959421236943843479792151693426853560614984857128523334417302282321711753622984194053723133759588761453667112895395889873265401511651068003182547930469478820612560883994297585733485568315120345319542180929189603921624383859170699987056927129842914489558311028302038968238388702961956616730056392303774934249734151321616813275941495868144260675331799539711138692177349570695807065900332176568641938253311730319171006882916946153559844785827025854605430356761332056766466947859204645793479761028689285599950479355183781031715693989411112746038318895787867453447803887581811519936970888789942475305505919922305349600836740370584403824453389136562528621282115069353900787122205451599151597486206566384136692098588861627175790599115851473229704557864276303267265024687851218700803420148489868165490011652410618859348849053045766957880959372762954038412102713474551377784760792529511590094774771713375573095445147365617136519899222673181001948718052262791200269302277121372206553107975805377422196030269233877888449400982434053695382673715434255342121066841461015088751071556518149469500325546822704998956840834313605643477478154927492077772863792389291150487424768577956671157441774469685449758505247532110193671114373773882268837997889671896792675185002742420121916168767459298433195376647650696997764960826939428024247284959431936014446033314768018111067755972344012420959193857980034213303797219408258318712420857897849662724958571727679082399304799539974901083291220413473083445335704582120110872423730763967935221777881655732427146489595037980725264746976372009736603902512910407639618330817965309809319764375335584198931548929152035740034601516872198864296489279660775608556994801346420190737263062136577856787364925952515475220735218084566781809382531451316815506434460808798442839015409069287169745043995474934313485411805917159804608371242270264066496812202861490911928433336988205265355517936536349348342453694221746057983155876272924300955192931933841786462931893217289755133943549030202754627047243835960621118960773426170059413632672208987124080227824272069626104868332631792849135558067754439280764316676577254364341349857505028553437505474563575503677201600052990213901760887197470793858608256189927979887312485335134067546585729533258177869801150984618925779420401758255345079835530340999673874124976533097358064431499906512926359649162919245456747422205576857227510869614193176967510680987533286337731226637512913916476260352


