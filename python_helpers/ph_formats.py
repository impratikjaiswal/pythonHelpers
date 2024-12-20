class PhFormats:
    TXT = 'txt'
    ASN = 'asn'
    ASN1 = 'asn1'
    BASE_64 = 'base64'
    HEX = 'hex'
    YML = 'yml'
    YAML = 'yaml'
    JSON = 'json'
    IN = 'in'
    OUT = 'out'
    CSV = 'csv'
    XLSX = 'xlsx'
    XLS = 'xls'
    PNG = 'png'
    SVG = 'svg'
    JPG = 'jpg'
    JPEG = 'jpeg'
    BKP = 'bkp'
    TMP = 'tmp'
    PY = 'py'
    JAVA = 'java'
    _7Z = '7z'
    ZIP = 'zip'
    HASH = 'hash'
    FUNCTION_SPECIFIC = 'function_specific'
    ASN_ORG = 'asn_org'
    ASN_MANUALLY_CORRECTED = 'asn_manually_corrected'
    ASN_AUTO_CORRECTED = 'asn_auto_corrected'
    ASN_FORMATTED = 'asn_formatted'
    PNG_URI = 'png_uri'
    SVG_URI = 'svg_uri'


class PhFormatsGroups:
    ARCHIVE_OUTPUT_FORMATS_SUPPORTED = [
        PhFormats.ZIP,
    ]
