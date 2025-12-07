#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ISIS-SAHANA LETHAL PATHOGEN ERADICATION DATABASE                          ║
║   D10Z-TTA Framework | Scale: GM·10⁻⁵¹                                       ║
║                                                                              ║
║   "Eliminar las cabezas, caen los cuerpos"                                  ║
║   Hackeo sistémico del registro patógeno omniversal                         ║
║                                                                              ║
║   Author: Jamil Al Thani | ORCID: 0009-0000-8858-4992                       ║
║                                                                              ║
║   This database contains representative protein sequences from key          ║
║   virulence factors of the most lethal pathogens known to humanity.         ║
║   Sequences are from public databases (UniProt, NCBI).                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum


class PathogenCategory(Enum):
    """Classification of pathogen types."""
    VIRUS = "VIRUS"
    BACTERIA = "BACTERIA"
    PARASITE = "PARASITE"
    FUNGUS = "FUNGUS"
    PRION = "PRION"


class ThreatLevel(Enum):
    """WHO/CDC threat classification."""
    TIER_1 = "TIER-1 (Máxima Amenaza)"      # Bioterrorism agents, pandemic potential
    TIER_2 = "TIER-2 (Alta Amenaza)"         # Major public health concern
    TIER_3 = "TIER-3 (Amenaza Significativa)" # Significant morbidity/mortality
    EMERGING = "EMERGENTE"                   # Newly emerging threats


@dataclass
class LethalPathogen:
    """Complete pathogen record for Isis-Sahana targeting."""
    
    name: str                    # Common name
    scientific_name: str         # Binomial/official name
    category: PathogenCategory   # Virus, bacteria, etc.
    threat_level: ThreatLevel    # CDC/WHO classification
    mortality_rate: str          # Estimated mortality
    annual_deaths: str           # Global annual deaths
    key_protein: str             # Target virulence factor
    protein_function: str        # What it does
    sequence: str                # Amino acid sequence (fragment)
    diseases: List[str]          # Associated diseases
    notes: str                   # Additional information


# =============================================================================
# TIER-1: MAXIMUM THREAT PATHOGENS (Bioterrorism / Pandemic)
# =============================================================================

TIER_1_PATHOGENS = [
    
    # --- VIRUSES ---
    
    LethalPathogen(
        name="Ébola (Zaire)",
        scientific_name="Zaire ebolavirus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="50-90%",
        annual_deaths="~11,000 (2014-2016 outbreak)",
        key_protein="Glicoproteína GP",
        protein_function="Fusión con membrana celular, entrada viral",
        sequence="MGVTGILQLPRDRFKRTSFFLWVIILFQRTFSIPLGVIHNSTLQVSDVDKLVCRDKLSSTNQLRSVGLNLEGNGVATDVPSATKRWGFRSGVPPKVVNYEAGEWAENCYNLEIKKPDGSECLPAAPDGIRGFPRCRYVHKVSGTGPCAGDFAFHKEGAFFLYDRLASTVIYRGTTFAEGVVAFLILPQAKKDFFSSHPLREPVNATEDPSSGYYSTTIRYQATGFGTNETEYLFEVDNLTYVQLESRFTPQFLLQLNETIYTSGKRSNTTGKLIWKVNPEIDTTIGEWAFWETKKNLTRKIRSEELSFTVVSNGAKNISGQSPARTSSDPGTNTTTEDHKIMASENSSAMVQVHSQGREAAVSHLTTLATISTSPQSLTTKPGPDNSTHNTPVYKLDISEATQVEQHHRRTDNDSTASDTPSATTAAGPPKAENTNTSKSTDFLDPATTTSPQNHSETAGNNNTHHQDTGEESASSGKLGLITNTIAGVAGLITGGRRTRREAIVNAQPKCNPNLHYWTTQDEGAAIGLAWIPYFGPAAEGIYIEGLMHNQDGLICGLRQLANETTQALQLFLRATTELRTFSILNRKAIDFLLQRWGGTCHILGPDCCIEPHDWTKNITDKIDQIIHDFVDKTLPDQGDNDNWWTGWRQWIPAGIGVTGVIIAVIALFCICKFVF",
        diseases=["Fiebre hemorrágica del Ébola"],
        notes="Tasa de letalidad más alta entre filovirus. Reservorio: murciélagos."
    ),
    
    LethalPathogen(
        name="Marburg",
        scientific_name="Marburg marburgvirus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="24-88%",
        annual_deaths="Variable (brotes esporádicos)",
        key_protein="Glicoproteína GP",
        protein_function="Entrada celular, evasión inmune",
        sequence="MWTTCFFISLILIQGIKTLPILEIASNNQPQNVDSVCSGTLQKTEDVHLMGFTLSGQKVADSPLEASKRWAFRTGVPPKNVEYTEGEEAKTCYNISILDGPPMLFDHSQTSDKGVYFHKEGAFFLYDRLASTVIYRGVNFAEGVIAFLILAKPKEYKLFFSSHPLRPVNTAEGHSDGLGAATKRWGFRAGVPPKVVSYEAGQWAESCYGLQEKPLSSRATVEMRQAPGSGFLTQSSCGYNGATNKGDIWIVMPKDELIKWAFWEKIKDNVTRMLIPKEPTVTAHEPTTQSCSVNQTGGRFCTTAQMSEILFPDFWMKSNPAKWNNCYTCSLSTVQQDNVPSPYTIGSSRSPPAPIYSVDLKNHSLLDLQKQLNILQNVLKPTASSPLQPLPTNPLTNPQDSNLSSQAPSKTSSPMEIYLKKQKQHNQATNFSGTVTIFKTEATDGLVIYVTLEILNEGFIQMLSTTQPHHLRSNDYTFLLTNQVRNLG",
        diseases=["Fiebre hemorrágica de Marburg"],
        notes="Primo del Ébola. Primer filovirus descubierto (1967)."
    ),
    
    LethalPathogen(
        name="Viruela",
        scientific_name="Variola major",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="30% (histórico)",
        annual_deaths="0 (erradicada 1980, ~500M muertes históricas)",
        key_protein="Proteína de fusión A28",
        protein_function="Fusión de membrana, entrada celular",
        sequence="MKRIFILACLSATTAYA" + "VLDKKQVLDMVNISDFPNVSSICNDYSELRVVDATSTCSSDGTCSPPLLLVHNGQDFKPGQNIYTIKAFDYYQSKGTLSICNQTSACLAYGTRCFAPVHCVQSKAKYNIVYRDRSQHCNDTTC",
        diseases=["Viruela mayor", "Viruela menor"],
        notes="Única enfermedad humana erradicada. Muestras en 2 laboratorios (CDC, VECTOR)."
    ),
    
    LethalPathogen(
        name="Influenza H5N1",
        scientific_name="Influenza A virus H5N1",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="60%",
        annual_deaths="~500 confirmados (potencial pandémico)",
        key_protein="Hemaglutinina H5",
        protein_function="Unión a receptores, fusión de membrana",
        sequence="MEKIVLLFAIVSLVKSDQICIGYHANNSTEQVDTIMEKNVTVTHAQDILEKTHNGKLCDLDGVKPLILRDCSVAGWLLGNPMCDEFINVPEWSYIVEKANPVNDLCYPGDFNDYEELKHLLSRINHFEKIQIIPKSSWSSHEASLGVSSACPYQGKSSFFRNVVWLIKKNSTYPTIKRSYNNTNQEDLLVLWGIHHPNDAAEQTKLYQNPTTYISVGTSTLNQRLVPRIATRSKVNGQSGRMEFFWTILKPNDAINFESNGNFIAPEYAYKIVKKGDSTIMKSELEYGNCNTKCQTPMGAINSSMPFHNIHPLTIGECPKYVKSNRLVLATGLRNSPQRERRRKKRGLFGAIAGFIEGGWQGMVDGWYGYHHSNEQGSGYAADKESTQKAIDGVTNKVNSIIDKMNTQFEAVGREFNNLERRIENLNKKMEDGFLDVWTYNAELLVLMENERTLDFHDSNVKNLYDKVRLQLRDNAKELGNGCFEFYHKCDNECMESVRNGTYDYPQYSEEARLKREEISGVKLESIGIYQI",
        diseases=["Gripe aviar", "Potencial pandemia"],
        notes="Altamente patógeno en aves. Pandemia potencial si muta para transmisión humana."
    ),
    
    LethalPathogen(
        name="Rabia",
        scientific_name="Rabies lyssavirus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="99.9% (sin tratamiento post-exposición)",
        annual_deaths="~59,000",
        key_protein="Glicoproteína G",
        protein_function="Unión a receptores neuronales, fusión",
        sequence="MVPQALLFVPLLVFPLCFGKFPIYTIPDKLGPWSPIDIHHLSCPNNLVVEDEGCTNLSGFSYMELKVGYISAIKVNGFTCTGVVTEAETYTNFVGYVTTTFKRKHFRPTPDACRAAYNWKMAGDPRYEESLHNPYPDYHWLRTVKTTKESLVIISPSVADLDPYDRSLHSRVFPSGKCSGITGTCVIKNTNVTKVDKRRRLVPPGN",
        diseases=["Rabia", "Hidrofobia"],
        notes="100% letal una vez aparecen síntomas. Solo 14 supervivientes documentados."
    ),
    
    # --- BACTERIA ---
    
    LethalPathogen(
        name="Ántrax",
        scientific_name="Bacillus anthracis",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="80-95% (inhalación sin tratamiento)",
        annual_deaths="~2,000 (natural), potencial bioterrorismo",
        key_protein="Factor Letal (LF)",
        protein_function="Metaloproteasa que destruye MAPK kinasas",
        sequence="MAGGHGDVGMHVKEKEKNKDENKRKDEERNKTQEEHLKEIMKHIVKIEVKGEEAVKKEAAEKLLEKVPSDVLEMYKAIGGKIYIVDGDITKHISLEALSEDKKKIKDIYGKDALLHEHYVYAKEGYEPVLVIQSSEDYVENTEKALNVYYEIGKILSRDILSKINQPYQKFLDVLNTIKNASDSDGQDLLFTNQLKEHPTDFSVEFLEQNSNEVQEVFAKAFAYYIEPQHRDVLQLYAPEAFNYMDKFNEQEINLSLEELKDQRMLSRYVNVIKKYGPSVVPDVILNADSSRKEGINLYIFKNIYKIYEITNN",
        diseases=["Ántrax cutáneo", "Ántrax pulmonar", "Ántrax gastrointestinal"],
        notes="Agente de bioterrorismo clase A. Esporas sobreviven décadas."
    ),
    
    LethalPathogen(
        name="Peste",
        scientific_name="Yersinia pestis",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="30-100% (sin tratamiento)",
        annual_deaths="~600",
        key_protein="Proteína F1 (Cápsula)",
        protein_function="Antifagocítica, evasión inmune",
        sequence="MKKISSVLAALAAVLPSAVAADLTDSNRANLVNKNSTNQTDAAVRWYNSSDQVTVKNGLPVSFSHDGGAISTTFVQVMNDGQPMTIVHNEVIAQDSSQEGGRAEEWKQLSASYDKFVVTAKAIKVAGLDVSNLGPNSAEAIGGGSTTEDDLAKIVDTFLDNSA",
        diseases=["Peste bubónica", "Peste neumónica", "Peste septicémica"],
        notes="Muerte Negra (1347-1351): 75-200M muertes. Pandemia más letal de la historia."
    ),
    
    LethalPathogen(
        name="Botulismo",
        scientific_name="Clostridium botulinum",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="5-10% (con tratamiento), 50%+ (sin)",
        annual_deaths="~100 (raros, pero toxina más letal conocida)",
        key_protein="Toxina Botulínica A",
        protein_function="Bloquea liberación de acetilcolina, parálisis",
        sequence="MPFVNKQFNYKDPVNGVDIAYIKIPNAGQMQPVKAFKIHNKIWVIPERDTFTNPEEGDLNPPPEAKQVPVSYYDSTYLSTDNEKDNYLKGVTKLFERIYSTDLGRMLLTSIVRGIPFWGGSTIDTELKVIDTNCINVIQPDGSYRSEELNLVIIGPSADIIQFECKSFGHEVLNLTRNGYGSTQYIRFSPDFTFGFEESLEVDTNPLLGAGKFATDPAVTLAHELIHAGHRLYGIAINPNRVFKVNTNAYYEMSGLEVSFEELRTFGGHDAKFIDSLQENEFRLYYYNKFKDIASTLNKAKSIVGTTASLQYMKNVFKEKYLLSEDTSGKFSVDKLKFDKLYKMLTEIYTEDNFVKFFKVLNRKTYLNFDKAVFKINIVPKVNYTIYDGFNLRNTNLAANFNGQNTEINNMNFTKLKNFTGLFEFYKLLCVRGIITSKTKSLDKGYNKALNDLCIKVNNWDLFFSPSEDNFTNDLNKGEEITSDTNIEAAEENISLDLIQQYYLTFNFDNEPENISIENLSSDIIGQLELMPNIERFPNGKKYELDKYTMFHYLRAQEFEHGKSRIALTNSVNEALLNPSRVYTFFSSDYVKKVNKATEAAMFLGWVEQLVYDFTDETSEVSTTDKIADITIIIPYIGPALNIGNMLYKDDFVGALIFSGAVILLEFIPEIAIPVLGTFALVSYIANKVLTVQTIDNALSKRNEKWDEVYKYIVTNWLAKVNTQIDLIRKKMKEALENQAEATKAIINYQYNQYTEEEKNNINFNIDDLSSKLNESINKAMININKFLNQCSVSYLMNSMIPYGVKRLEDFDASLKDALLKYIYDNRGTLIGQVDRLKDKVNNTLSTDIPFQLSKYVDNQRLLSTFTEYIKNIINTSILNLRYESNHLIDLSRYASKINIGSKVNFDPIDKNQIQLFNLESSKIEVILKNAIVYNSMYENFSTSFWIRIPKYFNSISLNNEYTIINCMENNSGWKVSLNYGEIIWTLQDTQEIKQRVVFKYSQMINISDYINRWIFVTITNNRLNNSKIYINGRLIDQKPISNLGNIHASNNIMFKLDGCRDTHRYIWIKYFNLFDKELNEKEIKDLYDNQSNSGILKDFWGDYLQYDKPYYMLNLYDPNKYVDVNNVGIRGYMYLKGPRGSVMTTNIYLNSSLYRGTKFIIKKYASGNKDNIVRNNDRVYINVVVKNKEYRLATNASQAGVEKILSALEIPDVGNLSQVVVMKSKNDQGITNKCKMNLQDNNGNDIGFIGFHQFNNIAKLVASNWYNRQIERSSRTLGCSWEFIPVDDGWGERPL",
        diseases=["Botulismo alimentario", "Botulismo infantil", "Botulismo por heridas"],
        notes="1 gramo puede matar 1 millón de personas. Usada en Botox en dosis mínimas."
    ),
    
    LethalPathogen(
        name="Tuberculosis MDR/XDR",
        scientific_name="Mycobacterium tuberculosis",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="40-60% (XDR-TB sin tratamiento)",
        annual_deaths="~1,300,000",
        key_protein="Antígeno ESAT-6",
        protein_function="Secreción ESX-1, virulencia, evasión inmune",
        sequence="MTEQQWNFAGIEAAASAIQGNVTSIHSLLDEGKQSLTKLAAAWGGSGSEAYQGVQQKWDATATELNNALQNLARTISEAGQAMASTEGNVTGMFA",
        diseases=["Tuberculosis pulmonar", "TB miliar", "TB meníngea"],
        notes="Mayor asesino bacteriano. 10M nuevos casos/año. Crisis de resistencia."
    ),
    
    # --- PARASITES ---
    
    LethalPathogen(
        name="Malaria (P. falciparum)",
        scientific_name="Plasmodium falciparum",
        category=PathogenCategory.PARASITE,
        threat_level=ThreatLevel.TIER_1,
        mortality_rate="15-20% (malaria cerebral)",
        annual_deaths="~619,000",
        key_protein="PfEMP1 (Eritrocyte Membrane Protein 1)",
        protein_function="Adhesión a endotelio, evasión del bazo",
        sequence="MKSFKNKKNDFKIVKNCISGICGKYSTKRKRSHTQENNKPFKNVNKKMNKKFKNNIIKRIFGKKQRKEKFVSSNEKYLIIFFILYIIFNPSLNLYTSIIYICVVPIVFPILGIFIYFQNLFQNLKKSYTPDFKGSQSLCLKGLSAASLALIASLSVSIFIPVKFLNKATYGKKNLFFHFKTKSTQELNNYCLLLIKDIVNQYGSNLVISGCKNWFKQPQLNLVIENPN",
        diseases=["Malaria cerebral", "Malaria grave", "Malaria congénita"],
        notes="Parásito más letal. 247M casos/año. Resistencia a artemisina emergiendo."
    ),
    
]

# =============================================================================
# TIER-2: HIGH THREAT PATHOGENS
# =============================================================================

TIER_2_PATHOGENS = [
    
    LethalPathogen(
        name="HIV-1",
        scientific_name="Human immunodeficiency virus 1",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="100% (sin tratamiento a largo plazo)",
        annual_deaths="~650,000",
        key_protein="Glicoproteína gp120",
        protein_function="Unión a CD4 y correceptores",
        sequence="MRVKEKYQHLWRWGWRWGTMLLGMLMICSATEKLWVTVYYGVPVWKEATTTLFCASDAKAYDTEVHNVWATHACVPTDPNPQEVVLVNVTENFNMWKNDMVEQMHEDIISLWDQSLKPCVKLTPLCVSLKCTDLKNDTNTNSSSGRMIMEKGEIKNCSFNISTSIRGKVQKEYAFFYKLDIIPIDNDTTSYKLTSCNTSVITQACPKVSFEPIPIHYCAPAGFAILKCNNKTFNGTGPCTNVSTVQCTHGIRPVVSTQLLLNGSLAEEEVVIRSVNFTDNAKTIIVQLNTSVEINCTRPNNNTRKSIRIQRGPGRAFVTIGKIGNMRQAHCNISRAKWNNTLKQIASKLREQFGNNKTIIFKQSSGGDPEIVTHSFNCGGEFFYCNSTQLFNSTWFNSTWSTEGSNNTEGSDTITLPCRIKQIINMWQKVGKAMYAPPISGQIRCSSNITGLLLTRDGGNSNNESEIFRPGGGDMRDNWRSELYKYKVVKIEPLGVAPTKAKRRVVQREKR",
        diseases=["SIDA", "Infecciones oportunistas"],
        notes="39M personas viven con VIH. Sin cura, pero controlable con TAR."
    ),
    
    LethalPathogen(
        name="Hepatitis B",
        scientific_name="Hepatitis B virus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="15-25% (cirrosis/cáncer)",
        annual_deaths="~820,000",
        key_protein="Antígeno de superficie HBsAg",
        protein_function="Entrada celular, evasión inmune",
        sequence="MENITSGFLGPLLVLQAGFFLLTRILTIPQSLDSWWTSLNFLGGTTVCLGQNSQSPTSNHSPTSCPPTCPGYRWMCLRRFIIFLFILLLCLIFLLVLLDYQGMLPVCPLIPGSSTTSTGPCRTCMTTAQGTSMYPSCCCTKPSDGNCTCIPIPSSWAFGKFLWEWASARFSWLSLLVPFVQWFVGLSPTVWLSVIWMMWYWGPSLYNILSPFLPLLPIFFCLWVYI",
        diseases=["Hepatitis crónica", "Cirrosis", "Carcinoma hepatocelular"],
        notes="296M infectados crónicos. Vacuna disponible pero subadministrada."
    ),
    
    LethalPathogen(
        name="Hepatitis C",
        scientific_name="Hepatitis C virus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="15-30% (cirrosis)",
        annual_deaths="~290,000",
        key_protein="Proteína E2 de envoltura",
        protein_function="Unión a receptor CD81, entrada",
        sequence="MHNYQAQQSYHATGNLPGCSFSIFLLALASCLTIPASAYEVRNVSGIYHVTNDCSNSSIVYEAADMIMHTPGCVPCVREGNASRCWVAVTPTVATRDGKLPTTQLRRHIDLLVGSATLCSALYVGDLCGSVFLVGQLFTFSPRRHWTTQDCNCSIYPGHITGHRMAWDMMMNWSPTAALVVAQLLRIPQAVMDMVAGAHWGVLAGLAYYSMVGNWAKVLIVMLLFAGVDGHTRV",
        diseases=["Hepatitis crónica", "Cirrosis", "Carcinoma hepatocelular"],
        notes="58M infectados crónicos. Curable con antivirales directos (90%+)."
    ),
    
    LethalPathogen(
        name="Dengue",
        scientific_name="Dengue virus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="1-5% (dengue grave)",
        annual_deaths="~40,000",
        key_protein="Proteína E de envoltura",
        protein_function="Fusión de membrana, entrada celular",
        sequence="MRCVGIGNRDFVEGLSGATWVDVVLEHGSCVTTMAKNKPTLDIELQKTEATQLATLRKLCIEGKITNITTDSRCPTQGEATLVEEQDTNFVCRRTFVDRGWGNGCGLFGKGSLITCAKFKCVTKLEGKIVQYENLKYSVIVTVHTGDQHQVGNETTEHGTIATITPQAPTSEIQLTDYGALTLDCSPRTGLDFNEMVLLTMKEKSWLVHKQWFLDLPLPWTSGASTSQETWNRQDLLVTFKTAHAKKQEVVVLGSQEGAMHTALTGATEIQNSGGTSIFAGHLKCRLKMDKLILKGMSYVMCTGSFKLEKEVAETQHGTVLVQVKYEGTDAPCKIPFSTQDEKGVTQNGRLITANPIVTDKEKPVNIEAEPPFGESYIVVGAGEKALKLSWFKKGSSIGKMFEATARGARRMAILGDTAWDFGSIGGVFTSVGKLIHQIFGTAYGVLFSGVSWTMKIGIGILLTWLGLNSRSTSLSMTCIAVGMVTLYLGVMVQA",
        diseases=["Fiebre del dengue", "Dengue hemorrágico", "Síndrome de shock"],
        notes="400M infecciones/año. 4 serotipos. Segunda infección más grave."
    ),
    
    LethalPathogen(
        name="Cólera",
        scientific_name="Vibrio cholerae",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="25-50% (sin tratamiento)",
        annual_deaths="~95,000",
        key_protein="Toxina colérica subunidad A",
        protein_function="ADP-ribosilación de Gs, diarrea masiva",
        sequence="MNIFTLLKFPTTITATSAENAKSSEVVNMDNDKEKNNESNEKTNATVAKSTKAEKQVKKTNLISNLNELSPQHENVLPGNYSKQLNMNVNKYQGSQVITLLNSGKHDEEGVIVKVSNDRTLSGKEEQSYAKYFSDEVVGQFQVVTNLAGDAIISEVYINSDMKNIFKNGYILGTQADITLDGGSRYAYTVNTDGNYKVIVDKNNQSYGSSDIYANDCKIVLLAGVFQVTTNANITTTNT",
        diseases=["Cólera"],
        notes="2-4M casos/año. Enfermedad de pobreza y desastres."
    ),
    
    LethalPathogen(
        name="SARS-CoV-2",
        scientific_name="Severe acute respiratory syndrome coronavirus 2",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="0.5-3% (variable por edad/comorbilidades)",
        annual_deaths="~3,000,000 (2020-2021), ahora <500,000",
        key_protein="Proteína Spike (S)",
        protein_function="Unión a ACE2, fusión de membrana",
        sequence="MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT",
        diseases=["COVID-19", "SARS", "Long COVID"],
        notes="Pandemia 2020-2023. >700M casos, >7M muertes confirmadas."
    ),
    
    LethalPathogen(
        name="Streptococcus pyogenes (Invasivo)",
        scientific_name="Streptococcus pyogenes",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="25-35% (fascitis necrotizante)",
        annual_deaths="~500,000",
        key_protein="Proteína M",
        protein_function="Antifagocítica, adhesión",
        sequence="MKRNEKLFKDLSNVTSVVNTTLIKKNFELTQLLKGDKLTQVLVDDDTRQAEKEAATQAQQELDKVKQKLDSYEKQVEKELSKLEGTLQSELRSLNDKDTKIKDLSSNMQEQLEDLIKTLNTLQRNSKALQAQVDKLTRDNLLAQQYKNAQDELSDAEKQLQANLTLLEKDIQNVQDNYKTQISQLKDELSEKEAQLKKQLEKQNRDLIQEKLTDLKATMENMGGGGAGSAVASAVGAGAALSLGGGAGGTTALSGCTAPAAKGDTTAPAKGDTTSAKGDTTSAKGDTTSAKGDSVTNLGGGGGSKGGFGVAA",
        diseases=["Fascitis necrotizante", "Síndrome de shock tóxico", "Fiebre reumática"],
        notes="'Bacteria comedora de carne'. 600M faringitis/año."
    ),
    
    LethalPathogen(
        name="MRSA",
        scientific_name="Staphylococcus aureus (MRSA)",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_2,
        mortality_rate="15-30% (bacteremia)",
        annual_deaths="~120,000",
        key_protein="PBP2a (Penicillin-Binding Protein 2a)",
        protein_function="Resistencia a beta-lactámicos",
        sequence="MKKIKIVPLILIFVLSFSFAYSKEQTYINQYYNSIDSYQKAFIKSHLSDDKISATKNQNSNNNRKPLKNAEDILNINYNQQKEVQYYSELANKLNKELAKSNNVDKILNNGIKILNSVSGEIQQNLKLGVKDDYSTYKTLNMSLYDNNQILFSNNNYLGITDQFNVQLTKDLPNLSQNKNEILSFNQTTYNSLVNKNQTVFYKNLNDTLILNTTTYGTKMTIITPGDNKGKLFMGSWGKTFFDSKASDKLITANLQGNLNQRSNIKLFNQNILQNTIQIGKGYMDLVGWNYNDMNDLSGMAGTINAADSSKWLFDKWTNQTLLGLKSNEITLLSSGNYIQQNATLLVQQYGSNITKQDLQQISQLAGKNIDKYLNSKSNIVLTDSQLYSGTSDRNINASQQINNLASQMYKGAQVVAQNFNLSTNALLSSFQIPGYYQSILYMKNNSVTNTGNMNYSLNNNNNILNQNQQTVLVPDYVLMGNQTISKSDVDTVQNKDVTTTNDTITVPITGQTSGSNTQLSLPTISSPTFPHTEPYTQIDPDQYNQLSTGASGTIPQDLVEVYATYQRLFKKPSILTVTDKDTITVKDKDKPKTGKPVTATAGVNELSNAKGNGDYDNNQYYGEVINSLGKFMQNPQDIDITKLTQEDMQGVSF",
        diseases=["Sepsis", "Neumonía", "Endocarditis", "Osteomielitis"],
        notes="Crisis de resistencia antibiótica. ESKAPE pathogen."
    ),
    
]

# =============================================================================
# TIER-3: SIGNIFICANT THREAT PATHOGENS
# =============================================================================

TIER_3_PATHOGENS = [
    
    LethalPathogen(
        name="Trypanosoma cruzi",
        scientific_name="Trypanosoma cruzi",
        category=PathogenCategory.PARASITE,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="5-10% (cardiomiopatía)",
        annual_deaths="~12,000",
        key_protein="Trans-sialidasa",
        protein_function="Transferencia de ácido siálico, evasión inmune",
        sequence="MQKLFSNDFAFSRNISSGVATAHSGNSSSSKRKISRKTPQDFKDSSANNGALHNKIYLGLAFGLSSLIVGLNMALFAALGSLGGTSNGKNSPTANNGIKNGLNNNKNNDNGLKNANGTKISSPKTSSIDNNISNINNNPTLTSKTITTNNPSVSSGTGGRFIVAIGGDGGNSSTRPSVLWTHGGHVVSAYNNDSGPWLKDNPFDAGRGTVDAGVNATRFVNGSAITSYLNVNISNGNSSRFIARGVGGSGTGSQVSVSDKGVPMAWGVGDGIGKNGPVTIVNSKGGQFTVVRVDNIINGNRAGNVINLTDGSRSNGFDYKGTHSAGGNVAVEGVATFVGTTGTPTGAGGDAGGNSSHSPSSGLCFRQQHAYWVGASNNVGHSGIINHNGHKSGILGQPNLSDGTHYTFGASNTGTSRNTGGTTGTTGTADGGTGTTGTTGTADGGTGTTGTTGTADGGTGTTGTTGTADGGTGTTGTTGAADGGDGTTGTTGTTGAADGGDGTTGTTGTTGTAGGSPSASQTSTGGMTSSPATSSS",
        diseases=["Enfermedad de Chagas", "Cardiomiopatía chagásica"],
        notes="6-7M infectados en Latinoamérica. 'Enfermedad silenciosa'."
    ),
    
    LethalPathogen(
        name="Leishmania donovani",
        scientific_name="Leishmania donovani",
        category=PathogenCategory.PARASITE,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="75-95% (kala-azar sin tratamiento)",
        annual_deaths="~30,000",
        key_protein="GP63 (Leishmanolisina)",
        protein_function="Metaloproteasa de superficie, evasión del complemento",
        sequence="MRAPLLRSLAALAALATLATAPTAPASPQGKSKIVVAVGNHEMGHELIGLVHQRSGPINQRSLHFLGGEQGTSDHVDEAWLKGANVEGSLFTRDTRFQPTQAAGLRKMKPTGETVHVVTFHGTPNDGHGTHVDGVFSAAFPGTHVNDRRGATGTFIAGHEIGHVGFVHQQNAVNITIGQSHNLCPAGSSGGSTSNGDCGDTCHKQQSCSSSPCCSKPCCSPTAPCAAGGCATTTTTTTTTTAAAAASSS",
        diseases=["Leishmaniasis visceral (Kala-azar)", "Leishmaniasis cutánea"],
        notes="1M nuevos casos/año. Segunda causa de muerte parasitaria."
    ),
    
    LethalPathogen(
        name="Candida auris",
        scientific_name="Candida auris",
        category=PathogenCategory.FUNGUS,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="30-60%",
        annual_deaths="~10,000 (estimado, emergente)",
        key_protein="Adhesina Als3",
        protein_function="Adhesión a células huésped, formación de biofilm",
        sequence="MKFSTILFATTALVAQASTSTSNVTITGSGNDTVTINSETGTTTTTLSFKNITDIDKNAKTVTLGCSISNGSVITVQASNDGSTTLTFSGNAKATSIDGNNTFSFSLSGSTTITLEGPNTTTITGSGNDTVTFNSVSGGTTTTLSFKNITDIDKNSKTVTLGCSISNGSVITVQATGDGSTTLTFSGNAKATSIDGNNTFSFSLSGSTTITVEG",
        diseases=["Candidemia", "Infecciones invasivas"],
        notes="Hongo emergente multirresistente. 'Superbug' fúngico. CDC: Amenaza Urgente."
    ),
    
    LethalPathogen(
        name="Trypanosoma brucei",
        scientific_name="Trypanosoma brucei",
        category=PathogenCategory.PARASITE,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="100% (sin tratamiento)",
        annual_deaths="<1,000 (casi eliminada)",
        key_protein="VSG (Variable Surface Glycoprotein)",
        protein_function="Variación antigénica, evasión inmune",
        sequence="MFNRLVFAAFAAIVLVSLYSNAKAQNEGKEATAAEKTAQQQAANSTANQGAAANTGSPVEANAQETAKTEAKAPAANTKPAAKAEAQKAQTKAQTKAEGKAQTPAAQKQANQKADNQKAQNKQSDAQKQQNTTTAQKAQSTPQVNATAKVQSRPAAQQDVAKTAASAQTTAQTTAQTTAQTTAEETNGKKNGDPANAQTATAANANATATCNSS",
        diseases=["Enfermedad del sueño africana"],
        notes="Casi eliminada gracias a control de vectores. Modelo de evasión inmune."
    ),
    
    LethalPathogen(
        name="Neisseria meningitidis",
        scientific_name="Neisseria meningitidis",
        category=PathogenCategory.BACTERIA,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="10-15%",
        annual_deaths="~50,000",
        key_protein="Porina PorA",
        protein_function="Porina de membrana externa, adhesión",
        sequence="MKKTNKLTLALTAGSAVAAADTSIASGFAGNSSSLAPEVQRYNFQPNTGVGVASFAFGDSGSSNGRNSRVSVDYGDQSTGQAAYEVNLGGRYSYRGRYFAADPKSNNQAHGSVASQVNVGGARFGSRFPETGYKGSVNYDEEQTNKSVSGIGGSFNAGSGTDVNISVQNKDDKSLNGDKLTGQGRLGDAEHTFKGGVKLGAIPINTTGGDYHTYARLFAYSYQNKGGYGEASYGQGEQIIHHDPAVVGTKGYSLQPNTTYANNYTRNQVHVGTYNYKDLHTGHYVPVAAKVQDQDTATFKKSYDIVGKYGLYSLQQGKDLSLGNKKVGTLKFNDRYFDVAAKNQGYSGAFSSQYDSAHVFGFGAPRKAGFKKSF",
        diseases=["Meningitis bacteriana", "Meningococcemia"],
        notes="Brotes en 'cinturón de meningitis' africano. Vacunas disponibles."
    ),
    
]

# =============================================================================
# EMERGING THREATS
# =============================================================================

EMERGING_PATHOGENS = [
    
    LethalPathogen(
        name="Nipah virus",
        scientific_name="Nipah henipavirus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.EMERGING,
        mortality_rate="40-75%",
        annual_deaths="<100 (brotes limitados)",
        key_protein="Glicoproteína G",
        protein_function="Unión a receptor Ephrin-B2/B3",
        sequence="MPAINGKLVLFLSVLSLNVAFSAKDKVVISWDFVEDPSEISDCQLTGSLISNCRKSKRPSGTRLPASKVNSYGSAGNTLYLTRPPSDNQVSIRLLSGIQQLSNISLGTIQQQLEKIQEIIRSGSSTSWIQSQTGSRDSIGIVGVALGVATSAQITAAVALVEAKQARSDIEKLKNNINTIATNTATMQKTLQFPLLGTTLAALTVTAIAVATVLCRIRKSSNCGGECSYTPPSTGRDCSYLAEPLVQGQGLCLQGQNIYTCECNTGVTGCPTGSAINIPNGSIPQDCTAVTGNRLLIPITSENGPVSGQITSSYVPTGGR",
        diseases=["Encefalitis por Nipah"],
        notes="OMS: Top 10 amenazas. Reservorio: murciélagos. Sin tratamiento."
    ),
    
    LethalPathogen(
        name="Virus de Lassa",
        scientific_name="Lassa mammarenavirus",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.EMERGING,
        mortality_rate="1-15% (30% en hospitalizados)",
        annual_deaths="~5,000",
        key_protein="Glicoproteína GPC",
        protein_function="Entrada celular via α-dystroglycan",
        sequence="MGQIVTMFEALPHIIDEVINIVIIVLIVITGIIKLNKWKSIKDKQLQGLDISALSGFLCLAGKLAGNNSVSAKNSANMDFNSNKSYIYSDHCSAFCLNNSYLNLTPLVFIYKDKLVLSLKGNGCTAIYKSRCTRGFMSKSYLVITFLVLLYLVNHLTKKKDIKGVQNLYKIGNYTLLLKALDEIQNRYSRNVDIQLRTASVRSQDAPRDSFTFATMSNITLFDCLKNKSDYYYNTTEGFGKDKMLVPRSGYLMIGKMLTLLNGLLDEDLDSQSLIESLKSHLGLIGGAFSILLHSLLVLWQLLSEQITDLRSASKSRGVEQIMQNVKAKGDLRLSGLFTWTLSDSEGNETPGGYCLTRWMLIEAELLLARRLNLNHIYRDGISAWLTQNGDSPCHLFISHKGNDTIKQIRGNLTNTHYCGLAQLNYQPLKNEVSHLYDGKSLEASKRVYLAGSKGIFFPVMLALVLAFLLAIPVLQLSYQAWRRLLRTFSMKNKRLQNSFQKQQENTNAFISSWSKFDFN",
        diseases=["Fiebre de Lassa"],
        notes="Endémico en África Occidental. 100,000-300,000 casos/año."
    ),
    
    LethalPathogen(
        name="Priones (CJD)",
        scientific_name="Prion protein (PrP^Sc)",
        category=PathogenCategory.PRION,
        threat_level=ThreatLevel.EMERGING,
        mortality_rate="100%",
        annual_deaths="~1,000",
        key_protein="Proteína Prión (forma patológica)",
        protein_function="Conversión autocatalítica de PrP^C a PrP^Sc",
        sequence="MANLGCWMLVLFVATWSDLGLCKKRPKPGGWNTGGSRYPGQGSPGGNRYPPQGGGGWGQPHGGGWGQPHGGGWGQPHGGGWGQPHGGGWGQGGGTHSQWNKPSKPKTNMKHMAGAAAAGAVVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG",
        diseases=["Enfermedad de Creutzfeldt-Jakob", "Kuru", "Insomnio familiar fatal"],
        notes="100% letal. Sin tratamiento. Mal plegamiento proteico autocatalítico."
    ),
    
]

# =============================================================================
# COMPLETE DATABASE
# =============================================================================

ALL_PATHOGENS = TIER_1_PATHOGENS + TIER_2_PATHOGENS + TIER_3_PATHOGENS + EMERGING_PATHOGENS

# Human controls for testing
HUMAN_CONTROLS = [
    LethalPathogen(
        name="Hemoglobina Alfa Humana",
        scientific_name="Homo sapiens (HBA1)",
        category=PathogenCategory.VIRUS,  # dummy, will be overridden
        threat_level=ThreatLevel.TIER_3,   # dummy
        mortality_rate="N/A",
        annual_deaths="N/A",
        key_protein="Hemoglobin alpha",
        protein_function="Transporte de oxígeno",
        sequence="MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR",
        diseases=[],
        notes="Control humano - NO debe ser atacado"
    ),
    LethalPathogen(
        name="Insulina Humana",
        scientific_name="Homo sapiens (INS)",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="N/A",
        annual_deaths="N/A",
        key_protein="Insulin",
        protein_function="Regulación de glucosa",
        sequence="MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN",
        diseases=[],
        notes="Control humano - NO debe ser atacado"
    ),
    LethalPathogen(
        name="ADN Mitocondrial Humano (D-Loop)",
        scientific_name="Homo sapiens (mtDNA)",
        category=PathogenCategory.VIRUS,
        threat_level=ThreatLevel.TIER_3,
        mortality_rate="N/A",
        annual_deaths="N/A",
        key_protein="Mitochondrial D-loop",
        protein_function="Región de control mitocondrial",
        sequence="GATCACAGGTCTATCACCCTATTAACCACTCACGGGAGCTCTCCATGCATTTGGTATTTTCGTCTGGGGGGTGTGCACGCGATAGCATTGCGAGACGCTGGAGCCGGAGCACCCTATGTCGCAGTATCTGTCTTTGATTCCTGCCTCATTCTATTATTTATCGCACCTACGTTCAATATTACAGGCGAACATACCTACTAAAGTGTGTTAATTAATTAATGCTTGTAGGACATAATAATAACAATTGAAT",
        diseases=[],
        notes="Control humano - NO debe ser atacado"
    ),
]


def get_all_pathogens() -> List[LethalPathogen]:
    """Return complete list of lethal pathogens."""
    return ALL_PATHOGENS


def get_pathogens_by_tier(tier: ThreatLevel) -> List[LethalPathogen]:
    """Get pathogens by threat level."""
    return [p for p in ALL_PATHOGENS if p.threat_level == tier]


def get_pathogens_by_category(category: PathogenCategory) -> List[LethalPathogen]:
    """Get pathogens by type (virus, bacteria, etc.)."""
    return [p for p in ALL_PATHOGENS if p.category == category]


def get_human_controls() -> List[LethalPathogen]:
    """Return human control sequences for testing."""
    return HUMAN_CONTROLS


def print_database_summary():
    """Print summary of pathogen database."""
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   BASE DE DATOS DE PATÓGENOS LETALES - D10Z-TTA                             ║
║   Isis-Sahana Eradication Target Library                                     ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   TIER-1 (Máxima Amenaza):        {len(TIER_1_PATHOGENS):>3} patógenos                            ║
║   TIER-2 (Alta Amenaza):          {len(TIER_2_PATHOGENS):>3} patógenos                            ║
║   TIER-3 (Amenaza Significativa): {len(TIER_3_PATHOGENS):>3} patógenos                            ║
║   EMERGENTES:                     {len(EMERGING_PATHOGENS):>3} patógenos                            ║
║   ──────────────────────────────────────────────────────────────────────────  ║
║   TOTAL OBJETIVOS:                {len(ALL_PATHOGENS):>3} patógenos                            ║
║   CONTROLES HUMANOS:              {len(HUMAN_CONTROLS):>3} secuencias                           ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   Por Categoría:                                                             ║
║   • Virus:      {len([p for p in ALL_PATHOGENS if p.category == PathogenCategory.VIRUS]):>3}                                                        ║
║   • Bacterias:  {len([p for p in ALL_PATHOGENS if p.category == PathogenCategory.BACTERIA]):>3}                                                        ║
║   • Parásitos:  {len([p for p in ALL_PATHOGENS if p.category == PathogenCategory.PARASITE]):>3}                                                        ║
║   • Hongos:     {len([p for p in ALL_PATHOGENS if p.category == PathogenCategory.FUNGUS]):>3}                                                        ║
║   • Priones:    {len([p for p in ALL_PATHOGENS if p.category == PathogenCategory.PRION]):>3}                                                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    print_database_summary()
    
    print("\nLISTA COMPLETA DE OBJETIVOS:\n")
    print(f"{'#':<3} {'Nombre':<35} {'Categoría':<12} {'Tier':<25} {'Mortalidad':<15}")
    print("─" * 95)
    
    for i, p in enumerate(ALL_PATHOGENS, 1):
        print(f"{i:<3} {p.name:<35} {p.category.value:<12} {p.threat_level.value:<25} {p.mortality_rate:<15}")
    
    print("\n" + "─" * 95)
    print(f"Total: {len(ALL_PATHOGENS)} patógenos letales identificados para erradicación Isis-Sahana")
