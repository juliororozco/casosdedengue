import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table, TableModel
from geopy.geocoders import ArcGIS
import plotly.graph_objects as go


#diccionario de datos para mostar municipios  y departamentos en la tabla
dpto_mapping = {
    '5': 'Antioquia',
    '8': 'Atlántico',
    '11': 'Bogotá D.C.',
    '13': 'Bolívar',
    '15': 'Boyacá',
    '17': 'Caldas',
    '18': 'Caquetá',
    '19': 'Cauca',
    '20': 'Cesar',
    '23': 'Córdoba',
    '25': 'Cundinamarca',
    '27': 'Chocó',
    '41': 'Huila',
    '44': 'La Guajira',
    '47': 'Magdalena',
    '50': 'Meta',
    '52': 'Nariño',
    '54': 'Norte de Santander',
    '63': 'Quindío',
    '66': 'Risaralda',
    '68': 'Santander',
    '70': 'Sucre',
    '73': 'Tolima',
    '76': 'Valle del Cauca',
    '81': 'Arauca',
    '85': 'Casanare',
    '86': 'Putumayo',
    '88': 'San Andrés y Providencia',
    '91': 'Amazonas',
    '94': 'Guainía',
    '95': 'Guaviare',
    '97': 'Vaupés',
    '99': 'Vichada'
}
dpto_lap = {
    '5': 'Antioquia',
    '8': 'Atlántico',
    '11': 'Bogotá D.C.',
    '13': 'Bolívar',
    '15': 'Boyacá',
    '17': 'Caldas',
    '18': 'Caquetá',
    '19': 'Cauca',
    '20': 'Cesar',
    '23': 'Córdoba',
    '25': 'Cundinamarca',
    '27': 'Chocó',
    '41': 'Huila',
    '44': 'La Guajira',
    '47': 'Magdalena',
    '50': 'Meta',
    '52': 'Nariño',
    '54': 'Norte de Santander',
    '63': 'Quindío',
    '66': 'Risaralda',
    '68': 'Santander',
    '70': 'Sucre',
    '73': 'Tolima',
    '76': 'Valle del Cauca',
    '81': 'Arauca',
    '85': 'Casanare',
    '86': 'Putumayo',
    '88': 'San Andrés y Providencia',
    '91': 'Amazonas',
    '94': 'Guainía',
    '95': 'Guaviare',
    '97': 'Vaupés',
    '99': 'Vichada'
}

municipio_mapping = {
    '5': {
'001':'MEDELLIN',
'002':'ABEJORRAL',
'004':'ABRIAQUI',
'021':'ALEJANDRIA',
'030':'AMAGA',
'031':'AMALFI',
'034':'ANDES',
'036':'ANGELOPOLIS',
'038':'ANGOSTURA',
'040':'ANORI',
'042':'SANTAFE DE ANTIOQUIA',
'044':'ANZA',
'045':'APARTADO',
'051':'ARBOLETES',
'055':'ARGELIA',
'059':'ARMENIA',
'079':'BARBOSA',
'086':'BELMIRA',
'088':'BELLO',
'091':'BETANIA',
'093':'BETULIA',
'101':'CIUDAD BOLIVAR',
'107':'BRICEÑO',
'113':'BURITICA',
'120':'CACERES',
'125':'CAICEDO',
'129':'CALDAS',
'134':'CAMPAMENTO',
'138':'CAÑASGORDAS',
'142':'CARACOLI',
'145':'CARAMANTA',
'147':'CAREPA',
'148':'EL CARMEN DE VIBORAL',
'150':'CAROLINA',
'154':'CAUCASIA',
'172':'CHIGORODO',
'190':'CISNEROS',
'197':'COCORNA',
'206':'CONCEPCION',
'209':'CONCORDIA',
'212':'COPACABANA',
'234':'DABEIBA',
'237':'DON MATIAS',
'240':'EBEJICO',
'250':'EL BAGRE',
'264':'ENTRERRIOS',
'266':'ENVIGADO',
'282':'FREDONIA',
'284':'FRONTINO',
'306':'GIRALDO',
'308':'GIRARDOTA',
'310':'GOMEZ PLATA',
'313':'GRANADA',
'315':'GUADALUPE',
'318':'GUARNE',
'321':'GUATAPE',
'347':'HELICONIA',
'353':'HISPANIA',
'360':'ITAGUI',
'361':'ITUANGO',
'364':'JARDIN',
'368':'JERICO',
'376':'LA CEJA',
'380':'LA ESTRELLA',
'390':'LA PINTADA',
'400':'LA UNION',
'411':'LIBORINA',
'425':'MACEO',
'440':'MARINILLA',
'467':'MONTEBELLO',
'475':'MURINDO',
'480':'MUTATA',
'483':'NARIÑO',
'490':'NECOCLI',
'495':'NECHI',
'501':'OLAYA',
'541':'PEÐOL',
'543':'PEQUE',
'576':'PUEBLORRICO',
'579':'PUERTO BERRIO',
'585':'PUERTO NARE',
'591':'PUERTO TRIUNFO',
'604':'REMEDIOS',
'607':'RETIRO',
'615':'RIONEGRO',
'628':'SABANALARGA',
'631':'SABANETA',
'642':'SALGAR',
'647':'SAN ANDRES DE CUERQUIA',
'649':'SAN CARLOS',
'652':'SAN FRANCISCO',
'656':'SAN JERONIMO',
'658':'SAN JOSE DE LA MONTAÑA',
'659':'SAN JUAN DE URABA',
'660':'SAN LUIS',
'664':'SAN PEDRO',
'665':'SAN PEDRO DE URABA',
'667':'SAN RAFAEL',
'670':'SAN ROQUE',
'674':'SAN VICENTE',
'679':'SANTA BARBARA',
'686':'SANTA ROSA DE OSOS',
'690':'SANTO DOMINGO',
'697':'EL SANTUARIO',
'736':'SEGOVIA',
'756':'SONSON',
'761':'SOPETRAN',
'789':'TAMESIS',
'790':'TARAZA',
'792':'TARSO',
'809':'TITIRIBI',
'819':'TOLEDO',
'837':'TURBO',
'842':'URAMITA',
'847':'URRAO',
'854':'VALDIVIA',
'856':'VALPARAISO',
'858':'VEGACHI',
'861':'VENECIA',
'873':'VIGIA DEL FUERTE',
'885':'YALI',
'887':'YARUMAL',
'890':'YOLOMBO',
'893':'YONDO',
'895':'ZARAGOZA',

    },
    '8': {
'001':'BARRANQUILLA',
'078':'BARANOA',
'137':'CAMPO DE LA CRUZ',
'141':'CANDELARIA',
'296':'GALAPA',
'372':'JUAN DE ACOSTA',
'421':'LURUACO',
'433':'MALAMBO',
'436':'MANATI',
'520':'PALMAR DE VARELA',
'549':'PIOJO',
'558':'POLONUEVO',
'560':'PONEDERA',
'573':'PUERTO COLOMBIA',
'606':'REPELON',
'634':'SABANAGRANDE',
'638':'SABANALARGA',
'675':'SANTA LUCIA',
'685':'SANTO TOMAS',
'758':'SOLEDAD',
'770':'SUAN',
'832':'TUBARA',
'849':'USIACURI',
    },
    '11': {
        '001': 'Bogotá D.C.'
    },
    '13': {
       '001':'CARTAGENA',
'006':'ACHI',
'030':'ALTOS DEL ROSARIO',
'042':'ARENAL',
'052':'ARJONA',
'062':'ARROYOHONDO',
'074':'BARRANCO DE LOBA',
'140':'CALAMAR',
'160':'CANTAGALLO',
'188':'CICUCO',
'212':'CORDOBA',
'222':'CLEMENCIA',
'244':'EL CARMEN DE BOLIVAR',
'248':'EL GUAMO',
'268':'EL PEÑON',
'300':'HATILLO DE LOBA',
'430':'MAGANGUE',
'433':'MAHATES',
'440':'MARGARITA',
'442':'MARIA LA BAJA',
'458':'MONTECRISTO',
'468':'MOMPOS',
'490':'NOROSI',
'473':'MORALES',
'549':'PINILLOS',
'580':'REGIDOR',
'600':'RIO VIEJO',
'620':'SAN CRISTOBAL',
'647':'SAN ESTANISLAO',
'650':'SAN FERNANDO',
'654':'SAN JACINTO',
'655':'SAN JACINTO DEL CAUCA',
'657':'SAN JUAN NEPOMUCENO',
'667':'SAN MARTIN DE LOBA',
'670':'SAN PABLO',
'673':'SANTA CATALINA',
'683':'SANTA ROSA',
'688':'SANTA ROSA DEL SUR',
'744':'SIMITI',
'760':'SOPLAVIENTO',
'780':'TALAIGUA NUEVO',
'810':'TIQUISIO',
'836':'TURBACO',
'838':'TURBANA',
'873':'VILLANUEVA',
'894':'ZAMBRANO',
    },
    '15': {
        '001':'TUNJA',
'022':'ALMEIDA',
'047':'AQUITANIA',
'051':'ARCABUCO',
'087':'BELEN',
'090':'BERBEO',
'092':'BETEITIVA',
'097':'BOAVITA',
'104':'BOYACA',
'106':'BRICEÑO',
'109':'BUENAVISTA',
'114':'BUSBANZA',
'131':'CALDAS',
'135':'CAMPOHERMOSO',
'162':'CERINZA',
'172':'CHINAVITA',
'176':'CHIQUINQUIRA',
'180':'CHISCAS',
'183':'CHITA',
'185':'CHITARAQUE',
'187':'CHIVATA',
'189':'CIENEGA',
'204':'COMBITA',
'212':'COPER',
'215':'CORRALES',
'218':'COVARACHIA',
'223':'CUBARA',
'224':'CUCAITA',
'226':'CUITIVA',
'232':'CHIQUIZA',
'236':'CHIVOR',
'238':'DUITAMA',
'244':'EL COCUY',
'248':'EL ESPINO',
'272':'FIRAVITOBA',
'276':'FLORESTA',
'293':'GACHANTIVA',
'296':'GAMEZA',
'299':'GARAGOA',
'317':'GUACAMAYAS',
'322':'GUATEQUE',
'325':'GUAYATA',
'332':'GsICAN',
'362':'IZA',
'367':'JENESANO',
'368':'JERICO',
'377':'LABRANZAGRANDE',
'380':'LA CAPILLA',
'401':'LA VICTORIA',
'403':'LA UVITA',
'407':'VILLA DE LEYVA',
'425':'MACANAL',
'442':'MARIPI',
'455':'MIRAFLORES',
'464':'MONGUA',
'466':'MONGUI',
'469':'MONIQUIRA',
'476':'MOTAVITA',
'480':'MUZO',
'491':'NOBSA',
'494':'NUEVO COLON',
'500':'OICATA',
'507':'OTANCHE',
'511':'PACHAVITA',
'514':'PAEZ',
'516':'PAIPA',
'518':'PAJARITO',
'522':'PANQUEBA',
'531':'PAUNA',
'533':'PAYA',
'537':'PAZ DE RIO',
'542':'PESCA',
'550':'PISBA',
'572':'PUERTO BOYACA',
'580':'QUIPAMA',
'599':'RAMIRIQUI',
'600':'RAQUIRA',
'621':'RONDON',
'632':'SABOYA',
'638':'SACHICA',
'646':'SAMACA',
'660':'SAN EDUARDO',
'664':'SAN JOSE DE PARE',
'667':'SAN LUIS DE GACENO',
'673':'SAN MATEO',
'676':'SAN MIGUEL DE SEMA',
'681':'SAN PABLO DE BORBUR',
'686':'SANTANA',
'690':'SANTA MARIA',
'693':'SANTA ROSA DE VITERBO',
'696':'SANTA SOFIA',
'720':'SATIVANORTE',
'723':'SATIVASUR',
'740':'SIACHOQUE',
'753':'SOATA',
'755':'SOCOTA',
'757':'SOCHA',
'759':'SOGAMOSO',
'761':'SOMONDOCO',
'762':'SORA',
'763':'SOTAQUIRA',
'764':'SORACA',
'774':'SUSACON',
'776':'SUTAMARCHAN',
'778':'SUTATENZA',
'790':'TASCO',
'798':'TENZA',
'804':'TIBANA',
'806':'TIBASOSA',
'808':'TINJACA',
'810':'TIPACOQUE',
'814':'TOCA',
'816':'TOGsI',
'820':'TOPAGA',
'822':'TOTA',
'832':'TUNUNGUA',
'835':'TURMEQUE',
'837':'TUTA',
'839':'TUTAZA',
'842':'UMBITA',
'861':'VENTAQUEMADA',
'879':'VIRACACHA',
'897':'ZETAQUIRA',
    },
    '17': {
      '001':'MANIZALES',
'013':'AGUADAS',
'042':'ANSERMA',
'050':'ARANZAZU',
'088':'BELALCAZAR',
'174':'CHINCHINA',
'272':'FILADELFIA',
'380':'LA DORADA',
'388':'LA MERCED',
'433':'MANZANARES',
'442':'MARMATO',
'444':'MARQUETALIA',
'446':'MARULANDA',
'486':'NEIRA',
'495':'NORCASIA',
'513':'PACORA',
'524':'PALESTINA',
'541':'PENSILVANIA',
'614':'RIOSUCIO',
'616':'RISARALDA',
'653':'SALAMINA',
'662':'SAMANA',
'665':'SAN JOSE',
'777':'SUPIA',
'867':'VICTORIA',
'873':'VILLAMARIA',
'877':'VITERBO',
    },
    '18':{
'001':'FLORENCIA',
'029':'ALBANIA',
'094':'BELEN DE LOS ANDAQUIES',
'150':'CARTAGENA DEL CHAIRA',
'205':'CURILLO',
'247':'EL DONCELLO',
'256':'EL PAUJIL',
'410':'LA MONTAÑITA',
'460':'MILAN',
'479':'MORELIA',
'592':'PUERTO RICO',
'610':'SAN JOSE DEL FRAGUA',
'753':'SAN VICENTE DEL CAGUAN',
'756':'SOLANO',
'785':'SOLITA',
'860':'VALPARAISO',

},
    '19': {
        '001':'POPAYAN',
'022':'ALMAGUER',
'050':'ARGELIA',
'075':'BALBOA',
'100':'BOLIVAR',
'110':'BUENOS AIRES',
'130':'CAJIBIO',
'137':'CALDONO',
'142':'CALOTO',
'212':'CORINTO',
'256':'EL TAMBO',
'290':'FLORENCIA',
'300':'GUACHENE',
'318':'GUAPI',
'355':'INZA',
'364':'JAMBALO',
'392':'LA SIERRA',
'397':'LA VEGA',
'418':'LOPEZ',
'450':'MERCADERES',
'455':'MIRANDA',
'473':'MORALES',
'513':'PADILLA',
'517':'PAEZ',
'532':'PATIA',
'533':'PIAMONTE',
'548':'PIENDAMO',
'573':'PUERTO TEJADA',
'585':'PURACE',
'622':'ROSAS',
'693':'SAN SEBASTIAN',
'698':'SANTANDER DE QUILICHAO',
'701':'SANTA ROSA',
'743':'SILVIA',
'760':'SOTARA',
'780':'SUAREZ',
'785':'SUCRE',
'807':'TIMBIO',
'809':'TIMBIQUI',
'821':'TORIBIO',
'824':'TOTORO',
'845':'VILLA RICA',
    },
    '20': {
    '001':'VALLEDUPAR',
'011':'AGUACHICA',
'013':'AGUSTIN CODAZZI',
'032':'ASTREA',
'045':'BECERRIL',
'060':'BOSCONIA',
'175':'CHIMICHAGUA',
'178':'CHIRIGUANA',
'228':'CURUMANI',
'238':'EL COPEY',
'250':'EL PASO',
'295':'GAMARRA',
'310':'GONZALEZ',
'383':'LA GLORIA',
'400':'LA JAGUA DE IBIRICO',
'443':'MANAURE',
'517':'PAILITAS',
'550':'PELAYA',
'570':'PUEBLO BELLO',
'614':'RIO DE ORO',
'621':'LA PAZ',
'710':'SAN ALBERTO',
'750':'SAN DIEGO',
'770':'SAN MARTIN',
'787':'TAMALAMEQUE',
},
    '23': {
        '001':'MONTERIA',
'068':'AYAPEL',
'079':'BUENAVISTA',
'090':'CANALETE',
'162':'CERETE',
'168':'CHIMA',
'182':'CHINU',
'189':'CIENAGA DE ORO',
'300':'COTORRA',
'350':'LA APARTADA',
'417':'LORICA',
'419':'LOS CORDOBAS',
'464':'MOMIL',
'466':'MONTELIBANO',
'500':'MOÑITOS',
'555':'PLANETA RICA',
'570':'PUEBLO NUEVO',
'574':'PUERTO ESCONDIDO',
'580':'PUERTO LIBERTADOR',
'586':'PURISIMA',
'660':'SAHAGUN',
'670':'SAN ANDRES SOTAVENTO',
'672':'SAN ANTERO',
'675':'SAN BERNARDO DEL VIENTO',
'678':'SAN CARLOS',
'686':'SAN PELAYO',
'807':'TIERRALTA',
'855':'VALENCIA',
},
    '25': {
        '001':'AGUA DE DIOS',
'019':'ALBAN',
'035':'ANAPOIMA',
'040':'ANOLAIMA',
'053':'ARBELAEZ',
'086':'BELTRAN',
'095':'BITUIMA',
'099':'BOJACA',
'120':'CABRERA',
'123':'CACHIPAY',
'126':'CAJICA',
'148':'CAPARRAPI',
'151':'CAQUEZA',
'154':'CARMEN DE CARUPA',
'168':'CHAGUANI',
'175':'CHIA',
'178':'CHIPAQUE',
'181':'CHOACHI',
'183':'CHOCONTA',
'200':'COGUA',
'214':'COTA',
'224':'CUCUNUBA',
'245':'EL COLEGIO',
'258':'EL PEÑON',
'260':'EL ROSAL',
'269':'FACATATIVA',
'279':'FOMEQUE',
'281':'FOSCA',
'286':'FUNZA',
'288':'FUQUENE',
'290':'FUSAGASUGA',
'293':'GACHALA',
'295':'GACHANCIPA',
'297':'GACHETA',
'299':'GAMA',
'307':'GIRARDOT',
'312':'GRANADA',
'317':'GUACHETA',
'320':'GUADUAS',
'322':'GUASCA',
'324':'GUATAQUI',
'326':'GUATAVITA',
'328':'GUAYABAL DE SIQUIMA',
'335':'GUAYABETAL',
'339':'GUTIERREZ',
'368':'JERUSALEN',
'372':'JUNIN',
'377':'LA CALERA',
'386':'LA MESA',
'394':'LA PALMA',
'398':'LA PEÑA',
'402':'LA VEGA',
'407':'LENGUAZAQUE',
'426':'MACHETA',
'430':'MADRID',
'436':'MANTA',
'438':'MEDINA',
'473':'MOSQUERA',
'483':'NARIÑO',
'486':'NEMOCON',
'488':'NILO',
'489':'NIMAIMA',
'491':'NOCAIMA',
'506':'VENECIA',
'513':'PACHO',
'518':'PAIME',
'524':'PANDI',
'530':'PARATEBUENO',
'535':'PASCA',
'572':'PUERTO SALGAR',
'580':'PULI',
'592':'QUEBRADANEGRA',
'594':'QUETAME',
'596':'QUIPILE',
'599':'APULO',
'612':'RICAURTE',
'645':'SAN ANTONIO DEL TEQUENDA',
'649':'SAN BERNARDO',
'653':'SAN CAYETANO',
'658':'SAN FRANCISCO',
'662':'SAN JUAN DE RIO SECO',
'718':'SASAIMA',
'736':'SESQUILE',
'740':'SIBATE',
'743':'SILVANIA',
'745':'SIMIJACA',
'754':'SOACHA',
'758':'SOPO',
'769':'SUBACHOQUE',
'772':'SUESCA',
'777':'SUPATA',
'779':'SUSA',
'781':'SUTATAUSA',
'785':'TABIO',
'793':'TAUSA',
'797':'TENA',
'799':'TENJO',
'805':'TIBACUY',
'807':'TIBIRITA',
'815':'TOCAIMA',
'817':'TOCANCIPA',
'823':'TOPAIPI',
'839':'UBALA',
'841':'UBAQUE',
'843':'VILLA DE SAN DIEGO DE UBAT',
'845':'UNE',
'851':'UTICA',
'862':'VERGARA',
'867':'VIANI',
'871':'VILLAGOMEZ',
'873':'VILLAPINZON',
'875':'VILLETA',
'878':'VIOTA',
'885':'YACOPI',
'898':'ZIPACON',
'899':'ZIPAQUIRA',
    },
    '27': {
  '001':'QUIBDO',
'006':'ACANDI',
'025':'ALTO BAUDO',
'050':'ATRATO',
'073':'BAGADO',
'075':'BAHIA SOLANO',
'077':'BAJO BAUDO',
'099':'BOJAYA',
'135':'EL CANTON DEL SAN PABLO',
'150':'CARMEN DEL DARIEN',
'160':'CERTEGUI',
'205':'CONDOTO',
'245':'EL CARMEN DE ATRATO',
'250':'EL LITORAL DEL SAN JUAN',
'361':'ISTMINA',
'372':'JURADO',
'413':'LLORO',
'425':'MEDIO ATRATO',
'430':'MEDIO BAUDO',
'450':'MEDIO SAN JUAN',
'491':'NOVITA',
'495':'NUQUI',
'580':'RIO IRO',
'600':'RIO QUITO',
'615':'RIOSUCIO',
'660':'SAN JOSE DEL PALMAR',
'745':'SIPI',
'787':'TADO',
'800':'UNGUIA',
'810':'UNION PANAMERICANA',
    },
    '41': {
        '001':'NEIVA',
'006':'ACEVEDO',
'013':'AGRADO',
'016':'AIPE',
'020':'ALGECIRAS',
'26':'ALTAMIRA',
'078':'BARAYA',
'132':'CAMPOALEGRE',
'206':'COLOMBIA',
'244':'ELIAS',
'298':'GARZON',
'306':'GIGANTE',
'319':'GUADALUPE',
'349':'HOBO',
'357':'IQUIRA',
'359':'ISNOS',
'378':'LA ARGENTINA',
'396':'LA PLATA',
'483':'NATAGA',
'503':'OPORAPA',
'518':'PAICOL',
'524':'PALERMO',
'530':'PALESTINA',
'548':'PITAL',
'551':'PITALITO',
'615':'RIVERA',
'660':'SALADOBLANCO',
'668':'SAN AGUSTIN',
'676':'SANTA MARIA',
'770':'SUAZA',
'791':'TARQUI',
'797':'TESALIA',
'799':'TELLO',
'801':'TERUEL',
'807':'TIMANA',
'872':'VILLAVIEJA',
'885':'YAGUARA',
    },
    '45':{
 '001':'RIOHACHA',
'035':'ALBANIA',
'078':'BARRANCAS',
'090':'DIBULLA',
'098':'DISTRACCION',
'110':'EL MOLINO',
'279':'FONSECA',
'378':'HATONUEVO',
'420':'LA JAGUA DEL PILAR',
'430':'MAICAO',
'560':'MANAURE',
'650':'SAN JUAN DEL CESAR',
'847':'URIBIA',
'855':'URUMITA',
'874':'VILLANUEVA',
    },
    '47': {
        '001':'SANTA MARTA',
'030':'ALGARROBO',
'053':'ARACATACA',
'058':'ARIGUANI',
'161':'CERRO SAN ANTONIO',
'170':'CHIBOLO',
'189':'CIENAGA',
'205':'CONCORDIA',
'245':'EL BANCO',
'258':'EL PIÑON',
'268':'EL RETEN',
'288':'FUNDACION',
'318':'GUAMAL',
'460':'NUEVA GRANADA',
'541':'PEDRAZA',
'545':'PIJIÑO DEL CARMEN',
'551':'PIVIJAY',
'555':'PLATO',
'570':'PUEBLOVIEJO',
'605':'REMOLINO',
'660':'SABANAS DE SAN ANGEL',
'675':'SALAMINA',
'692':'SAN SEBASTIAN DE BUENAVIS',
'703':'SAN ZENON',
'707':'SANTA ANA',
'720':'SANTA BARBARA DE PINTO',
'745':'SITIONUEVO',
'798':'TENERIFE',
'960':'ZAPAYAN',
'980':'ZONA BANANERA',
    },
    '50': {
'001':'VILLAVICENCIO',
'006':'ACACIAS',
'110':'BARRANCA DE UPIA',
'124':'CABUYARO',
'150':'CASTILLA LA NUEVA',
'223':'CUBARRAL',
'226':'CUMARAL',
'245':'EL CALVARIO',
'251':'EL CASTILLO',
'270':'EL DORADO',
'287':'FUENTE DE ORO',
'313':'GRANADA',
'318':'GUAMAL',
'325':'MAPIRIPAN',
'330':'MESETAS',
'350':'LA MACARENA',
'370':'URIBE',
'400':'LEJANIAS',
'450':'PUERTO CONCORDIA',
'568':'PUERTO GAITAN',
'573':'PUERTO LOPEZ',
'577':'PUERTO LLERAS',
'590':'PUERTO RICO',
'606':'RESTREPO',
'680':'SAN CARLOS DE GUAROA',
'683':'SAN JUAN DE ARAMA',
'686':'SAN JUANITO',
'689':'SAN MARTIN',
'711':'VISTAHERMOSA',
    },
'52': {
'001':'PASTO',
'019':'ALBAN',
'022':'ALDANA',
'036':'ANCUYA',
'051':'ARBOLEDA',
'079':'BARBACOAS',
'083':'BELEN',
'110':'BUESACO',
'203':'COLON',
'207':'CONSACA',
'210':'CONTADERO',
'215':'CORDOBA',
'224':'CUASPUD',
'227':'CUMBAL',
'233':'CUMBITARA',
'240':'CHACHAGsI',
'250':'EL CHARCO',
'254':'EL PEÑOL',
'256':'EL ROSARIO',
'258':'EL TABLON DE GOMEZ',
'260':'EL TAMBO',
'287':'FUNES',
'317':'GUACHUCAL',
'320':'GUAITARILLA',
'323':'GUALMATAN',
'352':'ILES',
'354':'IMUES',
'356':'IPIALES',
'378':'LA CRUZ',
'381':'LA FLORIDA',
'385':'LA LLANADA',
'390':'LA TOLA',
'399':'LA UNION',
'405':'LEIVA',
'411':'LINARES',
'418':'LOS ANDES',
'427':'MAGsI',
'435':'MALLAMA',
'473':'MOSQUERA',
'480':'NARIÑO',
'490':'OLAYA HERRERA',
'506':'OSPINA',
'520':'FRANCISCO PIZARRO',
'540':'POLICARPA',
'560':'POTOSI',
'565':'PROVIDENCIA',
'573':'PUERRES',
'585':'PUPIALES',
'612':'RICAURTE',
'621':'ROBERTO PAYAN',
'678':'SAMANIEGO',
'683':'SANDONA',
'685':'SAN BERNARDO',
'687':'SAN LORENZO',
'693':'SAN PABLO',
'694':'SAN PEDRO DE CARTAGO',
'696':'SANTA BARBARA',
'699':'SANTACRUZ',
'720':'SAPUYES',
'786':'TAMINANGO',
'788':'TANGUA',
'835':'SAN ANDRES DE TUMACO',
'838':'TUQUERRES',
'885':'YACUANQUER',
    },
    '54': {
        '001':'CUCUTA',
'003':'ABREGO',
'051':'ARBOLEDAS',
'099':'BOCHALEMA',
'109':'BUCARASICA',
'125':'CACOTA',
'128':'CACHIRA',
'172':'CHINACOTA',
'174':'CHITAGA',
'206':'CONVENCION',
'223':'CUCUTILLA',
'239':'DURANIA',
'245':'EL CARMEN',
'250':'EL TARRA',
'261':'EL ZULIA',
'313':'GRAMALOTE',
'344':'HACARI',
'347':'HERRAN',
'377':'LABATECA',
'385':'LA ESPERANZA',
'398':'LA PLAYA',
'405':'LOS PATIOS',
'418':'LOURDES',
'480':'MUTISCUA',
'498':'OCAÑA',
'518':'PAMPLONA',
'520':'PAMPLONITA',
'553':'PUERTO SANTANDER',
'599':'RAGONVALIA',
'660':'SALAZAR',
'670':'SAN CALIXTO',
'673':'SAN CAYETANO',
'680':'SANTIAGO',
'720':'SARDINATA',
'743':'SILOS',
'800':'TEORAMA',
'810':'TIBU',
'820':'TOLEDO',
'871':'VILLA CARO',
'874':'VILLA DEL ROSARIO',
    },
    '63': {
'001':'ARMENIA',
'111':'BUENAVISTA',
'130':'CALARCA',
'190':'CIRCASIA',
'212':'CORDOBA',
'272':'FILANDIA',
'302':'GENOVA',
'401':'LA TEBAIDA',
'470':'MONTENEGRO',
'548':'PIJAO',
'594':'QUIMBAYA',
'690':'SALENTO',
    },
    '66': {
'001':'PEREIRA',
'045':'APIA',
'075':'BALBOA',
'088':'BELEN DE UMBRIA',
'170':'DOSQUEBRADAS',
'318':'GUATICA',
'383':'LA CELIA',
'400':'LA VIRGINIA',
'440':'MARSELLA',
'456':'MISTRATO',
'572':'PUEBLO RICO',
'594':'QUINCHIA',
'682':'SANTA ROSA DE CABAL',
'687':'SANTUARIO',
    },
    '68': {
'001':'BUCARAMANGA',
'013':'AGUADA',
'020':'ALBANIA',
'051':'ARATOCA',
'077':'BARBOSA',
'079':'BARICHARA',
'081':'BARRANCABERMEJA',
'092':'BETULIA',
'101':'BOLIVAR',
'121':'CABRERA',
'132':'CALIFORNIA',
'147':'CAPITANEJO',
'152':'CARCASI',
'160':'CEPITA',
'162':'CERRITO',
'167':'CHARALA',
'169':'CHARTA',
'176':'CHIMA',
'179':'CHIPATA',
'190':'CIMITARRA',
'207':'CONCEPCION',
'209':'CONFINES',
'211':'CONTRATACION',
'217':'COROMORO',
'229':'CURITI',
'235':'EL CARMEN DE CHUCURI',
'245':'EL GUACAMAYO',
'250':'EL PEÑON',
'255':'EL PLAYON',
'264':'ENCINO',
'266':'ENCISO',
'271':'FLORIAN',
'276':'FLORIDABLANCA',
'296':'GALAN',
'298':'GAMBITA',
'307':'GIRON',
'318':'GUACA',
'320':'GUADALUPE',
'322':'GUAPOTA',
'324':'GUAVATA',
'327':'GsEPSA',
'344':'HATO',
'368':'JESUS MARIA',
'370':'JORDAN',
'377':'LA BELLEZA',
'385':'LANDAZURI',
'397':'LA PAZ',
'406':'LEBRIJA',
'418':'LOS SANTOS',
'425':'MACARAVITA',
'432':'MALAGA',
'444':'MATANZA',
'464':'MOGOTES',
'468':'MOLAGAVITA',
'498':'OCAMONTE',
'500':'OIBA',
'502':'ONZAGA',
'522':'PALMAR',
'524':'PALMAS DEL SOCORRO',
'533':'PARAMO',
'547':'PIEDECUESTA',
'549':'PINCHOTE',
'572':'PUENTE NACIONAL',
'573':'PUERTO PARRA',
'575':'PUERTO WILCHES',
'615':'RIONEGRO',
'655':'SABANA DE TORRES',
'669':'SAN ANDRES',
'673':'SAN BENITO',
'679':'SAN GIL',
'682':'SAN JOAQUIN',
'684':'SAN JOSE DE MIRANDA',
'686':'SAN MIGUEL',
'689':'SAN VICENTE DE CHUCURI',
'705':'SANTA BARBARA',
'720':'SANTA HELENA DEL OPON',
'745':'SIMACOTA',
'755':'SOCORRO',
'770':'SUAITA',
'773':'SUCRE',
'780':'SURATA',
'820':'TONA',
'855':'VALLE DE SAN JOSE',
'861':'VELEZ',
'867':'VETAS',
'872':'VILLANUEVA',
'895':'ZAPATOCA',
        },

'70': {
    '001':'SINCELEJO',
'110':'BUENAVISTA',
'124':'CAIMITO',
'204':'COLOSO',
'215':'COROZAL',
'221':'COVEÑAS',
'230':'CHALAN',
'233':'EL ROBLE',
'235':'GALERAS',
'265':'GUARANDA',
'400':'LA UNION',
'418':'LOS PALMITOS',
'429':'MAJAGUAL',
'473':'MORROA',
'508':'OVEJAS',
'523':'PALMITO',
'670':'SAMPUES',
'678':'SAN BENITO ABAD',
'702':'SAN JUAN DE BETULIA',
'708':'SAN MARCOS',
'713':'SAN ONOFRE',
'717':'SAN PEDRO',
'742':'SAN LUIS DE SINCE',
'771':'SUCRE',
'820':'SANTIAGO DE TOLU',
'823':'TOLU VIEJO',
},
'73': {
'001':'IBAGUE',
'024':'ALPUJARRA',
'026':'ALVARADO',
'030':'AMBALEMA',
'043':'ANZOATEGUI',
'055':'ARMERO',
'067':'ATACO',
'124':'CAJAMARCA',
'148':'CARMEN DE APICALA',
'152':'CASABIANCA',
'168':'CHAPARRAL',
'200':'COELLO',
'217':'COYAIMA',
'226':'CUNDAY',
'236':'DOLORES',
'268':'ESPINAL',
'270':'FALAN',
'275':'FLANDES',
'283':'FRESNO',
'319':'GUAMO',
'347':'HERVEO',
'349':'HONDA',
'352':'ICONONZO',
'408':'LERIDA',
'411':'LIBANO',
'443':'MARIQUITA',
'449':'MELGAR',
'461':'MURILLO',
'483':'NATAGAIMA',
'504':'ORTEGA',
'520':'PALOCABILDO',
'547':'PIEDRAS',
'555':'PLANADAS',
'563':'PRADO',
'585':'PURIFICACION',
'616':'RIOBLANCO',
'622':'RONCESVALLES',
'624':'ROVIRA',
'671':'SALDAÑA',
'675':'SAN ANTONIO',
'678':'SAN LUIS',
'686':'SANTA ISABEL',
'770':'SUAREZ',
'854':'VALLE DE SAN JUAN',
'861':'VENADILLO',
'870':'VILLAHERMOSA',
'873':'VILLARRICA',
},
'76': {
    '001':'CALI',
'020':'ALCALA',
'036':'ANDALUCIA',
'041':'ANSERMANUEVO',
'054':'ARGELIA',
'100':'BOLIVAR',
'109':'BUENAVENTURA',
'111':'GUADALAJARA DE BUGA',
'113':'BUGALAGRANDE',
'122':'CAICEDONIA',
'126':'CALIMA',
'130':'CANDELARIA',
'147':'CARTAGO',
'233':'DAGUA',
'243':'EL AGUILA',
'246':'EL CAIRO',
'248':'EL CERRITO',
'250':'EL DOVIO',
'275':'FLORIDA',
'306':'GINEBRA',
'318':'GUACARI',
'364':'JAMUNDI',
'377':'LA CUMBRE',
'400':'LA UNION',
'403':'LA VICTORIA',
'497':'OBANDO',
'520':'PALMIRA',
'563':'PRADERA',
'606':'RESTREPO',
'616':'RIOFRIO',
'622':'ROLDANILLO',
'670':'SAN PEDRO',
'736':'SEVILLA',
'823':'TORO',
'828':'TRUJILLO',
'834':'TULUA',
'845':'ULLOA',
'863':'VERSALLES',
'869':'VIJES',
'890':'YOTOCO',
'892':'YUMBO',
'895':'ZARZAL',
},
'81': {
'001':'ARAUCA',
'065':'ARAUQUITA',
'220':'CRAVO NORTE',
'300':'FORTUL',
'591':'PUERTO RONDON',
'736':'SARAVENA',
'794':'TAME',
},
'85': {
'001':'YOPAL',
'010':'AGUAZUL',
'015':'CHAMEZA',
'125':'HATO COROZAL',
'136':'LA SALINA',
'139':'MANI',
'162':'MONTERREY',
'225':'NUNCHIA',
'230':'OROCUE',
'250':'PAZ DE ARIPORO',
'263':'PORE',
'279':'RECETOR',
'300':'SABANALARGA',
'315':'SACAMA',
'325':'SAN LUIS DE PALENQUE',
'400':'TAMARA',
'410':'TAURAMENA',
'430':'TRINIDAD',
'440':'VILLANUEVA',
},
'86': {
'001':'MOCOA',
'219':'COLON',
'320':'ORITO',
'568':'PUERTO ASIS',
'569':'PUERTO CAICEDO',
'571':'PUERTO GUZMAN',
'573':'LEGUIZAMO',
'749':'SIBUNDOY',
'755':'SAN FRANCISCO',
'757':'SAN MIGUEL',
'760':'SANTIAGO',
'865':'VALLE DEL GUAMUEZ',
'885':'VILLAGARZON',
},
'88': {
    '001':'SAN ANDRES',
'564':'PROVIDENCIA',

},
'91': {
    
'001':'LETICIA',
'263':'EL ENCANTO',
'405':'LA CHORRERA',
'407':'LA PEDRERA',
'430':'LA VICTORIA',
'460':'MIRITI - PARANA',
'530':'PUERTO ALEGRIA',
'536':'PUERTO ARICA',
'540':'PUERTO NARIÑO',
'669':'PUERTO SANTANDER',
'798':'TARAPACA',
},
'94': {
    '001':'INIRIDA',
'343':'BARRANCO MINAS',
'663':'MAPIRIPANA',
'883':'SAN FELIPE',
'884':'PUERTO COLOMBIA',
'885':'LA GUADALUPE',
'886':'CACAHUAL',
'887':'PANA PANA',
'888':'MORICHAL',

},
'95': {
    '001':'SAN JOSE DEL GUAVIARE',
'015':'CALAMAR',
'025':'EL RETORNO',
'200':'MIRAFLORES',
},
'97': {
'001':'MITU',
'161':'CARURU',
'511':'PACOA',
'666':'TARAIRA',
'777':'PAPUNAUA',
'889':'YAVARATE',
    
},
'99': {
'001':'PUERTO CARREÑO',
'524':'LA PRIMAVERA',
'624':'SANTA ROSALIA',
'773':'CUMARIBO',
}
}
def cargar_archivo():
    global datos
    global variables
    
    try:
        # Mostrar el cuadro de diálogo para seleccionar el archivo CSV
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivo CSV", "*.csv")])
        
        # Cargar el archivo CSV en un DataFrame
        datos = pd.read_csv(ruta_archivo)
        
        # Añadir información del DANE al DataFrame cargado
        datos = agregar_info_dane(datos)
        
        # Listar las variables cargadas del archivo
        variables = datos.columns.tolist()
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Archivo cargado exitosamente.")
        
        # Mostrar tabla con los datos y la información del DANE
        mostrar_tabla(datos)
        
    except FileNotFoundError:
        messagebox.showerror("Error", "No se seleccionó ningún archivo.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def agregar_info_dane(df):
    """
    Agrega información del DANE, incluyendo departamento, municipio y coordenadas de latitud y longitud al DataFrame.
    
    Args:
    - df: DataFrame de pandas que contiene los datos a los que se les agregará la información del DANE.
    
    Returns:
    - df: DataFrame con la información del DANE agregada.
    """
    global datos
    
    # Cargar los datos si no se han cargado previamente
    if datos is None:
        cargar_archivo()
        
    # Verificar si hay un DANE válido antes de asignar el nombre del departamento y municipio
    df['Departamento'] = ''
    df['Municipio'] = ''
    df['Latitud'] = None
    df['Longitud'] = None
    
    # Obtener las coordenadas de latitud y longitud para cada departamento
    dpto_lat_long = obtener_coordenadas(dpto_mapping)
    
    for index, row in df.iterrows():
        dane = str(row['DANE'])  # Convertir el DANE a string para garantizar la longitud
        if len(dane) == 5:
            # Verificar si el código DANE corresponde a un departamento válido
            departamento = dpto_mapping.get(dane[:2])
            if departamento:
                df.at[index, 'Departamento'] = departamento
                # Verificar si el código DANE del municipio es válido para el departamento
                municipio = municipio_mapping.get(dane[:2], {}).get(dane[2:])
                if municipio:
                    df.at[index, 'Municipio'] = municipio
        elif len(dane) == 4:
            # Validar que los códigos DANE de 4 dígitos correspondan a Antioquia o Atlántico
            departamento = dpto_mapping.get(dane[:1])
            if departamento in ['Antioquia', 'Atlántico']:
                df.at[index, 'Departamento'] = departamento
                municipio = municipio_mapping.get(dane[:1], {}).get(dane[1:])
                if municipio:
                    df.at[index, 'Municipio'] = municipio
        else:
            # Cualquier otro caso de longitud del DANE se considera inválido
            df.at[index, 'Departamento'] = 'Inválido'
        
        # Agregar las coordenadas de latitud y longitud si están disponibles
        codigo_departamento = dane[:2]
        if codigo_departamento in dpto_lat_long:
            latitud, longitud = dpto_lat_long[codigo_departamento]
            df.at[index, 'Latitud'] = latitud
            df.at[index, 'Longitud'] = longitud
    
    return df

def mostrar_tabla(df):
    global datos
    
    # Cargar los datos si no se han cargado previamente
    if datos is None:
        cargar_archivo()
    
    if 'pt' not in globals():
        frame = tk.Frame(ventana)  # Usamos 'ventana' en lugar de 'root'
        frame.pack(fill='both', expand=True)
        global pt
        pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()
    else:
        pt.updateModel(TableModel(df))

#***********************************************************************************************************************
def obtener_coordenadas(dpto_mapping):
    """
    Obtiene las coordenadas de latitud y longitud para cada departamento en el diccionario dpto_mapping.
    
    Args:
    - dpto_mapping: Diccionario que mapea los códigos DANE a los nombres de los departamentos.
    
    Returns:
    - dpto_lat_long: Diccionario que mapea los códigos DANE a las coordenadas de latitud y longitud.
    """
    geolocator = ArcGIS()
    dpto_lat_long = {}
    
    for codigo, departamento in dpto_mapping.items():
        location = geolocator.geocode(departamento + ", Colombia")
        if location:
            dpto_lat_long[codigo] = (location.latitude, location.longitude)
        else:
            print(f"No se encontraron coordenadas para {departamento}")
    
    return dpto_lat_long

# Ejemplo de uso
dpto_lat_long = obtener_coordenadas(dpto_mapping)
print(dpto_lat_long)



#***********************************************************************************************************************

def mostrar_estadisticas():
    global datos
    
    # Verificar si se han cargado datos previamente
    if datos is not None:
        # Crear diagrama de dispersión para visualizar la relación entre año y casos
        plt.figure(figsize=(10, 6))
        plt.scatter(datos['Ano'], datos['cases_all'], color='blue', alpha=0.5, label='Casos de Dengue (Todos)')
        plt.scatter(datos['Ano'], datos['cases_lab'], color='red', alpha=0.5, label='Casos de Dengue (Laboratorio)')
        plt.title('Diagrama de Dispersión: Año vs. Casos de Dengue')
        plt.xlabel('Año')
        plt.ylabel('Casos de Dengue')
        plt.legend()
        plt.grid(True)
        plt.show()
        
        # Gráfico de barras para los mínimos y máximos casos
        plt.figure(figsize=(10, 6))
        plt.bar(['Mínimo', 'Máximo'], [datos['cases_all'].min(), datos['cases_all'].max()], color=['green', 'red'])
        plt.title('Mínimos y Máximos Casos de Dengue')
        plt.xlabel('Caso')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        plt.show()
        
        # Gráfico de barras para los casos de laboratorio y todos los casos
        plt.figure(figsize=(10, 6))
        plt.bar(['Laboratorio', 'Todos'], [datos['cases_lab'].sum(), datos['cases_all'].sum()], color=['blue', 'orange'])
        plt.title('Casos de Dengue: Laboratorio vs. Todos')
        plt.xlabel('Tipo de Caso')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        plt.show()
        
        # Estadísticas adicionales por departamento y municipio
        plt.figure(figsize=(16, 10))
        
        # Departamentos con más casos de dengue
        top_departamentos = datos.groupby('Departamento')['cases_all'].sum().nlargest(5)
        plt.subplot(3, 2, 1)
        top_departamentos.plot(kind='bar', color='skyblue')
        plt.title('Top 5 Departamentos con Más Casos de Dengue')
        plt.xlabel('Departamento')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        
        # Municipios con más casos de dengue
        top_municipios = datos.groupby('Municipio')['cases_all'].sum().nlargest(5)
        plt.subplot(3, 2, 2)
        top_municipios.plot(kind='bar', color='salmon')
        plt.title('Top 5 Municipios con Más Casos de Dengue')
        plt.xlabel('Municipio')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        
        # Año con más casos de dengue
        plt.subplot(3, 2, 3)
        year_with_most_cases = datos.groupby('Ano')['cases_all'].sum().idxmax()
        year_cases = datos.groupby('Ano')['cases_all'].sum()
        year_cases.plot(kind='bar', color='purple')
        plt.title(f'Año con Más Casos de Dengue: {year_with_most_cases}')
        plt.xlabel('Año')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        
        # Mes con más casos de dengue
        plt.subplot(3, 2, 4)
        month_with_most_cases = datos.groupby('Mes')['cases_all'].sum().idxmax()
        month_cases = datos.groupby('Mes')['cases_all'].sum()
        month_cases.plot(kind='bar', color='orange')
        plt.title(f'Mes con Más Casos de Dengue: {month_with_most_cases}')
        plt.xlabel('Mes')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
        
    else:
        messagebox.showwarning("Advertencia", "No se han cargado datos aún.")

#******************************************************************************************************************************
def mostrar_mapa():
    global datos

    # Verificar si hay datos cargados
    if datos is None:
        print("No se han cargado datos.")
        return

    

    # Calcular el total de casos por departamento
    total_casos_por_departamento = datos.groupby('Departamento')['cases_all'].sum()

    # Obtener los 5 departamentos con más casos
    top_departamentos = total_casos_por_departamento.nlargest(5)

    # Restablecer el índice de datos
    datos_reset_index = datos.reset_index()

    # Crear el texto de información para cada departamento
    hover_text = []
    for departamento, total_casos in total_casos_por_departamento.items():
        hover_text.append(f"{departamento}<br>Total de casos: {total_casos}")

    # Crear el mapa de calor
    fig = go.Figure(go.Densitymapbox(
        lat=datos_reset_index['Latitud'],  # Latitud de los 5 departamentos
        lon=datos_reset_index['Longitud'],  # Longitud de los 5 departamentos
        z=datos_reset_index['cases_all'],  # Casos de dengue por cada punto
        radius=10,
        colorscale="YlOrRd",  # Escala de colores
        zmin=0,
        zmax=datos_reset_index['cases_all'].max(),
        hovertext=hover_text  # Agregar texto de información al pasar el ratón
    ))

    # Configurar el diseño del mapa
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=4,
        mapbox_center={"lat": 4.5709, "lon": -74.2973},
        margin={"r":0,"t":0,"l":0,"b":0}  # Reducir los márgenes para ocupar más espacio
    )

    # Guardar el mapa como un archivo HTML
    fig.write_html("mapa_interactivo.html")

#******************************************************************************************************************************


# Inicializar variables globales para almacenar los datos cargados
datos = None
variables = None

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Casos de Dengue")

# Botón para cargar el archivo
boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack(pady=10)

# Botón para mostrar estadísticas
boton_estadisticas = tk.Button(ventana, text="Mostrar Estadísticas", command=mostrar_estadisticas)
boton_estadisticas.pack(pady=10)

# Botón para mostrar la tabla
boton_mostrar_tabla = tk.Button(ventana, text="Mostrar Tabla", command=lambda: mostrar_tabla(datos))
boton_mostrar_tabla.pack(pady=10)

boton_mostrar_tabla = tk.Button(ventana, text="Mostrar Mapa", command=lambda: mostrar_mapa())
boton_mostrar_tabla.pack(pady=10)

# Mantener el programa en ejecución
ventana.mainloop()