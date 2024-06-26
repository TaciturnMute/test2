from __future__ import annotations

TRAIN_START_DATE = "2019-01-01"
TRAIN_END_DATE = "2019-12-31"

TEST_START_DATE = "2020-01-01"
TEST_END_DATE = "2020-12-31"

TRADE_START_DATE = "2021-01-01"
TRADE_END_DATE = "2021-07-31"

def func(a):
    print(a)


NAME= "wenhao"

PATH_OF_DATA = "data"


FAANG_TICKER = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]

# Dow 30 constituents at 2019/01
DOW_30_TICKER = [
    "AAPL",
    "MSFT",
    "JPM",
    "V",
    "RTX",
    "PG",
    "GS",
    "NKE",
    "DIS",
    "AXP",
    "HD",
    "INTC",
    "WMT",
    "IBM",
    "MRK",
    "UNH",
    "KO",
    "CAT",
    "TRV",
    "JNJ",
    "CVX",
    "MCD",
    "VZ",
    "CSCO",
    "XOM",
    "BA",
    "MMM",
    "PFE",
    "WBA",
    "DD",
]

#Dow 30 constituents at 2023/02
#来源：https://zh.wikipedia.org/wiki/%E9%81%93%E7%90%BC%E6%96%AF%E5%B7%A5%E4%B8%9A%E5%B9%B3%E5%9D%87%E6%8C%87%E6%95%B0
#包含30支股票。与finrl提供的股票相比，少了{'XOM', 'RTX', 'DD', 'PFE'}，多了{'NYSE', 'AMGN', 'DOW'}
DOW_30_TICKER_2023_wiki = [
    'AMGN',
    'MMM',
    'AXP',
    'AAPL',
    'BA',
    'CAT',
    'CVX',
    'CSCO',
    'KO',
    'DOW',
    'GS',
    'HD',
    'HON',
    'IBM',
    'INTC',
    'JNJ',
    'JPM',
    'MCD',
    'MRK',
    'MSFT',
    'NKE',
    'PG',
    'CRM',
    'TRV',
    'UNH',
    'VZ',
    'V',
    'WBA',
    'WMT',
    'DIS',
]

#--------------------------------------------------------------------------------------------------------------------#
# Nasdaq 100 constituents at 2019/01
#finrl提供。
#共100支。比较久远，现今已有较大改动。
NAS_100_TICKER_2019_finrl = [
    "AMGN",
    "AAPL",
    "AMAT",
    "INTC",
    "PCAR",
    "PAYX",
    "MSFT",
    "ADBE",
    "CSCO",
    "XLNX",  ###################
    "QCOM",
    "COST",
    "SBUX",
    "FISV",
    "CTXS", ###################33
    "INTU",
    "AMZN",
    "EBAY",
    "BIIB",
    "CHKP",
    "GILD",
    "NLOK",
    "CMCSA",
    "FAST",
    "ADSK",
    "CTSH",
    "NVDA",
    "GOOGL",
    "ISRG",
    "VRTX",
    "HSIC",
    "BIDU",
    "ATVI", ########################
    "ADP",
    "ROST", ################
    "ORLY",
    "CERN",  ################
    "BKNG",  ###########
    "MYL",   # MYLK.V
    "MU",
    "DLTR",
    "ALXN", #######3
    "SIRI",
    "MNST",
    "AVGO",
    "TXN",
    "MDLZ",
    "FB",   #改名为meta
    "ADI",
    "WDC",
    "REGN",
    "LBTYK",
    "VRSK",
    "NFLX",
    "TSLA",
    "CHTR",
    "MAR",
    "ILMN",
    "LRCX",
    "EA",
    "AAL",
    "WBA",
    "KHC",
    "BMRN",
    "JD",
    "SWKS",
    "INCY",
    "PYPL",
    "CDW",
    "FOXA",
    "MXIM",    #ADI收购
    "TMUS",
    "EXPE",
    "TCOM",
    "ULTA",
    "CSX",
    "NTES",
    "MCHP",
    "CTAS",
    "KLAC",
    "HAS",
    "JBHT",
    "IDXX",
    "WYNN",
    "MELI",
    "ALGN",
    "CDNS",
    "WDAY",
    "SNPS",
    "ASML",
    "TTWO",
    "PEP",
    "NXPI",
    "XEL",
    "AMD",
    "NTAP",
    "VRSN",
    "LULU",
    "WLTW", #########333
    "UAL",
]

# Nasdaq 100 constituents at 2023/2
#来源：https://zh.wikipedia.org/zh-cn/%E7%B4%8D%E6%96%AF%E9%81%94%E5%85%8B100%E6%8C%87%E6%95%B8#2022%E5%B9%B4，维基百科
#含有101支。与aastock相比，没有ENPH，有OKTA。
NAS_100_TICKER_2023_wiki = [
    'ABNB',
    'ATVI',
    'ADBE',
    'AMD',
    'ALGN',
    'GOOGL',
    'GOOG',
    'AMZN',
    'AEP',
    'AMGN',
    'ADI',
    'ANSS',
    'AAPL',
    'AMAT',
    'ASML',
    'TEAM',
    'ADSK',
    'ADP',
    'AZN',
    'BIIB',
    'BKNG',
    'BKR',
    'AVGO',
    'CDNS',
    'CEG',
    'CHTR',
    'CTAS',
    'CSCO',
    'CSGP',
    'CTSH',
    'CMCSA',
    'CPRT',
    'COST',
    'CRWD',
    'CSX',
    'DDOG',
    'DXCM',
    'DLTR',
    'EBAY',
    'EA',
    'EXC',
    'FANG',
    'FAST',
    'META',
    'FISV',
    'FTNT',
    'GFS',
    'GILD',
    'HON',
    'IDXX',
    'ILMN',
    'INTC',
    'INTU',
    'ISRG',
    'JD',
    'KDP',
    'KLAC',
    'KHC',
    'LCID',
    'LRCX',
    'LULU',
    'MAR',
    'MRVL',
    'MELI',
    'MCHP',
    'MU',
    'MSFT',
    'MRNA',
    'MDLZ',
    'MNST',
    'NFLX',
    'NVDA',
    'NXPI',
    'ODFL',
    'ORLY',
    'OKTA',
    'PANW',
    'PCAR',
    'PAYX',
    'PYPL',
    'PEP',
    'PDD',
    'QCOM',
    'REGN',
    'RIVN',
    'ROST',
    'SGEN',
    'SIRI',
    'SBUX',
    'SNPS',
    'TMUS',
    'TSLA',
    'TXN',
    'VRSK',
    'VRTX',
    'WBA',
    'WBD',
    'WDAY',
    'XEL',
    'ZM',
    'ZS',

]

#来源：http://www.aastocks.com/tc/usq/market/nasdaq100.aspx，阿斯达克财经
#含有101支。与wiki相比，没有OKTA，有ENPH
NAS_100_TICKER_2023_aastocks = [
    'AAPL',
    'MSFT',
    'GOOG',
    'GOOGL',
    'AMZN',
    'TSLA',
    'NVDA',
    'META',
    'AVGO',
    'ASML',
    'PEP',
    'COST',
    'CSCO',
    'TMUS',
    'TXN',
    'CMCSA',
    'ADBE',
    'NFLX',
    'QCOM',
    'HON',
    'AMD',
    'AMGN',
    'SBUX',
    'PDD',
    'INTU',
    'INTC',
    'GILD',
    'AMAT',
    'BKNG',
    'ADI',
    'ADP',
    'MDLZ',
    'REGN',
    'PYPL',
    'ISRG',
    'ABNB',
    'VRTX',
    'FISV',
    'JD',
    'LRCX',
    'CSX',
    'MU',
    'MELI',
    'ATVI',
    'CHTR',
    'SNPS',
    'MRNA',
    'KLAC',
    'CDNS',
    'MAR',
    'MNST',
    'ORLY',
    'KDP',
    'WDAY',
    'KHC',
    'NXPI',
    'FTNT',
    'MCHP',
    'CTAS',
    'DXCM',
    'ADSK',
    'TEAM',
    'PAYX',
    'EXC',
    'LULU',
    'BIIB',
    'IDXX',
    'MRVL',
    'ROST',
    'PCAR',
    'ODFL',
    'WBD',
    'GFS',
    'XEL',
    'CPRT',
    'SGEN',
    'DLTR',
    'CTSH',
    'ILMN',
    'BKR',
    'WBA',
    'EA',
    'FAST',
    'ENPH',
    'CSGP',
    'CRWD',
    'VRSK',
    'ANSS',
    'FANG',
    'EBAY',
    'CEG',
    'DDOG',
    'ALGN',
    'ZM',
    'ZS',
    'SIRI',
    'LCID',
    'RIVN',
    'AEP',
    'AZN',
    'PANW',
]

#-------------------------------------------------------------------------------------------------------------------#
# SP 500 constituents at 2019
SP_500_TICKER = [
    "A",
    "AAL",
    "AAP",
    "AAPL",
    "ABBV",
    "ABC",
    "ABMD",
    "ABT",
    "ACN",
    "ADBE",
    "ADI",
    "ADM",
    "ADP",
    "ADS",
    "ADSK",
    "AEE",
    "AEP",
    "AES",
    "AFL",
    "AGN",
    "AIG",
    "AIV",
    "AIZ",
    "AJG",
    "AKAM",
    "ALB",
    "ALGN",
    "ALK",
    "ALL",
    "ALLE",
    "ALXN",
    "AMAT",
    "AMCR",
    "AMD",
    "AME",
    "AMG",
    "AMGN",
    "AMP",
    "AMT",
    "AMZN",
    "ANET",
    "ANSS",
    "ANTM",
    "AON",
    "AOS",
    "APA",
    "APD",
    "APH",
    "APTV",
    "ARE",
    "ARNC",
    "ATO",
    "ATVI",
    "AVB",
    "AVGO",
    "AVY",
    "AWK",
    "AXP",
    "AZO",
    "BA",
    "BAC",
    "BAX",
    "BBT",
    "BBY",
    "BDX",
    "BEN",
    "BF.B",
    "BHGE",
    "BIIB",
    "BK",
    "BKNG",
    "BLK",
    "BLL",
    "BMY",
    "BR",
    "BRK.B",
    "BSX",
    "BWA",
    "BXP",
    "C",
    "CAG",
    "CAH",
    "CAT",
    "CB",
    "CBOE",
    "CBRE",
    "CBS",
    "CCI",
    "CCL",
    "CDNS",
    "CE",
    "CELG",
    "CERN",
    "CF",
    "CFG",
    "CHD",
    "CHRW",
    "CHTR",
    "CI",
    "CINF",
    "CL",
    "CLX",
    "CMA",
    "CMCSA",
    "CME",
    "CMG",
    "CMI",
    "CMS",
    "CNC",
    "CNP",
    "COF",
    "COG",
    "COO",
    "COP",
    "COST",
    "COTY",
    "CPB",
    "CPRI",
    "CPRT",
    "CRM",
    "CSCO",
    "CSX",
    "CTAS",
    "CTL",
    "CTSH",
    "CTVA",
    "CTXS",
    "CVS",
    "CVX",
    "CXO",
    "D",
    "DAL",
    "DD",
    "DE",
    "DFS",
    "DG",
    "DGX",
    "DHI",
    "DHR",
    "DIS",
    "DISCK",
    "DISH",
    "DLR",
    "DLTR",
    "DOV",
    "DOW",
    "DRE",
    "DRI",
    "DTE",
    "DUK",
    "DVA",
    "DVN",
    "DXC",
    "EA",
    "EBAY",
    "ECL",
    "ED",
    "EFX",
    "EIX",
    "EL",
    "EMN",
    "EMR",
    "EOG",
    "EQIX",
    "EQR",
    "ES",
    "ESS",
    "ETFC",
    "ETN",
    "ETR",
    "EVRG",
    "EW",
    "EXC",
    "EXPD",
    "EXPE",
    "EXR",
    "F",
    "FANG",
    "FAST",
    "FB",
    "FBHS",
    "FCX",
    "FDX",
    "FE",
    "FFIV",
    "FIS",
    "FISV",
    "FITB",
    "FLIR",
    "FLS",
    "FLT",
    "FMC",
    "FOXA",
    "FRC",
    "FRT",
    "FTI",
    "FTNT",
    "FTV",
    "GD",
    "GE",
    "GILD",
    "GIS",
    "GL",
    "GLW",
    "GM",
    "GOOG",
    "GPC",
    "GPN",
    "GPS",
    "GRMN",
    "GS",
    "GWW",
    "HAL",
    "HAS",
    "HBAN",
    "HBI",
    "HCA",
    "HCP",
    "HD",
    "HES",
    "HFC",
    "HIG",
    "HII",
    "HLT",
    "HOG",
    "HOLX",
    "HON",
    "HP",
    "HPE",
    "HPQ",
    "HRB",
    "HRL",
    "HSIC",
    "HST",
    "HSY",
    "HUM",
    "IBM",
    "ICE",
    "IDXX",
    "IEX",
    "IFF",
    "ILMN",
    "INCY",
    "INFO",
    "INTC",
    "INTU",
    "IP",
    "IPG",
    "IPGP",
    "IQV",
    "IR",
    "IRM",
    "ISRG",
    "IT",
    "ITW",
    "IVZ",
    "JBHT",
    "JCI",
    "JEC",
    "JEF",
    "JKHY",
    "JNJ",
    "JNPR",
    "JPM",
    "JWN",
    "K",
    "KEY",
    "KEYS",
    "KHC",
    "KIM",
    "KLAC",
    "KMB",
    "KMI",
    "KMX",
    "KO",
    "KR",
    "KSS",
    "KSU",
    "L",
    "LB",
    "LDOS",
    "LEG",
    "LEN",
    "LH",
    "LHX",
    "LIN",
    "LKQ",
    "LLY",
    "LMT",
    "LNC",
    "LNT",
    "LOW",
    "LRCX",
    "LUV",
    "LW",
    "LYB",
    "M",
    "MA",
    "MAA",
    "MAC",
    "MAR",
    "MAS",
    "MCD",
    "MCHP",
    "MCK",
    "MCO",
    "MDLZ",
    "MDT",
    "MET",
    "MGM",
    "MHK",
    "MKC",
    "MKTX",
    "MLM",
    "MMC",
    "MMM",
    "MNST",
    "MO",
    "MOS",
    "MPC",
    "MRK",
    "MRO",
    "MS",
    "MSCI",
    "MSFT",
    "MSI",
    "MTB",
    "MTD",
    "MU",
    "MXIM",
    "MYL",
    "NBL",
    "NCLH",
    "NDAQ",
    "NEE",
    "NEM",
    "NFLX",
    "NI",
    "NKE",
    "NKTR",
    "NLSN",
    "NOC",
    "NOV",
    "NRG",
    "NSC",
    "NTAP",
    "NTRS",
    "NUE",
    "NVDA",
    "NWL",
    "NWS",
    "O",
    "OI",
    "OKE",
    "OMC",
    "ORCL",
    "ORLY",
    "OXY",
    "PAYX",
    "PBCT",
    "PCAR",
    "PEG",
    "PEP",
    "PFE",
    "PFG",
    "PG",
    "PGR",
    "PH",
    "PHM",
    "PKG",
    "PKI",
    "PLD",
    "PM",
    "PNC",
    "PNR",
    "PNW",
    "PPG",
    "PPL",
    "PRGO",
    "PRU",
    "PSA",
    "PSX",
    "PVH",
    "PWR",
    "PXD",
    "PYPL",
    "QCOM",
    "QRVO",
    "RCL",
    "RE",
    "REG",
    "REGN",
    "RF",
    "RHI",
    "RJF",
    "RL",
    "RMD",
    "ROK",
    "ROL",
    "ROP",
    "ROST",
    "RSG",
    "RTN",
    "SBAC",
    "SBUX",
    "SCHW",
    "SEE",
    "SHW",
    "SIVB",
    "SJM",
    "SLB",
    "SLG",
    "SNA",
    "SNPS",
    "SO",
    "SPG",
    "SPGI",
    "SRE",
    "STI",
    "STT",
    "STX",
    "STZ",
    "SWK",
    "SWKS",
    "SYF",
    "SYK",
    "SYMC",
    "SYY",
    "T",
    "TAP",
    "TDG",
    "TEL",
    "TFX",
    "TGT",
    "TIF",
    "TJX",
    "TMO",
    "TMUS",
    "TPR",
    "TRIP",
    "TROW",
    "TRV",
    "TSCO",
    "TSN",
    "TSS",
    "TTWO",
    "TWTR",
    "TXN",
    "TXT",
    "UA",
    "UAL",
    "UDR",
    "UHS",
    "ULTA",
    "UNH",
    "UNM",
    "UNP",
    "UPS",
    "URI",
    "USB",
    "UTX",
    "V",
    "VAR",
    "VFC",
    "VIAB",
    "VLO",
    "VMC",
    "VNO",
    "VRSK",
    "VRSN",
    "VRTX",
    "VTR",
    "VZ",
    "WAB",
    "WAT",
    "WBA",
    "WCG",
    "WDC",
    "WEC",
    "WELL",
    "WFC",
    "WHR",
    "WLTW",
    "WM",
    "WMB",
    "WMT",
    "WRK",
    "WU",
    "WY",
    "WYNN",
    "XEC",
    "XEL",
    "XLNX",
    "XOM",
    "XRAY",
    "XRX",
    "XYL",
    "YUM",
    "ZBH",
    "ZION",
    "ZTS",
]



