# ═══ PyVault ═══
__VAULT_PACK_VENDOR__ = "PyVault"
__VAULT_PACK_REV__ = 2
__VAULT_PACK_SCHEME__ = "vault-stream-v2"
__VAULT_CONTACT__ = "@Developyer"
# ═══════════════

def _vault_xd(key, data):
    kb = key.encode("utf-8")
    return ''.join(chr(v ^ kb[i % len(kb)]) for i, v in enumerate(data))

def _vault_kdf(seed, salt):
    import hashlib
    return hashlib.pbkdf2_hmac('sha256', seed, salt, 150000, dklen=32)

def _vault_stream(key, blob):
    import hashlib
    out = bytearray(len(blob))
    pos = 0
    ctr = 0
    while pos < len(blob):
        blk = hashlib.sha256(key + ctr.to_bytes(8, 'big')).digest()
        n = min(len(blk), len(blob) - pos)
        for i in range(n):
            out[pos + i] = blob[pos + i] ^ blk[i]
        pos += n
        ctr += 1
    return bytes(out)

_pv_b64 = __import__(_vault_xd('ыЭЗрЪ', [179, 234, 163, 200, 230, 163]))
_pv_tar = __import__(_vault_xd('ыЭЗрЪ', [165, 234, 162, 203, 185, 251, 180]))
_pv_tmp = __import__(_vault_xd('ыЭЗрЪ', [165, 238, 189, 221, 182, 254, 189, 229]))
_pv_os = __import__(_vault_xd('ыЭЗрЪ', [190, 248]))
_pv_sys = __import__(_vault_xd('ыЭЗрЪ', [162, 242, 163]))

ВзЄпЪБС = bytes.fromhex('d7015d0517f2aea523f1a275db857b5d')
дыЇГШСЙыРЙ = _vault_xd('боп', [92, 23, 43, 64, 222, 50, 132, 184, 77, 122, 55, 22, 89, 210, 252, 40, 126, 117, 193, 195, 46, 157, 49, 91, 218, 129, 96, 74, 138, 137, 182, 111]).encode('latin-1')
ФЃЕКХЩЫЫжЅЇ = _vault_kdf(дыЇГШСЙыРЙ, ВзЄпЪБС)
юЅЯъНиэшсПЅЄ = 'lL7%l-pDKQ>Nr9YMM3a*AVRQB#A?JuhQgFH*q1c29{#6|K{wB@Csk%n#GQAItiVRT)fcn1y?hK{q>vd`Nxd8FKqA_K<OJz=io={C%nVt$aM_GvM4B2HDBTZnX(fP~1lHR)_TKho>`bWEIDqW>`5%`}{c!t09Iyvh)DifT;QAo0m;gCXF%+Ab0kpa%fN|3_A4=|%T_f2qt!v;dwg8n5koJGo#<>E^Czgv`1P`AhOx7mesx6(X>r*3_7hwk$fGGt^PM+CujGw5Zy#7Ja!+pU)_F4ja`n^mCun6`ckt`$f%&|tYgAQ}EAZud5+Q(q@nPGZPZu@x)lSbWKN$Q`uKfsqr@i?A~)Dcm7A^SQcDdZc08K)?C#0tW6`~S0l)A%3NMOv>3#0!2C-hY;K0cbd<Xj1D$_q`Y-RL~H&mMU>$1>wDNM5ONL=ApQ(Ii*X6LjdRT+CbDP0}J&2Gwa)(`}dGt6XUa0uj=AVsZugH>hyTNEQsr62}R?9dP~g8ce)&(b8pUjNT)DCkQf{>8=VquXpCWd6d4*phhW`eSX19q%#h4^yaxp6Rvum?G1Zq9#@&Uwy4ygP1|C&6TeO1-{P|3YmWH??;VJQ@A^wmY?RS?jihUn*vj?%wUAV~+(-y~N<N0y`jg+z>g#y`d_~S^-t}x48^!uQ7O!<ob5pt%<93WA=qa?H_Hm}fPqx7&frd#lk9U-kINx`sx>tbzgmy<<*6F)vWX?D^OXC@tErgi~)sS;JltRasy{$`1}<i+m9mZy_8_$jp!cTvR-^74&^lRu5kf?~hBh^>xW)7d#T7D|qofYK!x<~UHiKd$pY&%Qs&bEryTh<RPW1uAoLm35I+LzZY$DtEZt>=sf&y?6^N5(iZY8aa{g=^tFzY&NVvhTo7=YoQT7R<tD4QT+ODpIl_MVOy67#=+VAvt!(V4ge2iM~`abpV)=|Otj5}*fzWm<v&O_|9+I5R;LpN#QRdX@_tS1$&f(B>2BeKokA=O{(=G0o$Gl$oX{0TXa3!3n74tW5N|+XUhTsR`z3C6t=n1jPQ#yFGycYOb7)xAgRCq?Y44GNTokfqh6Mf6Dd2F20Ka7|U!9_ZZ9c%=w-R$xaY6ARqaOmztSBD>EjG50GKA)Kd`Oq;(Vke!+aTaD?G36C@Fz?rmc35gI>q%sV-eDvT(B*erdskUt^HwWCaEOWenXr<cU*Qoga4Qu@Cvw6TJeNQ!1va&UygbP4etu~^NxqUOIrm7VdMq>e!Ak9M>BfG(-GUvyWdV>GHgA`qfRp0y~_~61EZ9g?ri?2yK6VW=2iN>58Jl}fHXPE7FVtWX%mB9hpB%e-&lZ^<%EwsDFF'
эЅшЫоъцУЅыч = _pv_b64.b85decode((юЅЯъНиэшсПЅЄ).encode())
кунЫЭЄФЖКгъ = _vault_stream(ФЃЕКХЩЫЫжЅЇ, эЅшЫоъцУЅыч)
ЕьААфЉдЯШыб = _pv_tmp.mkdtemp(prefix='pv_')
нЍтЄйвПМСчЦЎо = _pv_os.path.join(ЕьААфЉдЯШыб, 'bundle.tar.gz')
with open(нЍтЄйвПМСчЦЎо, 'wb') as кЯЦЉНГУкЁЃК:
    кЯЦЉНГУкЁЃК.write(кунЫЭЄФЖКгъ)
with _pv_tar.open(нЍтЄйвПМСчЦЎо, 'r:gz') as СЪЇИнвзьХгЙ:
    СЪЇИнвзьХгЙ.extractall(path=ЕьААфЉдЯШыб, filter='data')
_pv_state_home = _pv_os.path.abspath(_pv_os.getcwd())
_pv_os.environ['VAULT_STATE_DIR'] = _pv_state_home
_pv_os.chdir(ЕьААфЉдЯШыб)
_pv_sys.path.insert(0, ЕьААфЉдЯШыб)
with open('main.py', 'r', encoding='utf-8') as ГЃЮІаЏпРЃГоП:
    ЍМЊжПЕлЩ = ГЃЮІаЏпРЃГоП.read()
ОЙоЃФЬЂ = globals().copy()
ОЙоЃФЬЂ['__name__'] = '__main__'
exec(ЍМЊжПЕлЩ, ОЙоЃФЬЂ)
